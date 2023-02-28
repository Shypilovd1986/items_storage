# Item storage

“Item storage” is web-application that allows users to record information about items, goods or other murchandise which store on warehouse.

Application should provide:
* Storing items and brands in a database;
* Display list of items with their characteristics;
* Updating the list of items (adding, editing, removing);
* Display list of brands;
* Updating the list of brands (adding, editing, removing);
* Finding item by date that it was produced ;
* Finding item by name.

## 1. List of items
## 1.1 Display list of items
The mode is designed to view the list of items in database with it's name and identifier.
### Main scenario:
* User selects "list of items;
* Application displays list of items wrote in database.

The "list of items" displays the following columns:
* number – serial number in database;
* id – unique item identifier, primary key in database;
* name - name of item.

<image src="html_prototype/static/images/list_of_items.png" alt="list of items" height="500" align="center">.
##### Pic. 1.1 View "list of items".


## 2. List of brands
## 2.1 Display list of brands
The mode is designed to view the list of brands in database with it's name and number.
### Main scenario:
* User selects "list of brands;
* Application displays list of brands wrote in database.

The "list of brands" displays the following columns:
* number – serial number in database, primary key in database;
* brand's name - name of brand.

<image src="html_prototype/static/images/list_of_brands.png" alt="list of brands" height="300">.
##### Pic. 2.1 View "list of brands".

## 3. Details of items
## 3.1 Display details of items
The mode is designed to view the details of items. To add, edit and delete item.
### Main scenario:
* User selects "details of items";
* Application displays details of all items.

The "details of items" displays the following columns:
* id – unique identifier of item, primary key in database;
* name - name of item;
* colour - colour of item;
* price - price of item;
* brand - brand of item;
* date - date of production of item.

<image src="html_prototype/static/images/details of items.png" alt="details of items" height="600">.
##### Pic. 3.1 View "details of items".

Finding by name or by date of production.

* In order to find item by name, the user fill in field 'searching item by name' and press button 'search'. 
The application will display items which match the name filled in field.
* Also user can find item by date of production. 

## 3.2 Add item

### Main scenario:

* User clicks the “add item” button in order to open form for adding item to database;
* Application displays form to enter order data;
* User fills data in fields and presses “Add” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, data will be added to database;
* If error occurs, then error message is displaying;
* If new data is successfully added, then list of items with added data is displaying.


<image src="html_prototype/static/images/add_item.png" alt="adding item" height="700">.
##### Pic. 3.2 View "adding item".

Cancel operation scenario:

If user doesn't want to add item, he just can select one of 4 link in main menu and go there.

When user adding an item, he must fill the data:
* id – unique identifier of item;
* name – name of item;
* colour, price, brand, date of production – characteristics of items;
* press button 'Add'.

## 3.3 Edit item.
### Main scenario:
* User clicks the “edit” button in order to open edit form;
* Application displays form like adding new item;
* User enters required data and presses “save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is saved to database;
* If error occurs, then error message is displaying;
* If record is successfully edited, then list of item with added records is displaying.

Cancel operation scenario:
* User clicks the “edit” button in details of items view mode;
* Application displays form to enter required data;
* If user doesn't want to add item, he just can select one of 4 link in main menu and go there.
* Data don’t save in database, then list of items is displaying to user.

<image src="html_prototype/static/images/editing_item.png" alt="editing item" height="700">.
##### Pic. 3.3 View "editing item".
When editing an item, the following details are entered:
* id – unique identifier of item, primary key in database;
* name - name of item;
* colour - colour of item;
* price - price of item;
* brand - brand of item;
* date - date of production of item.

Constraints for data validation:
* id – maximum length of 10 characters;
* name – maximum length of 15 characters;
* color, brand – maximum length of 10 characters;
* price – maximum length of 8 characters;
* date – date in format dd/mm/yyyy.

## 3.4 Deleting item
### Main scenario:
* The user, while in 'details of item', presses the "delete" button in the selected item line;
* The user confirms the deleting of the item;
* Item is deleted from database;
* If error occurs, then error message displays;
* If item is successfully deleted, then list of items without deleted records is displaying.

<image src="html_prototype/static/images/delete_item.png" alt="delete item" height="300">.
#### Pic. 3.4 View 'Delete item'.
Cancel operation scenario:
* Application displays confirmation dialog “Do you really want to delete item?”;
* User press “Cancel” button if he wants to cancel deletion item;
* List of brands without changes is displaying.

## 4. Details of brands
## 4.1 Display details of brands
The mode is designed to view the details of brands. To add, edit and delete brands.
### Main scenario:
* User selects "details of brands";
* Application displays details of all brands.

The "details of brands" displays the following columns:
* brand's id – serial number in database, primary key in database;
* brand's name - name of brand;
* country of origin - country where this brand was invented;

<image src="html_prototype/static/images/details_brands.png" alt="details of brands" height="600">.
##### Pic. 4.1 View "details of brands".

## 4.2 Add brand

### Main scenario:

* User clicks the “add brand” button in order to open form for adding brand to database;
* Application displays form to enter order data;
* User fills data in fields and presses “Add” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, data will be added to database;
* If error occurs, then error message is displaying;
* If new data is successfully added, then list of brands with added data is displaying.


<image src="html_prototype/static/images/adding_brands.png" alt="adding brand" height="500">.
##### Pic. 4.2 View "adding brands".

Cancel operation scenario:

If user doesn't want to add brand, he just can select one of 4 link in main menu and go there.

When user adding brand, he must fill the data:
* brand's id – serial number in database, primary key in database;
* brand's name - name of brand;
* country of origin - country where this brand was invented;
* press button 'Add'.

## 4.3 Edit brand.
### Main scenario:
* User clicks the “edit” button in order to open edit form;
* Application displays form like adding new brand;
* User enters required data and presses “save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is saved to database;
* If error occurs, then error message is displaying;
* If record is successfully edited, then list of brands with added records is displaying.

Cancel operation scenario:
* User clicks the “edit” button in details of brands view mode;
* Application displays form to enter required data;
* If user doesn't want to add brand, he just can select one of 4 link in main menu and go there.
* Data don’t save in database.

<image src="html_prototype/static/images/editing_brand.png" alt="editing item" height="400">.
##### Pic. 4.3 View "editing brand".
When editing brand, the following details are entered:
* brand's id – serial number in database, primary key in database;
* brand's name - name of brand;
* country of origin - country where this brand was invented;

Constraints for data validation:
* brand's id  – maximum length of 10 characters;
* brand's name – maximum length of 15 characters;
* country of origin – maximum length of 15 characters;


## 4.4 Deleting brand
### Main scenario:
* The user, while in 'details of brand', presses the "delete" button in the selected item line;
* The user confirms the deleting of the brand;
* Brand is deleted from database;
* If error occurs, then error message displays;
* If brand is successfully deleted, then list of brands without deleted records is displaying.

<image src="html_prototype/static/images/delete_brand.png" alt="delete brand" height="300">.
#### Pic. 4.4 View 'Delete brand'.
Cancel operation scenario:
* Application displays confirmation dialog “Do you really want to delete brand?”;
* User press “Cancel” button if he wants to cancel deletion brand;
* List of brands without changes is displaying.