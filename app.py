from flask import Flask, render_template, request
app = Flask(__name__)

todos=[]

@app.route('/', methods=['GET','POST'])
def home():
    name="Red"
    age=22
    names=["Red","John","Alice","Bob"]
    todo=""
    if request.method == 'POST':
        todo = request.form['todo']
        todos.append(todo)
        return render_template('home.html',name=name,age=age,names=names,todos=todos)
    return render_template('home.html',name=name,age=age,names=names,todos=todos)

@app.route('/about')
def about():
    return "I am learning flask"

@app.route('/contact')
def contact():
    return "Contact me at:"

if __name__=='__main__':
    app.run(debug=True)