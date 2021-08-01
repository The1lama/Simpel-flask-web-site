from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

# this will render the main.html file in the templates folder if the URL has nothing to add
@app.route('/')
def start_site():
    return render_template("main.html")


# the "app.route" checks the URL for the layout1 and changes the html file to the render_template you have chosen
@app.route('/layout1')
def layoute1():  # if you want to make a python code for example a working light switch thure the internet or a pyhton car, that I have uploaded in my github "https://github.com/The1lama"
    return render_template("layout1.html") #the layout1.html can be what ever file name you want just the file should be a working html file 

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True) #sets up the ip number and port for the website 
