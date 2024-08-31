from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for form CSRF protection

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)

@app.route('/home')
def home():
    return 'Home Page'

if __name__ == '__main__':
    app.run(debug=True)
