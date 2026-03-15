from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db.ehxbhicothvwggaupgzm.supabase.co",
    database="postgres",
    user="postgres",
    password="Ra04Ma10Na05",
    port="5432"
)

@app.route("/")
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", products=data)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    qty = request.form["qty"]
    price = request.form["price"]
    supplier = request.form["supplier"]

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, quantity, price, supplier) VALUES (%s,%s,%s,%s)",
        (name, qty, price, supplier)
    )
    conn.commit()
    cur.close()

    return redirect("/")

app.run()
