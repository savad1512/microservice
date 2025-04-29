from fastapi import FastAPI, Query, HTTPException # type: ignore

import psycopg2 # type: ignore

app = FastAPI()

# Database connection (PostgreSQL)
conn = psycopg2.connect("dbname=user_db user=dbadmin password=mysql12345 host=my-db.cz6ecsuycumr.us-east-1.rds.amazonaws.com")
cursor = conn.cursor()

@app.get("/users/")
def get_users(
    user_id: int | None = Query(None, description="User ID (required if user_name is not provided)"),
    user_name: str | None = Query(None, description="user_name (required if user_id is not provided)")
):
    if user_id is None and user_name is None:
        raise HTTPException(status_code=400, detail="Either user_id or user_name must be provided.")
    cursor.execute(
        "SELECT user_id, user_name, mobile_number FROM users WHERE user_id = %s or user_name = %s",
        (user_id,user_name)
    )
    users = cursor.fetchone()
    if users:
        return {
            "user_id" : users[0],
            "user_name" : users[1],
            "mobile_number" : users[2],
        }
    raise HTTPException(status_code=404, detail="users not found")


























# from fastapi import FastAPI
# import psycopg2

# app = FastAPI()

# # Database connection (PostgreSQL)
# conn = psycopg2.connect("dbname=user_db user=postgres password=secret host=db")
# cursor = conn.cursor()

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
#     user = cursor.fetchone()
#     return {"user": user}
