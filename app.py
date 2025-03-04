from flask import Flask
app = Flask( __name__ )
@app.route("/")
def hello():
    return "Hello, I'm Ruigu Joseph"
if __name__  == " main ":
    app.run(debug= True)