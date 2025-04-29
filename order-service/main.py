from fastapi import FastAPI, Query, HTTPException # type: ignore
import psycopg2 # type: ignore

app = FastAPI()

# Database connection
conn = psycopg2.connect("dbname=order_db user=dbadmin password=mysql12345 host=my-db.cz6ecsuycumr.us-east-1.rds.amazonaws.com")
cursor = conn.cursor()

@app.get("/health")
def health_check():
    try:
        cursor.execute("SELECT 1")
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
    
@app.get("/orders/")
def get_order(
    order_id: int | None = Query(None, description="Order ID (required if customer_name is not provided)"),
    customer_name: str | None = Query(None, description="Customer name (required if order_id is not provided)")
): 
    if order_id is None and customer_name is None:
        raise HTTPException(status_code=400, detail="Either order_id or customer_name must be provided.")   
    cursor.execute(
        "SELECT order_id, order_name, customer_name, order_date, total_amount FROM orders WHERE order_id = %s or customer_name = %s",
        (order_id,customer_name)
    )
    order = cursor.fetchone()
    if order:
        return {
            "order_id": order[0],
            "order_name": order[1],
            "customer_name": order[2],
            "order_date": order[3],
            "total_amount": order[4],
        }
    raise HTTPException(status_code=404, detail="Order not found")
