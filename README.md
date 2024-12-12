# Assignment 6 - Web Application to Manage Beverages

## Author
Walter Podewil
CIS 226
November 23, 2024


## Description

You are to create a web application using Flask and SQLAlchemy to manage a beverage database.
The application should have the following pages and navigation:

* A Home page. Does not have to be fancy.
* A Contact page. Does not have to be fancy.
* A Beverage List page.
* A Beverage Add page.
* A Beverage Update page.
* A Beverage Delete page.

Every template must use a Base template file for the things that do not change.
The entire project should use Bootstrap to improve the overall styling of the site.

The Home page should have a nice welcome page that helps a new user figure out how to use the site without being overly detailed. This will more or less be a static page. You may want to look at some Bootstrap examples (linked below) to see what sorts of things you could do to make a decent looking page with minimal effort.

The Contact Page should provide a way for users of the site to contact you if they have questions or concerns about the site. This can be made up information. This will also be more or less be a static page.

The Beverage List and related pages is where the main focus of the site should be.

The Beverage List page should list all of the beverages stored in a copy of the same database as what was used for assignment 5. I have included a copy of the database in this repository. Normally databases should not be tracked by Git. But, for the sake of ensuring that you all have access to the database I have included it.

In addition to the page displaying the list of beverages, there should be links (buttons) for each beverage that allows the user to update or delete a specific item from the list. This will require the creation of additional pages to implement that functionality. There should also be a way to create a new beverage and add it to the database. This will require yet another page to implement the functionality.

When creating a new beverage, the user must be able to enter in the id for the beverage. When updating a beverage,
the user should NOT enter in the id. Since the id is a primary key, users should be unable to change that. This differs slightly from what we did in the In-Class work. If you need help or have questions, ask.

The list of updatable fields are as follows:
* Description
* Pack
* Price
* Active

The project should have good file structure. This mean that the Beverage model should be in a Python module specifically for models / the beverage. All views should be in a Python module specifically for views. All templates should be in a templates folder and structured cleanly inside of there. All static files should be in a static folder. Assuming you followed along with the In-Class work, this shouldn't be too hard to do.

**BE SURE TO DUMP YOUR REQUIREMENTS.TXT FILE!**<br>
If you do not dump, add, commit and otherwise include it with your submission, I will not grade it.

### Solution Requirements:

* 2 Static pages: Home, Contact
* 4 CRUD pages: Beverage List, Beverage Add, Beverage Update, and Beverage Delete
* Use of Bootstrap
* Base Template page
* Model class for the Beverage
* View methods and Routes are separated into different Python modules
* List all functionality
* Insert functionality
* Update functionality
* Delete functionality

### Extra Credit
You can get up to 40 assignment points of extra credit by adding additional functionality (Max 8 points per feature). If you attempt any of this extra credit, be sure to add a section to this README stating what Extra Credit you are attempting. Otherwise, I may not know to look for it. The extra credit can be obtained by adding the following features:

* Validate all information that is submitted to ensure it is valid. This includes Insert and Update of Beverages.
    1. I looked at this one.  ID, Name, and Price should be easy to validate as the first two are just strings and the last is a float.  Active is a radio button and validation is inherent.  As a matter of fact, unless there are further guidelines concerning ID and Name, they can be strings of any value.
    2. Unfortunantly, validating Pack will entail too much scope creep.  I would have to:
        1. Figure out what all the different pack values mean
        2. Create a Regex for every possible combination of units, package size, package quantity
        3. OR modify the Beverage model's pack attribute to be more granular with sub-attributes
            1. Modify the Add and Edit views to account for new sub-attributes
    3. But, I could do a simple pack validation by checking for at least one integer(quantity) and at least one string(unit)
        1. Nope.  Not all existing beverages have a Pack of quantity and unit that can be split into two strings.  I will abandon this one for scope creep.  I would need to sanitize the existing database first.
    4. At this point, the only input I will validate is Price and maybe a simple Pack validation to avoid scope creep.
    5. I enabled Price validation with one caveat: my validator assumes that floats of any length can be entered, beyond dollars and cents.  While this allows for users to input seemingly illogical prices (49.00000304 for example), this is not a fault.  Look at gas prices per gallon: they often involve numbers smaller than 1 cent.  Beverages could POTENTIALLY involve numbers smaller than one cent.  While unusual, I will rely on the user to make that determination.  The user's business logic may require more price granularity.
        1. I could change the Beverage model to include a get_price() method that returns the self.price formatted to two decimal places .2f but I think this would confuse users if they don't know the actual price is more granular.  get_price() would change a self.price of 49.009 and return 49.00 or 49.01 depending on my rounding.
    6. EDIT: ID must be validated.  All of the initial IDs are of length 6 and only contain letters and 0-9.
    7. As of 12/11/2024, ID and Price are explicitly validated via utility methods.  Active is implicitly validated via radio buttons.  Name is implicitly validated by checking for existence of a string.
* Use JavaScript / jQuery to handle getting to the edit page of a item in the list by setting a click listener on the table row for the item. (This would replace the edit link from scaffolding)
    1. I put a click listener into the base.html and it works EXCEPT that it also reacts to clicking on the header row.
