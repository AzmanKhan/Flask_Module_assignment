from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_form():
    name = None
    if request.method == 'POST':
        name = request.form.get('name')
    return render_template('form.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
