#!/usr/bin/env python3

# Russell Felts
# Simple Time Server Assignment 05

""" Main """

import os
import time

from flask import Flask # render_template, request, redirect, url_for, session


APP = Flask(__name__)


@APP.route('/time/')
def get_time():
    """
    Display the time
    :return: The time
    """
    return str(time.time())


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 6738))
    APP.run(host='0.0.0.0', port=PORT)
