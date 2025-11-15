from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_name = request.form["student_name"]
        school_name = request.form["school_name"]
        class_name = request.form["class_name"]

        conn = get_connection()
        cur = conn.cursor()
        qry = "INSERT INTO student VALUES(%s, %s, %s)"
        data = (student_name, school_name, class_name)
        cur.execute(qry, data)
        conn.commit()
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM student")
    students = cur.fetchall()
    return render_template("index.html", students=students)

@app.route("/about")
def about():
    return "About Us"

def get_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="KByte@21",
        database="prayas"
    )   
    return conn

app.run(debug=True)
