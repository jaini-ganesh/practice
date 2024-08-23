from flask import *
from database.dbconnection import db

website=Flask(__name__)
website.secret_key="auhdu"
cursor=db.cursor()


@website.route('/',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        phone=request.form['phno']
        address=request.form['addr']

        cursor.execute("insert into users values(%s,%s,%s,%s)",(username,email,phone,address))
        db.commit()
        flash("Data inserted successfully")

        return redirect(url_for('submit'))

    cursor.execute("select * from users")
    users=cursor.fetchall()
    return render_template('webpage.html',users=users)


if __name__=="__main__":
    website.run(debug=True)