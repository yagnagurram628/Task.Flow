import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def get_db():
    db=sqlite3.connect('todo.db')
    db.row_factory=sqlite3.Row
    db.execute("""
    CREATE TABLE IF NOT EXISTS todo(
        id INTEGER PRIMARY KEY,
        text TEXT,
        completed INTEGER)
        """)
    db.commit()
    return db

@app.route('/', methods=['GET','POST'])
def home():

    db=get_db()
    if request.method == 'POST':
        todo=request.form['todo'].strip()

        if not todo:
            todos=db.execute("SELECT * FROM todo")
            return render_template('home.html',todos=todos,error="Field is empty!")

        db.execute("""
            INSERT INTO todo (text,completed)
            VALUES(?,0)
        """,(todo,))
        db.commit()

    todos=db.execute("SELECT * FROM todo")    
    return render_template('home.html',todos=todos)

@app.route('/delete/<int:id>')
def delete(id):
    db=get_db()
    db.execute("DELETE FROM todo WHERE id=?",(id,))
    db.commit()

    return redirect(url_for('home'))

@app.route('/completed/<int:id>')
def completed(id):
    db=get_db()
    db.execute("""
        UPDATE todo
        SET completed=1-completed
        WHERE id=?
    """,(id,))
    db.commit()

    return redirect(url_for('home'))

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    db=get_db()
    if request.method=="POST":
        ntext=request.form['text'].strip()
        if not ntext:
            return render_template('edit.html',text=ntext, error="Field is empty!")
        db.execute("""
        UPDATE todo
        SET text=?
        WHERE id=?
        """,(ntext,id))
        db.commit()
        return redirect(url_for('home'))
    text=db.execute("SELECT text FROM todo where id=?",(id,)).fetchone()
    return render_template('edit.html',text=text["text"])

if __name__=='__main__':
    app.run(debug=True)