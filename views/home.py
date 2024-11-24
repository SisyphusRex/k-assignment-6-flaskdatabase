"""home views"""

# Third Party Imports
from flask import render_template


def home_view():
    """home view"""
    return render_template("home.html")


def contact_view():
    """contact view"""
    return render_template("contact.html")
