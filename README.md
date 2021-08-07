# Flask-web-site-with-python

### This is an example for how to use the flask packages in python to create a local hosted website

---

#### First you have to install the flask packages for it to work by going in to terminal and typing in "pip install flask", and know a bit of how to write code in python and especially in html, for you to be able to continue working with flask and making a website.
---


After that you will have to make a directory with the example name `flask`.

In the `flask` directory you will make a pyhton file, for this example the file name is `app.py`, and another directory with name `templates`.

In the `templates` directory you can have as many templates you wan't but for this exampel we will have to html files named `layout1.html` and `main.html`

---------------------------------------

In the `app.py` file I have made a bit of starter code:

```python:
from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

# this will render the main.html file in the templates folder if the URL has nothing to add
@app.route('/')
def start_site():
    return render_template("main.html")


# the "app.route" checks the URL for the layout1 and changes the html file to the render_template you have chosen
@app.route('/layout1')
def layoute1():     # if you want to make a python code for example a working light switch thure the internet or a pyhton car, that I have uploaded in my github "https://github.com/The1lama"
    return render_template("layout1.html")    # the layout1.html can be what ever file name you want just the file should be a working html file 

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)   # sets up the ip number and port for the website 
```

---------------------------------------

#### In the `templates` directory I have added two files `layout1.html` and `main.html`

---------------------------------------

In the `main.html` file I have made a bit of html code:
```html:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<head>
   <title>Look at this</title>
   <link rel="stylesheet" media="screen" href ="static/bootstrap.min.css">
   <link rel="stylesheet" href="static/bootstrap-theme.min.css">
   <meta name="viewport" content = "width=device-width, initial-scale=1.0">

</head>

<body style="background: rgb((248,248,255)">
<h1 style="text-decoration:underline; text-align:center; font-weight:bold;">This is the website</h1>
<h2 style=" "> This can change the website look</h2>

<h2>
<button>
<a href="/layout1" style="color: black;"> layout1</a>
</button>
</h2>

<h2 style="text-align:left; font-weight:bold;">This is a link to the main Flask website </h2>

<h2>
<button>
<a href="https://flask.palletsprojects.com/en/2.0.x/" style="color: black;">To the Flask website</a>
</button>
</h2>

</html>

```

and then the `layout1.html` file code

```html:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<head>
   <title>Look at this</title>
   <link rel="stylesheet" media="screen" href ="static/bootstrap.min.css">
   <link rel="stylesheet" href="static/bootstrap-theme.min.css">
   <meta name="viewport" content = "width=device-width, initial-scale=1.0">

</head>

<body style="background: rgb(98, 196, 155)">
<h1 style="text-decoration:underline; text-align:center; font-weight:bold;">This is the website</h1>
<h2 style=" "> das</h2>


<button>
<a href="/" style="color: black;"> start site </a>
</button>


</html>
```


