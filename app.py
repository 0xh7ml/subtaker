from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    return '// Poc By test N00B //11-03-2023 ', 200
 
if (__name__) == "__main__":
    app.run()
