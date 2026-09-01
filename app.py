from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

todos=[]

@app.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        todo = {
            "text":request.form['todo'],
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

if __name__=='__main__':
    app.run(debug=True)