# Flask-web-site-with-python

## This is an example for how to use the flask packages in python to create a local hosted website

---

### First you have to install the flask packages for it to work by going in to terminal and typing in "pip install flask", and know a bit of how to write code in python and especially in html, for you to be able to continue working with flask and making a website

---

After that you will have to make a directory with the example name `flask`.

In the `flask` directory you will make a pyhton file, for this example the file name is `app.py`, and another directory with name `templates`.

In the `templates` directory you can have as many templates you wan't but for this exampel we will have to html files named `layout1.html` and `main.html`

---

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

---

#### In the `templates` directory I have added two files `layout1.html` and `main.html`

---

In the `main.html` file I have made a bit of html code:

```html:
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<head>
   <title>Look at this</title>
   <link rel="stylesheet" media="screen" href ="static/bootstrap.min.css">
   <link rel="stylesheet" href="static/bootstrap-theme.min.css">
   <meta name="viewport" content = "width=device-width, initial-scale=1.0">

</head>

<body style="background: rgb(152,244,174)">
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

<h2>
<img src="https://imgr.search.brave.com/2IiQwtnoLp9m3LSWYShdm2rMJfc591KTsWQ3ZVh9lmU/fit/1200/487/no/1/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi9kL2Q5L0hl/bGxvXyh5ZWxsb3cp/LnN2Zy8xMjAwcHgt/SGVsbG9fKHllbGxv/dykuc3ZnLnBuZw" alt="Hello there" width="1080" height="350">
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

<p>
<img src="https://imgr.search.brave.com/NDud3gnY1lG_VA4DkJRhX9f91WiCsnamHP4AAKDA6HQ/fit/630/630/no/1/aHR0cHM6Ly9yZXMu/Y2xvdWRpbmFyeS5j/b20vdGVlcHVibGlj/L2ltYWdlL3ByaXZh/dGUvcy0tOFpReXRx/LWctLS90X1ByZXZp/ZXcvYl9yZ2I6MjYy/YzNhLGNfbGltaXQs/Zl9hdXRvLGhfNjMw/LHFfOTAsd182MzAv/djE1NDI5MDQ5NzAv/cHJvZHVjdGlvbi9k/ZXNpZ25zLzM1NTYw/NTJfMC5qcGc" alt="some_text" width="200" height="200">
</p>

</html>

```

---

### Some useful links for you to start with creating a website

* For [HTML](https://www.w3schools.com/html/ "w3schools.com") code
* How to use [FLASK](https://flask.palletsprojects.com/en/2.0.x/ "Flask own website")
* For an exampel to combine the website and a raspberry pi to make a car [GITHUB](https://github.com/The1lama/python-car-L298N-motor-driver-with-web-controller "The project")

---
