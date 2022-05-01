from os import environ
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request
from dotenv import load_dotenv
import requests, time


load_dotenv(dotenv_path="../.env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[environ["ALLOWED_ORIGIN"]],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host=environ["REDIS_HOST"],
    port=environ["REDIS_PORT"],
    password=environ["REDIS_PSWD"],
    decode_responses=True,
)


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending, completed, and refunded

    class Meta:
        database = redis


@app.get("/orders")
def all():
    return Order.all_pks()


@app.get("/orders/{pk}")
def get_order(pk):
    return Order.get(pk)


@app.post("/orders")
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    resp = requests.get(environ["INVENTORY_URL"] + "/%s" % body["id"])
    product = resp.json()

    order = Order(
        product_id=body["id"],
        price=product["price"],
        fee=0.2 * product["price"],
        total=1.2 * product["price"],
        quantity=body["quantity"],
        status="pending",
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order


def order_completed(order: Order):
    time.sleep(5)
    order.status = "completed"
    order.save()
