# Online-Auctions
Description: An online auction management system is a web-based platform that allows users to create, manage and participate in online auctions. 

Intended User: This system is intended for auction organizers, sellers and buyers who want to participate in online auctions. 

Scope: The system allows auction organizers to create and manage auctions, manage bidders and auction items, 
set bidding rules(starting price), monitor bidding activities, and close auctions. 
Buyers can browse auction items, place bids,add to their watch list and track their bidding activities. 
Sellers can list items for auction, monitor bidding activities and receive payment upon the conclusion of the auction. 

Features: 
1. User management - Register/login or Login Using Social Accounts like Facebook, Twitter , and GitHub.
2. Auction creation - auction organizers can create new auctions with a description, start time and other relevant details. 
3. Bidding - Buyers can place bids on auction items and view their bidding history.
4. Item management - Organizers and sellers can add/delete items to an auction.
5. Bid management - Organizers can monitor bidding activities, set minimum bids and reserve prices. 
6. Payment processing - The system integrates with payment gateways to securely process payments.
7. Reporting - generate reports on auction activities, item sales and buyer/seller information in Telegram .
8. Bid winners - The system will identify the winner when an item listing is closed

Requirements: 
1. Python and Django framework installed on the server.
2. A payment gateway integration (e.g. PayPal, Yenepay).
3. A database to store information about auctions, bidders, and items (sqlite3).

- The crucial files are:
  - 'manage.py' : the python file required to run the website
  - 'db.sqlite3': the website uses `sqlite3` database which stores the data in this file
- The 'auctions' directory has the files for the auction application which includes:
  - 'views.py': server side code for the website
  - 'urls.py': the urls that determine which associates url extensions to the views from `views.py` file
  - 'models.py': the tables needed for the 'sqlite3' database
  - 'decorators.py': functions that add a layer of security concerning logged-in and logged-out users
  - 'admin.py': adds the database tables to be modified in the django admin interface
  - 'forms.py': to create forms for easier access of `POST` data from the `HTML` forms
  - 'templates' directory: consists of all the `HTML` files to be rendered
  - 'static' directory: consists of files such as `CSS` and images used in the web page
  - 'uploads' directory: consists of images from the ImageField in the database table
- The 'commerce' directory has the files for crucial for the functions of the auction application which includes:
  - 'settings.py': consists of all the settings for the whole web application
  - 'urls.py': the main urls file with the urls from all the apps in the web application (such as auctions)
- The 'images' directory holds many pictures that show you the look of the website

