from flask import Blueprint, render_template
from flask_login import login_required, current_user
from create_app import create_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

# Initialize the app using the create_app function
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
