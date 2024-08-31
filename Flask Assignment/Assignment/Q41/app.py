from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template_string('<h1>Hello, {{ name }}!</h1>', name=name)

if __name__ == '__main__':
    app.run(debug=True)
