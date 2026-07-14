from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from tinydb import TinyDB
from datetime import datetime

app = FastAPI()

# TinyDB database
db = TinyDB("orders.json")
orders = db.table("orders")

# HTML templates
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    all_orders = orders.all()

    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"orders": orders}
)

# Add new order
@app.post("/orders")
def add_order(
    item: str = Form(...),
    qty: int = Form(...),
    table_number: int = Form(...)
):

    order = {
        "item": item,
        "qty": qty,
        "table_number": table_number,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    orders.insert(order)

    return RedirectResponse(
        url="/",
        status_code=303
    )


# API endpoint to view orders
@app.get("/api/orders")
def get_orders():

    return orders.all()


# Delete order
@app.delete("/orders/{order_id}")
def delete_order(order_id: int):

    orders.remove(doc_ids=[order_id])

    return {
        "message": "Order deleted successfully"
    }
