from flask import Flask, render_template, request, redirect
from friends import Friend

app = Flask('__name__')

@app.route('/')
def index():
    friends =Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)

@app.route('/about')
def about():
     return render_template("about.html")

@app.route('/contact')
def contact():
     return render_template("contact.html")

# @app.route('/home')
# def home():
#      return render_template("home.html")

@app.route('/project')
def project():
     return render_template("project.html")

@app.route('/login')
def login():
     return render_template("login.html")

@app.route('/register')
def register():
     return render_template("register.html")

@app.route('/create_friend' ,methods=['post'])
def create_name():
     #create a dictionary with data collected from the form
     data = {
          "first_name": request.form['fname'],
          "last_name": request.form['lname'],
          "occupation": request.form['occ']
     }
     Friend.save(data)
     return redirect('/')

@app.route('/friend/details/<int:friend_id>')
def show_details(friend_id):
     data = {
           "id": friend_id
     }
     friend_details = Friend.get_one(data)
     return render_template('actions/details.html', details =friend_details)

   
@app.route('/friend/edit/<int:friend_id>')
def edit_details(friend_id):
     data = {
           "id": friend_id
     }
     friend_details = Friend.get_one(data)
     return render_template('actions/edit.html', details =friend_details)

@app.route('/friend/update', methods=["POST"])
def update_details():
     data = {
          'id': request.form['id'],
          'first_name': request.form['first_name'],
          'last_name': request.form['last_name'],
          'occupation': request.form['occupation']
     }
     Friend.update(data)
     return redirect('/')

@app.route('/friend/remove/<int: friend>')
def delete(friend_id):
     data = {
          'id': friend_id
     }
     Friend.remove(data)
     return redirect('/')

     return redirect('/')

   
if __name__ =="__main__":
     app.run(debug= True, host='localhost', port=8000)