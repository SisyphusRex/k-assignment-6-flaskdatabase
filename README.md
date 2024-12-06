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
* Use JavaScript / jQuery to handle getting to the edit page of a item in the list by setting a click listener on the table row for the item. (This would replace the edit link from scaffolding)
* Use JavaScript / jQuery to pop up a confirmation delete message when deleting a beverage. (I realize that there is already a delete check via a whole page, but I want a JS one in addition to that for the Extra Credit)
* Ability to click on a table header and sort the list of items by that column. You must do at least 2 column headings.
* Write at least 2 unit tests to verify some part of your code.

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


## Known Problems, Issues, And/Or Errors in the Program
1. TypeError when using the Active field.  True/False and 0/1 do not work as bools.
    * Need to figure out how to convert input to bool
    * or use radio buttons (checkboxes) and convert to bool

