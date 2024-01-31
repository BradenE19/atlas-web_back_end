#!/usr/bin/env python3
""" Create a basic Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """configure available languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


def get_user():
    """ Return user dict if exists """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            # In case user_id is not an integer
            return None
    return None


@babel.localeselector
def get_locale():
    """return user preferred locale"""
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale
    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """get users preferred locale / language"""
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """return index.html template"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
