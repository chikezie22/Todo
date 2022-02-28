from flask import Flask, render_template, redirect, request, url_for
#from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import primary_key
#import os

app = Flask(__name__)

todoData = []
#find the curren app path directory
#project_dir = os.path.dirname(os.path.abspath(__file__))
#database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))

#connecting the database file (todo.db) to the SQLALchemy dependencies

#app.config["SQLALCHEMY_DATABASE_URI"]=database_file
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

#db=SQLAlchemy(app)
#class Todo(db.Model):
    ##todo = db.Column(db.String(30), unique=False, nullable=False, primary_key=True)

    #def __repr__(self) :
    #    return f"Todo: {self.todo}"


@app.route('/')
def home():
    return render_template("index.html", todos=todoData)


@app.route('/create-todo', methods=['POST'])
def create_todo():
    new_todo = request.form.get("new_todo")
    todoData.append(new_todo) #to add to a list use append
    print(todoData)
    return redirect(url_for('home')) # takes us back to home

@app.route('/delete/<todo_item>')
def delete(todo_item):
    print(todo_item)
    todoData.remove(todo_item)
    return redirect(url_for('home'))

item = ''
@app.route('/update/<todo_item>', methods=['GET','POST']) #renders page to update
def update(todo_item):

    index = todoData.index(todo_item) #gets index of item to be changed

    global item     # make this variable global(accessible outside this scope)
    item = index

    return render_template('update.html', todo_item=todo_item) # render and take todo_item


@app.route('/update_item', methods=['POST'])  #performs the update function
def update_item():
    if request.method == 'POST':
        new_item = request.form.get('new_item')  #get that particular item u just updated from the form
        todoData[item] = new_item  # set the new item to index of the old item to replace the old one

    return redirect(url_for('home')) # redirect to index page



if __name__=="__main__":
    app.run(debug=True)
