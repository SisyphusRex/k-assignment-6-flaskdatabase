"""unit test module"""

# System Imports
from unittest import TestCase

# First Party Imports
from models.beverage import Beverage
from views.beverage import beverage_list_view
from views.utils import Utilities

# Third Party Imports
from flask import flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()
utility = Utilities()


class BeverageListViewTest(TestCase):
    """class to test beverage_list_view()"""

    def test_beverage_list_view(self):
        """test if beverage list view returns correct render template"""

        # arrange
        def my_method():
            beverages = db_session.query(Beverage).all()
            status = request.form.get("status")
            return render_template(
                "beverage/beverage_list.html",
                beverages=beverages,
                status=status,
            )

        # Act

        # Assert
        self.assertEqual(beverage_list_view(), my_method())
