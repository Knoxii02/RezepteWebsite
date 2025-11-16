from recipes import app, db, limiter
from flask import render_template, request, redirect, url_for
from sqlalchemy import text

@app.route('/')
def home_page():
    cookie = request.cookies.get('username')
    print("<>home_page", cookie)
    return render_template("home.html", cookie=cookie)

@app.route('/rezepte')
def rezepte_page():
    cookie = request.cookies.get('username')
    print("<>rezepte_page", cookie)
    
    search = request.args.get('search', '')
    
    if search:
        qstmt = text("SELECT * FROM rezepte WHERE name LIKE :search")
        print(f"Search query with param: {search}")
        result = db.session.execute(qstmt, {"search": search})
    else:
        result = db.session.execute(text("SELECT * FROM rezepte"))
    
    rezepte = result.fetchall()
    print(f"Found {len(rezepte)} rezepte")
    return render_template("rezepte.html", rezepte=rezepte, cookie=cookie)

@app.route('/rezept/<rezept_id>')
def rezept_page(rezept_id):
    cookie = request.cookies.get('username')
    if not cookie:
        return redirect(url_for('login_page'))
    qstmt = text("SELECT * FROM rezepte WHERE id = :id")
    result = db.session.execute(qstmt, {"id": rezept_id})
    rezept = result.fetchone()
    return render_template("rezept.html", rezept=rezept, cookie=cookie)

@app.route('/rezept/hinzufuegen', methods=['GET', 'POST'])
def rezept_hinzufuegen_page():
    cookie = request.cookies.get('username')
    if not cookie:
        return redirect(url_for('login_page'))
    if request.method == 'POST':
        name = request.form.get('Name')
        dauer = request.form.get('Dauer')
        kalorien = request.form.get('Kalorien')
        zutaten = request.form.get('Zutaten')
        zubereitung = request.form.get('Zubereitung')

        if not name or not dauer or not kalorien or not zutaten or not zubereitung:
            print("Inputs dürfen nicht leer sein")
            return render_template("rezept_hinzufuegen.html", cookie=cookie)

        qstmt = text("INSERT INTO rezepte (name, dauer, kalorien, zutaten, zubereitung) VALUES (:name, :dauer, :kalorien, :zutaten, :zubereitung)")
        
        print(f"Executing query with params: name={name}, dauer={dauer}")
        db.session.execute(qstmt, {"name": name, "dauer": dauer, "kalorien": kalorien, "zutaten": zutaten, "zubereitung": zubereitung})
        db.session.commit()

        print("Rezept hinzugefügt")
        resp = redirect("/rezepte")
        return resp
    return render_template("rezept_hinzufuegen.html", cookie=cookie)

@app.route('/login', methods=['GET','POST'])
@limiter.limit("5 per minute")
def login_page():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        
        if username is None or isinstance(username, str) is False or len(username) < 3:
            print("Invalid username")
            return render_template("login.html", cookie=None)
        
        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Invalid password")
            return render_template("login.html", cookie=None)

        qstmt = text("SELECT * FROM bugusers WHERE username = :username AND password = :password")
        print(f"Executing query with params: username={username}")
        result = db.session.execute(qstmt, {"username": username, "password": password})
        user = result.fetchall()
        
        if not user:
            print("Login failed")
            return render_template("login.html", cookie=None)
        
        print("Login successful")
        resp = redirect("/rezepte")
        resp.set_cookie('username', username)
        return resp
    return render_template("login.html", cookie=None)
    

@app.route('/register', methods=['GET', 'POST'])
@limiter.limit("3 per hour")
def register_page():
    if request.method == 'POST':
        username = request.form.get('Username')
        password = request.form.get('Password')
        email = request.form.get('Email')

        if username is None or isinstance(username, str) is False or len(username) < 3:
            print("Invalid username")
            return render_template("register.html", cookie=None)

        if password is None or isinstance(password, str) is False or len(password) < 3:
            print("Invalid password")
            return render_template("register.html", cookie=None)

        if email is None or isinstance(email, str) is False or "@" not in email:
            print("Invalid email")
            return render_template("register.html", cookie=None)

        qstmt = text("INSERT INTO bugusers (username, password, email_address) VALUES (:username, :password, :email)")
        
        print(f"Executing query with params: username={username}, email={email}")
        db.session.execute(qstmt, {"username": username, "password": password, "email": email})
        db.session.commit()

        print("Registration successful")
        resp = redirect("/login")
        return resp
    return render_template("register.html", cookie=None)

@app.route('/logout')
def logout():
    resp = redirect('/')
    resp.set_cookie('username', '', expires=0)
    return resp