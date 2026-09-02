from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

todos=[]

@app.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        todo=request.form['todo']

        if not todo:
            return render_template('home.html',todos=todos,error="Field is empty!")
        
        todo = {
            "text":todo ,
            "completed":False
        }
        todos.append(todo)
        
    return render_template('home.html',todos=todos)

@app.route('/delete/<int:index>')
def delete(index):
    todos.pop(index)
    return redirect(url_for('home'))

@app.route('/completed/<int:index>')
def completed(index):
    todos[index]["completed"]=not todos[index]["completed"]
    return redirect(url_for('home'))

@app.route('/edit/<int:index>',methods=['GET','POST'])
def edit(index):
    if request.method=="POST":
        ntext=request.form['text']
        if not ntext:
            return render_template('edit.html',text=ntext, error="Field is empty!")
        todos[index]["text"]=ntext
        return redirect(url_for('home'))
    return render_template('edit.html',text=todos[index]["text"])

if __name__=='__main__':
    app.run(debug=True)