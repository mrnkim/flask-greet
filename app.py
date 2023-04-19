from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def show_welcome():
    return "<h1>welcome</h1>"

@app.get('/welcome/<page>')
def show_welcome_page(page):
    return f"<h1>welcome {page}</h1>"
