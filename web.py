from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def main():
    return render_template("./templates/main.html")
if __name__=='main':
    app.run()