# Import necessary classes and modules from the flask and flask_sqlalchemy packages
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create an instance of the Flask class for our web app
app = Flask(__name__)

# Configure the SQLite database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# Initialize the SQLAlchemy object with the Flask app
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as an integer and the primary key
    name = db.Column(db.String(80), nullable=False)  # Define the name column as a string of max length 80, and it cannot be null

    def __repr__(self):
        # Define how the User object is represented
        return f'<User {self.name}>'

# Define a BlogPost model for the database
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Define the id column as an integer and the primary key
    title = db.Column(db.String(120), nullable=False)  # Define the title column as a string of max length 120, and it cannot be null
    content = db.Column(db.Text, nullable=False)  # Define the content column as text, and it cannot be null
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Define a foreign key to associate the blog post with a user
    user = db.relationship('User', back_populates='posts')  # Define the relationship with the User model

# Add a relationship attribute to the User model
User.posts = db.relationship('BlogPost', order_by=BlogPost.id, back_populates='user')

# Push an application context and create the database and the User table
with app.app_context():
    db.create_all()

# Define a route for the root URL ("/")
@app.route('/')
def hello():
    # Return a simple response for the root URL
    return "Hello, World!"

# Define a route that accepts a dynamic parameter in the URL
@app.route('/<name>')
def hello_name(name):
    # Return a personalized greeting using the dynamic parameter
    return f"Hello, {name}!"

# Define a route to serve the form
@app.route('/form')
def form():
    # Render the HTML form template
    return render_template('form.html')

# Define a route to handle form submissions via POST method
@app.route('/greet', methods=['POST'])
def greet_post():
    # Get the name from the submitted form data
    name = request.form['name']
    # Create a new User instance with the submitted name
    new_user = User(name=name)
    # Add the new user to the database session
    db.session.add(new_user)
    # Commit the session to save the new user to the database
    db.session.commit()
    # Render the index.html template with the name variable
    return render_template('index.html', name=name)

# Define a route to list all users
@app.route('/users')
def list_users():
    # Query all users from the database
    users = User.query.all()
    # Render the users.html template with the list of users
    return render_template('users.html', users=users)

# Define a route to delete all users
@app.route('/delete_users', methods=['POST'])
def delete_users():
    # Delete all users from the database
    User.query.delete()
    # Commit the session to save the changes to the database
    db.session.commit()
    # Redirect to the list users page
    return redirect(url_for('list_users'))

# Define a route to serve the blog post form
@app.route('/post_blog')
def post_blog():
    # Render the HTML form template for creating a blog post
    return render_template('post_blog.html')

# Define a route to handle blog post submissions via POST method
@app.route('/submit_blog', methods=['POST'])
def submit_blog():
    # Get the title and content from the submitted form data
    title = request.form['title']
    content = request.form['content']
    user_name = request.form['user_name']
    
    # Find the user by name
    user = User.query.filter_by(name=user_name).first()
    
    if user:
        # Create a new BlogPost instance with the submitted data
        new_post = BlogPost(title=title, content=content, user_id=user.id)
        # Add the new blog post to the database session
        db.session.add(new_post)
        # Commit the session to save the new blog post to the database
        db.session.commit()
        return redirect(url_for('list_blogs', user_id=user.id))
    else:
        return "User not found", 404

# Define a route to list all blog posts of a specific user
@app.route('/blogs/<int:user_id>')
def list_blogs(user_id):
    # Query all blog posts of the specific user from the database
    user = User.query.get(user_id)
    if user:
        return render_template('blogs.html', user=user)
    else:
        return "User not found", 404

# Check if the script is run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask web server with debugging enabled
    app.run(debug=True)
