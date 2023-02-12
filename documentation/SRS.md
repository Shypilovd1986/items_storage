# Item storage

“Item storage” is web-application that allows users to record information about items, goods or other murchandise which store on warehouse.

Application should provide:
* Storing categories, items and brands in a database;
* Display list of categories and quantity of items that store on warehouse;
* Updating the list of category (adding, editing, removing);
* Display list of items with their characteristics;
* Updating the list of items (adding, editing, removing);
* Display list of brands;
* Updating the list of brands (adding, editing, removing);
* Display number of the orders for cars and clients;
* Filtering by date that items was produced ;
* Filtering by price of the items.

## 1. Category
## 1.1 Display list of category
The mode is designed to view the list of category, if it possible to display the number of items for a specified period of time.
### Main scenario:
* User selects item “Category”;
* Application displays list of Categories.

The list displays the following columns:
* Category number – unique category number;
 Client passport number – unique client passport number;
 Add date – date of adding a rental order;
 Rental time – rental time in days, minimal time is one day;
 Car rental cost – cost of car rental for one day;
 Total cost – total cost of car rental, total cost is calculated as the rental time multiplied by car rental
 cost.
Aggregate function: Total cost = Rental time * Car rental cost.
Filtering by date:
 In the order list view mode, the user sets a date filter and presses the refresh list button (to the right of the date entry field);
 The application will display a form to view the list of orders with updated data.
