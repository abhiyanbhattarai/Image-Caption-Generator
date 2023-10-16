from website import create_app

from flask import redirect, url_for

app = create_app()

# Redirect to the login page when the app is started
@app.route('/login')
def index():
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run(debug=True)

