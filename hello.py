from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Vamos testar isso... quero ver funcionar direito!!'
app.run()