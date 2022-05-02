# FastAPI Microservices
FastAPI microservices is a fun project for practicing microservices with FastAPI. It's architecture is based two backends: i.e. one for inventory and one for orders. The inventory backend is a simple REST API that provides a CRUD interface for managing products. The orders backend is a simple REST API that provides a CRUD interface for managing orders. The frontend is a React app that uses the FastAPI microservices to manage the inventory and orders.

## Technologies
- FastAPI
- Redis JSON
- Redis Streams
- React

## Usage
- Clone the repository:
    ```bash
    git clone https://github.com/sameeramin/fastapi-microservices.git
    cd fastapi-microservices
    ```
- Python envronment:
    ```bash
    # If you're using conda
    conda create -n fastapi python=3.7
    conda activate fastapi

    # If you're using virtualenv
    python3 -m venv fastapi
    source fastapi/bin/activate
    ```
- Install dependencies:
    ```bash
    pip install -r inventory/requirements.txt
    pip install -r payment/requirements.txt
    ```
- Run the server:
    ```bash
    uvicorn inventory/main:app --reload --port 8001
    uvicorn payment/main:app --reload
    ```
- Run the frontend:
    ```bash
    cd frontend
    npm install
    npm start
    ```


## Project Structure
```
- inventory/
    - main.py
    - .gitignore
    - consumer.py
    - requirements.txt
- payment/
    - main.py
    - .gitignore
    - requirements.txt
- frontend/
    - public/
    - src/
        - App.js
        - index.js
        - index.css
        - components/
    - package-lock.json
    - package.json
- README.md
- .gitignore
- .nvmrc
- .env
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Authors
- [Muhammad Sameer](https://github.com/sameeramin)
