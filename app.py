from sqlite3 import Cursor
from flask import Flask,render_template,redirect,request,flash,url_for,session
from flask_mysqldb import MySQL
from flask_login import current_user, user_accessed


app =Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hotel'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)


@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    q="select * from registeruser"
    cursor.execute(q)
    res = cursor.fetchall()
    return render_template('home.html',user=res)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/registeruser',methods=['GET','POST'])
def registeruser():
    cursor = mysql.connection.cursor()
    q="select*from room where Availability='Available'"
    cursor.execute(q)
    res = cursor.fetchall()
    
    if request.method == 'POST':
        flash('Customer Added successfully')
        name=request.form['name']
        email=request.form['email']
        phoneno=request.form['phoneno']
        gender=request.form['gender']
        roomno=request.form['roomno']
        cursor = mysql.connection.cursor()
        cursor.execute("insert into registeruser(name,email,phoneno,gender,roomno) values(%s,%s,%s,%s,%s)",(name,email,phoneno,gender,roomno))
        cursor.execute("update room set Availability='occupied' where roomno=%s",(roomno,))
        mysql.connection.commit()
        return redirect('/registeruser')
    return render_template('registeruser.html', res=res)

@app.route('/sidebar')
def sidebar():
    return render_template('/sidebar.html')

@app.route('/Rooms')
def Rooms():
    cursor = mysql.connection.cursor()
    q="select * from room"
    cursor.execute(q)
    res = cursor.fetchall()
    return render_template('Rooms.html',res=res)

@app.route('/Customer')
def Customer():
    cursor = mysql.connection.cursor()
    q="select * from registeruser"
    cursor.execute(q)
    res = cursor.fetchall()
    return render_template('Customer.html',res=res)

@app.route('/updateuser/<string:uid>')
def updateuser(uid):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from registeruser where uid=%s",(uid,))
    res=cursor.fetchall()
    return render_template('updateuser.html',user=res)

@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        flash("Customer Updated Successfully")
        name=request.form['name']
        email=request.form['email']
        phoneno=request.form['phoneno']
        gender=request.form['gender']
        roomno=request.form['roomno']
        cursor = mysql.connection.cursor()
        cursor.execute("update registeruser set name=%s,email=%s,phoneno=%s,gender=%s,roomno=%s",(name,email,phoneno,gender,roomno))
        mysql.connection.commit()
        return redirect('/Customer')

@app.route('/updateroom/<string:id_data>')
def updateroom(id_data):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from room where roomno=%s",(id_data,))
    res=cursor.fetchall()
    return render_template('updateroom.html',user=res)

@app.route('/update_room',methods=['GET','POST'])
def update_room():
    if request.method=='POST':
        flash("Room Updated Successfully")
        roomno=request.form['roomno']
        Availability=request.form['Availability']
        status=request.form['status']
        bedtype=request.form['bedtype']
        price=request.form['price']
        cursor = mysql.connection.cursor()
        cursor.execute("update room set roomno=%s,Availability=%s,status=%s,bedtype=%s,price=%s",(roomno,Availability,status,bedtype,price))
        mysql.connection.commit()
        return redirect('/Rooms')



@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Room Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("delete from room where roomno=%s",(id_data,))
    mysql.connection.commit()
    return redirect('/Rooms')

@app.route('/deleteuser/<string:id_data>/<string:data>', methods = ['GET','POST'])
def deleteuser(id_data,data):
    flash("Customer Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("update room set Availability='Available' where roomno=%s",(data,))
    cursor.execute("delete from registeruser where uid=%s",(id_data,))
    mysql.connection.commit()
    return redirect('/Customer')

@app.route("/contact")
def contact():
    return render_template('contact.html')     

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("SignUp Successfully")
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        mysql.connection.commit()
        return redirect('/')
    return render_template('navbar.html')  

@app.route('/log', methods = ['POST','GET'])
def log():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("select * from register where username=%s and password=%s", (username,password))
        data1=cur.fetchone()
        if username==username and password==password:
            flash("Login successfully")
            return redirect('/AddRoom')
        else:
            flash("invalid username and password")
            return redirect('/')
    return render_template('sidebar.html')

"""@app.route('/log',methods=['POST','GET'])
def log():
    status=True
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]
        cur=mysql.connection.cursor()
        cur.execute("select * from register where username=%s and password=%s",(username,password))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["username"]
            flash('Login Successfully','success')
            return redirect('sidebar')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("sidebar.html")"""

@app.route('/AddRoom',methods=['POST','GET'])
def AddRoom():
    if request.method=='POST':
        flash("Room Added successfully")
        roomno=request.form['roomno']
        Availability=request.form['Availability']
        status=request.form['status']
        bedtype=request.form['bedtype']
        price=request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO room(roomno,Availability,status,bedtype,price) VALUES (%s, %s, %s,%s,%s)", (roomno,Availability,status,bedtype,price))
        mysql.connection.commit()
        return redirect('/AddRoom')
    return render_template("AddRoom.html")

app.run(debug=True,port=5000)