* Use JavaScript / jQuery to pop up a confirmation delete message when deleting a beverage. (I realize that there is already a delete check via a whole page, but I want a JS one in addition to that for the Extra Credit)
    1. pasted copied script into beverage_delete.html, doesn't work as of 12/11/2024
* Ability to click on a table header and sort the list of items by that column. You must do at least 2 column headings.
    1. I attempted this one.  I can sort by the headers, albeit not in place, but by rendering a new view.  Now, I tried adding the radio buttons for Active, Inactive, All, but I can't get the table to show up.  The only button I tried the Active, Inactive, All radio button filtering on is sorting Price by Ascending order.  The other header buttons sort as they should.
    2. I commented out the status checker on Price sort in Ascending order, so it sorts as normal.
    3. Active, Inactive, All radio buttons are non functional
* Write at least 2 unit tests to verify some part of your code.
    1. 12/11/2024: started unit tests by making tests directory and test_beverage_view.py
    2. I'm not sure how to test view methods.  They return render_template.
        1. I attempted to test a view by making my own method that returns a render_template and then assertingequal the view method vs my method
        2. pytest throws a runtime error
        3. On second thought, these are integration tests and beyond the scope
    3. I think I can write unit tests for the model Beverage
    4.

### Notes

The following Bootstrap documentation should help you figure out how to add some simple styling to your project if interested. In addition, you may be able to find an entire Bootstrap theme that you could include to really make it look good.
[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

The following Bootstrap examples should help you see some thing that you can do in your own site if desired. Since they are part of the Bootstrap documentation, it is okay (and encouraged) that you take code directly from it. Again, since this is part of the documentation, it is free from Plagiarism. Examples taken from anywhere else on the internet must be properly listed in the outside resources section.
[Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)

I may not have had time to demonstrate checkboxes in the in-class material. Because of that, you may find some useful information in the following link that explains how to use them. More than likely you will want to use them for the `Active` field. Additionally, if you are stuck, don't hesitate to ask questions and have me look at your project.
[HTML Checkboxes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)

## Grading
| Feature                                 | Points |
|-----------------------------------------|--------|
| Home and Contact Pages                  | 10     |
| CRUD Pages                              | 20     |
| Bootstrap                               | 10     |
| Base Template                           | 10     |
| Beverage Model                          | 10     |
| View methods and Routes separated       | 10     |
| List All Functionality                  | 5      |
| Insert Functionality                    | 5      |
| Update Functionality                    | 5      |
| Delete Functionality                    | 5      |
| Documentation                           | 5      |
| README                                  | 5      |
| **Total**                               | **100**|

## Outside Resources Used
1. https://werkzeug.palletsprojects.com/en/stable/
    * used to diagnose to_url() ValueError
2. https://stackoverflow.com/questions/31859903/get-the-value-of-a-checkbox-in-flask
    * how to get radiobox value
3. https://stackoverflow.com/questions/19614027/jinja2-template-variable-if-none-object-set-a-default-value
    * how to test for None/null in jinja (use none)
4. https://stackoverflow.com/questions/20134651/does-jinja2-support-nested-if-statements
    * jinja2 nested if statements
5. https://www.w3schools.com/howto/howto_js_sort_table.asp#:~:text=Sort%20Table%20by%20Clicking%20the,ascending%20(A%20to%20Z).
    * try to sort by table header
6. https://gist.github.com/gibtang/83f9681b525908900ec4b490992f032d
    * sort using sorted() method plus lambda function
7. https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_event_click
    * jquery click listener
8. https://stackoverflow.com/questions/43099296/best-method-for-dynamically-building-url-with-flask-url-for
    * use flask url_for() inside jquery click listener
9. https://craftpip.github.io/jquery-confirm/
    * jquery confirm method popup
10. https://circleci.com/blog/testing-flask-framework-with-pytest/
    * how to use pytest on flask

## Known Problems, Issues, And/Or Errors in the Program
1. 12/05/24 TypeError when using the Active field.  True/False and 0/1 do not work as bools.
    * Need to figure out how to convert input to bool
    * or use radio buttons (checkboxes) and convert to bool
    * NOTE: Fixed it.  change checkbox input values to 1 or true for Active, and empty string for inactive
        cast to bool when updating beverage in database

2. 12/06/24: All of the beverages in the database are set to Active: False
    * I don't remember if the database came this way, or if I screwed something up

3. https://api.beverage.barnesbrothers.net/beverages

4. 12/11/24 Filtering table by Active (true, false) using radio buttons not working.
    * Currently, you can sort the table by all headers except for Price Ascending because I am trying to work out how to simultaneously filter the table by Active using radio buttons.  Price ascending is the "test button" for the moment

5. 12/11/24 outsource sort method to utils class
    * I tried making a utils class that houses the sorting methods until I realized that each beverage attribute would have to have a method for both ascending and descending order.  I did some research and there is a lambda function I could pass, but that is beyond the scope of this project

6. 12/11/24 jquery click listener on header
    * jquery click listener responds to clicking on table header when it should only be rows

7. 12/11/24 jquery confirm delete script
    * jquery confirm script in beverage_delete.html doesn't work

8. 12/11/24
    * After messing around with the table in attempt to add more functionality, the rows are no longer striped.  In beverage_list.html, <table class="table table-striped"> should make it striped.
