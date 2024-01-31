#!/usr/bin/env python3
""" Create a basic Flask App
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, refresh


class Config:
    """configure available languages"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """return best match for user locale """
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """return index.html template"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
