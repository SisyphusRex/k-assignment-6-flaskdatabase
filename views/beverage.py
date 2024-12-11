# Third-party imports
from flask import flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker

# First-party imports
from models.beverage import Beverage

engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()


def beverage_list_view():
    """display a list of employees from the database"""
    beverages = db_session.query(Beverage).all()

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_add_view():
    """allow adding a beverage to database"""

    errors = []
    status = None
    if request.method == "POST":
        id_ = request.form["id"]
        name = request.form["name"]
        pack = request.form["pack"]
        price = request.form["price"]
        status = request.form.get("status")

        if not id_:
            errors.append("ID is required.")
        if not name:
            errors.append("Name is required.")
        if not pack:
            errors.append("Pack is required.")
        if not price:
            errors.append("Price is required.")
        if status is None:
            errors.append("Status active/inactive is required.")

        if not errors:
            new_beverage = Beverage(id_, name, pack, price, bool(status))

            db_session.add(new_beverage)
            db_session.commit()

            flash("Beverage added successfully!", "success")

            return redirect(url_for("beverage_list_view"))

    return render_template(
        "beverage/beverage_add.html",
        errors=errors,
        status=status,
    )


def beverage_edit_view(pk):
    """allow adding a beverage to database"""

    errors = []

    beverage = db_session.get(Beverage, pk)

    if not beverage:
        flash(f"Unknown beverage with pk of {pk}", "danger")
        return redirect(url_for("beverage_list_view"))

    if request.method == "POST":

        name = request.form["name"]
        pack = request.form["pack"]
        price = request.form["price"]
        status = request.form.get("status")

        if not name:
            errors.append("Name is required.")
        if not pack:
            errors.append("Pack is required.")
        if not price:
            errors.append("Price is required.")
        if status is None:
            errors.append("Status active/inactive is required.")

        if not errors:

            beverage.name = name
            beverage.pack = pack
            beverage.price = price
            beverage.active = bool(status)
            db_session.commit()

            flash("Beverage updated successfully!", "success")

            return redirect(url_for("beverage_list_view"))

    return render_template(
        "beverage/beverage_edit.html",
        beverage=beverage,
        errors=errors,
    )


def beverage_delete_view(pk):
    """delete beverage view"""
    errors = []
    beverage = db_session.get(Beverage, pk)

    if not beverage:
        flash(f"Unknown beverage with pk of {pk}", "danger")
        return redirect(url_for("beverage_list_view"))

    if beverage and request.method == "POST":
        db_session.delete(beverage)
        db_session.commit()

        flash("Beverage deleted successfully!", "success")

        return redirect(url_for("beverage_list_view"))

    return render_template(
        "beverage/beverage_delete.html",
        beverage=beverage,
        errors=errors,
    )
