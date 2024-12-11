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
    status = request.form.get("status")

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
        status=status,
    )


def beverage_sort_by_active_true_view():
    """display list sorted by id"""
    beverages = db_session.query(Beverage).all()
    new_beverages = []
    for index, element in enumerate(beverages):
        if beverages[index].active is True:
            new_beverages.append(element)

    return render_template(
        "beverage/beverage_list.html",
        beverages=new_beverages,
    )


def beverage_sort_by_pack_ascending_view():
    """display list sorted by id"""
    beverages = db_session.query(Beverage).all()
    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].pack < beverages[index2].pack:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_pack_descending_view():
    """display list sorted by id"""
    beverages = db_session.query(Beverage).all()
    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].pack > beverages[index2].pack:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_id_ascending_view():
    """display list sorted by id"""
    beverages = db_session.query(Beverage).all()
    status = request.form.get("status")
    new_beverages = []

    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].id < beverages[index2].id:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    if status == "0":
        for index, element in enumerate(beverages):
            if beverages[index].active is False:
                new_beverages.append(beverages[index])

    if status == "1":
        for index, element in enumerate(beverages):
            if beverages[index].active is True:
                new_beverages.append(beverages[index])

    if status == "":
        new_beverages = beverages

    return render_template(
        "beverage/beverage_list.html",
        beverages=new_beverages,
        status=status,
    )


def beverage_sort_by_id_descending_view():
    """display list sorted by id"""
    beverages = db_session.query(Beverage).all()
    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].id > beverages[index2].id:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_name_ascending_view():
    """display list sorted by name"""
    beverages = db_session.query(Beverage).all()

    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].name < beverages[index2].name:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_name_descending_view():
    """display list sorted by name"""
    beverages = db_session.query(Beverage).all()

    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].name > beverages[index2].name:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_price_ascending_view():
    """sort by price"""
    beverages = db_session.query(Beverage).all()

    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].price < beverages[index2].price:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

    return render_template(
        "beverage/beverage_list.html",
        beverages=beverages,
    )


def beverage_sort_by_price_descending_view():
    """sort by price"""
    beverages = db_session.query(Beverage).all()

    for index in range(len(beverages)):
        for index2 in range(len(beverages)):
            if beverages[index].price > beverages[index2].price:
                temp = beverages[index]
                beverages[index] = beverages[index2]
                beverages[index2] = temp

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
