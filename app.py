from flask import Flask, render_template, redirect, url_for, flash, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/memberships')
def memberships():
    return render_template('membership.html')

@app.route('/login', )
def login():
    return render_template('login.html', )

@app.route('/signup', )
def signup():
   
    return render_template('signup.html', )

def gallery():
    images = [
        "image1.jpg", "image2.jpg", "image3.jpg",
        "image4.jpg", "image5.jpg", "image6.jpg"
    ] 
    return render_template('gallery.html', images=images)

# Contact Page Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
