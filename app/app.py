from flask import Flask


'''
This is a sample flask app.
'''

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Test URI!'


app.run()
