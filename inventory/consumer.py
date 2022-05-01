from itertools import product
from main import redis, Product
import time

key = "order_completed"
group = "inventory-group"

# Creating group for Redis Streams
try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists!")


while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)
        if results != []:
            for result in results:
                # [['order_completed', [('1651415732695-0', {'pk': '01G200RFD59GGPBW1DSJ1842C7',
                # 'product_id': '01G1YEXGKPWC25VVRT96YV9CVA', 'price': '5000.0', 'fee': '1000.0',
                # 'total': '6000.0', 'quantity': '1', 'status': 'completed'})]]]
                obj = result[1][0][1]
                product = Product.get(obj["product_id"])
                print(product)
                product.quantity = product.quantity - int(obj["quantity"])
                product.save()

    except Exception as e:
        print(str(e))

    time.sleep(1)
