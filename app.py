from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return '// Poc By N00B', 200
 
if (__name__) == "__main__":
    app.run()
