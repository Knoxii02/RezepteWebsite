from recipes import app, db
from flask import render_template, request, redirect, url_for
from sqlalchemy import text

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/rezepte')
def rezepte_page():
    qstmt = "SELECT * FROM rezepte"
    result = db.session.execute(text(qstmt))
    rezepte = result.fetchall()
    print(rezepte)
    return render_template("rezepte.html", rezepte=rezepte)

@app.route('/rezept/<int:rezept_id>')
def rezept_page(rezept_id):
    qstmt = f"SELECT * FROM rezepte WHERE id = {rezept_id}"
    result = db.session.execute(text(qstmt))
    rezept = result.fetchone()
    return render_template("rezept.html", rezept=rezept)

@app.route('/rezept/hinzufuegen', methods=['GET', 'POST'])
def rezept_hinzufuegen_page():
    if request.method == 'POST':
        name = request.form.get('Name')
        dauer = request.form.get('Dauer')
        kalorien = request.form.get('Kalorien')
        zutaten = request.form.get('Zutaten')
        zubereitung = request.form.get('Zubereitung')

        if not name or not dauer or not kalorien or not zutaten or not zubereitung:
            print("Inputs dürfen nicht leer sein")
            return render_template("rezept_hinzufuegen.html")

        qstmt = f"INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES ('{name}', '{dauer}', '{kalorien}', '{zutaten}', '{zubereitung}')"
        
        print(f"Executing query: {qstmt}")
        db.session.execute(text(qstmt))
        db.session.commit()

        print("Rezept hinzugefügt")
        resp = redirect("/rezepte")
        return resp
    return render_template("rezept_hinzufuegen.html")

@app.route('/login', methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        
        if username is None or isinstance(username, str) is False or len(username) < 3:
            print("Invalid username")
            return render_template("login.html")
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Invalid password")
            return render_template("login.html")

        qstmt = f"SELECT * FROM bugusers WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {qstmt}")
        result = db.session.execute(text(qstmt))
        user = result.fetchall()
        
        if not user:
            print("Login failed")
            return render_template("login.html")
        
        print("Login successful")
        resp = redirect("/rezepte")
        return resp
    return render_template("login.html")
    

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        email = request.form.get('Email')

        if username is None or isinstance(username, str) is False or len(username) < 3:
            print("Invalid username")
            return render_template("register.html")

        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Invalid password")
            return render_template("register.html")

        if email is None or isinstance(email, str) is False or "@" not in email:
            print("Invalid email")
            return render_template("register.html")

        qstmt = f"INSERT INTO bugusers (username, password, email_address) VALUES ('{username}', '{password}', '{email}')"
        
        print(f"Executing query: {qstmt}")
        db.session.execute(text(qstmt))
        db.session.commit()

        print("Registration successful")
        resp = redirect("/login")
        return resp
    return render_template("register.html")