"""Tiny Flask Example

From https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

Requires you to install flask in your virtual environment:

  $ . .venv/Scripts/activate

  $ python -m pip install flask

To run this on windows:

  Activate your environment if you haven't already.

  $ flask --app main run

Then in a browser go to http://127.0.0.1:5000/
"""

# System Imports

# First Party Imports
from views.home import (
    home_view,
    contact_view,
)

from views.beverage import (
    beverage_list_view,
    beverage_add_view,
    beverage_edit_view,
    beverage_delete_view,
    beverage_sort_by_id_ascending_view,
    beverage_sort_by_name_ascending_view,
    beverage_sort_by_price_ascending_view,
    beverage_sort_by_pack_ascending_view,
    beverage_sort_by_active_true_view,
    beverage_sort_by_id_descending_view,
    beverage_sort_by_name_descending_view,
    beverage_sort_by_pack_descending_view,
    beverage_sort_by_price_descending_view,
)

# Third Party Imports
from flask import Flask


app = Flask(__name__)

app.secret_key = b"TAf51nEWZkp4Z6EkZOjueDz0lTXCPemPYEomgrT6lo0"


# @app.route() lets you set the url path that will trigger each view.
# '/' is the root of the domain. If your website was hosted at example.com
# then the full url would be https://example.com/
# If the path was '/do/thing/' then the full url would be https://example.com/do/thing/
# @app.route("/")
# def hello_world():
#     # Return a string that will be the full response the browser gets
#     return "<h1>Hello, World!</h1>"
app.add_url_rule("/", view_func=home_view)
app.add_url_rule("/contact", view_func=contact_view)
app.add_url_rule("/beverages", view_func=beverage_list_view)
app.add_url_rule("/beverages/add", view_func=beverage_add_view, methods=["GET", "POST"])
app.add_url_rule(
    "/beverages/<string:pk>/edit",
    view_func=beverage_edit_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/beverages/<string:pk>/delete",
    view_func=beverage_delete_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/beverages/ascending_id", view_func=beverage_sort_by_id_ascending_view
)
app.add_url_rule(
    "/beverages/ascending_name", view_func=beverage_sort_by_name_ascending_view
)
app.add_url_rule(
    "/beverages/ascending_price", view_func=beverage_sort_by_price_ascending_view
)
app.add_url_rule(
    "/beverages/ascending_pack", view_func=beverage_sort_by_pack_ascending_view
)
app.add_url_rule(
    "/beverages/ascending_active", view_func=beverage_sort_by_active_true_view
)
app.add_url_rule(
    "/beverages/descending_id", view_func=beverage_sort_by_id_descending_view
)
app.add_url_rule(
    "/beverages/descending_name", view_func=beverage_sort_by_name_descending_view
)
app.add_url_rule(
    "/beverages/descending_pack", view_func=beverage_sort_by_pack_descending_view
)
app.add_url_rule(
    "/beverages/descending_price", view_func=beverage_sort_by_price_descending_view
)
