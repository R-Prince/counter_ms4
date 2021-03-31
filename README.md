# Counter

An online bookkeeping service that allows users to record and track payments such as invoices and bills. Like the name suggests Counter will help you keep count of your finances and track money coming in and out of your business.

Whether the user is a Freelance, Sole-Trader or Small Business they will be able to easily keep track of payments and ensure they never miss one!

[Counter](https://counter-ms4.herokuapp.com/)

Business goals: 
- Provide users with a simple platform to record invoices and bills
- Earn income from users subscribing to the site.
- Provide information on overdue invoices and bills so users do not miss a payment

User goals:
- Easily track invoices and bills issued by customers
- Easily find information on what current bills and invoices are outstanding. 
- Find information on customers such as email and phone number to contatc regarding overdue payments

# Table of Contents
1. [UX](#UX)
2. [Features](#Features)
3. [Features Left to Implement](#Features-left-to-Implement)
4. [Information Architecture](#Information-Architecture)
5. [Technologies Used](#Technologies-Used)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
8. [Heroku Deployment](#Heroku-Deployment)
9. [Credits](#Credits)

# UX

#### Ideal Client

The ideal client for this business is: 
- Someone who has their own business.
- Over 18 years old.
- Handle the day to day finances of a company. 
- An accountant who needs to track invoices. 
- Someone who needs to track and chase payments.

Visitors to this website are searching for: 
- A service that can help them easily track the money going in and out their business.
- A platform to easily create invocies and bills. 
- A platform to view when payments are due to be paid.
- Easy to keep track of payments and ensure they are paid on time.

This website helps users achieve this goal by:
- Providing a simple platform for user to keep track of payments.
- Easy fillabel forms so users can create invoices and bills.
- Provide simple and clear information on if payments have been made or when they are due.
- Simple digestable chunks of data so users can find information on customers.

### Clients stories
1. As a subscribed user, I want to easily be able to view information on what bills/invoices i currently have outstanding and what has been paid.
2. As a subscribed user, I want to easily be able to create bills and invoices for customers. 
3. As a subscribed user, I want to easily be able to create customers and update information when needed. 
4. As a subscribed user, I want to easily be able to track bills and invoices for each customer I do business with.  
5. As a new visitor to the website, I want to make sure this service is right for me before I buy. 

### Wireframes
These wirerames were created using [Figma](https://www.figma.com/) during the planning process for the project and includes wireframes for desktop, tablets and mobile devices.

[Counter Wireframes](/readme/wireframes/counter.pdf)

# Features

### Navigation Bar 
The navigation bar includes the Counter logo in the top left corner. 

- For visitors that are not logged in, the below links are available:
    1. Features
    2. Prices
    3. Contact Us 
    4. Login
    5. Try for Free (cta)


- For users that are logged in, the below links are available:
    1. Features
    2. Prices
    3. Contact Us 
    4. Login
    5. Profile (link to user profile)

The navigation bar will display the different links depending on if the “user” is in session.

The navbar collapses into a hamburger icon on the top right corner on tablet and mobile devices. The mobile nav displays the same information as the desktop navbar.

## Homepage

Hero Section:

The hero section includes a backgroung image. In front of the image is the name of the site and a tagline for the website. Directly underneath is a call to action button “Try for Free” which directs the users to a page to create an account.

Feature Section:

The feature section includes the 3 main benefits of the platform and is used so that the user can recieve clear information on what the service has to offer and if it's right for them.

On large and medium screens the features are display in one row but on smaller devices each feature is stacked and has it’s own row.

Price Section:

The section displays how much the service is going to cost and how long the durations of the service lasts. £19.99 for 31 days access to the platform. 

Contact Us Section:

This section details how to get in contact with Counter if you have any questions. This includes email address, phone number and office address. 

Footer Section:

This includes links to Counters social media accounts including Facebook, Twitter and LinkedIn. 

## Profiles App
This app is used to create, edit and store information about the users profile.

### Profile Template
This template is effectively the dashboard and includes specific information about the users profile such as current overdue invoices and bills. This give the user clear information about the invoices customers owe and what the currently owe customers. These are both display in responsive tables and include table headers such Customer account, bill/invoice date, due date, total amount and if the bill/invoice has been paid or not. It also features 3 call to action buttons along the side so users can quickly create an Invoice, Bill or Customer.

### Profile Info Template
This template renders a cripsy form which includes information on the users profile which they used to create their profile originally. This template allows them to edit and update information on their account such as contact details.

### Create Profile Template
This template renders a crispy form for the user to create their own profile.

## Customers App

### Customers
This template simply renders the users customers they have created. The data on each customer is shown in a responsive table which details information such as company name, contact name and contact information. 

### Create Customer 
This template renders a crispy form which is used to a create a new customer for a user. This includes fields such as company name, contact name and contact information.

### Edit Customer
This template renders a crispy form with information on the customer they have selected. Users are able to edit and update information on the customer and save to their profile. 

### Customer Account
This template renders data in the form of a responsive table detailing any invoices and bills related to the selected customer. Both tables include information such as due date, status of whether the payment has been made or not as well as the total amount. 

## Invoice App

### Create Invoice 
This template includes a cripsy form rendered as a table detailing fields needed to create an informative invoice and attach to a selected customer. It also includes "item lines" where users can create products/services describing what they are selling. This icludes jquery to manipulate the DOM and add more item lines or delete item lines. Once the user has field out the required input fields the invoice is saved to the db.

### Edit Invoice 
This template renders a crispy form detailing information on the selected invoice. User can then edit certain fields on the invoice such the invoice date, due date and payment status. This template view also includes a delete button which would delete the invoice from the users account and db. 

## Bill App

### Create Bill 
This template includes a cripsy form rendered as a table detailing fields needed to create an informative bill and attach to a selected customer. It also includes "item lines" where users can create products/services describing what they are selling. This icludes jquery to manipulate the DOM and add more item lines or delete item lines. Once the user has field out the required input fields the bill is saved to the db.

### Edit Bill 
This template renders a crispy form detailing information on the selected bill. User can then edit certain fields on the bill such the bill date, due date and payment status. This template view also includes a delete button which would delete the bill from the users account and db. 

## Subscription

### Update Subscription
This template uses stripe to take payments and is used to update the users subscription. When a user first creates an account they instantly recieve a 14 day free trial to see if they like the service. Once this has ended they will not be able to access their account and will need to pay a fee of £19.99 to regain access to thier profile. Using Stripe this template allows user to make a payment using a credit card to gain access to the site for the next 31 days. 

### Checkout Success
The template simply features a success message to let the user know their payment was successfull and gives them a link back to their profile page. 

## Allauth Templates
Allauth templates were used throughout the site to handle creating a user,  logging in and out as well as handling forgotten passwords, email verifications ect. 

# Features left to Implement

1. Search Bar - Add a search bar to allow users to search the database for invoice, bills and customers.
2. Email notification for overdue invoices and bills - User recieve a notification via email if a bill or invoice falls overdue.
3. Invoice/Bill total - Enable users to see the grand total of an invoice or bill when creating a payment.  
4. Display data regarding bills, invoice and customers to users on the profile page in the form of graphs and bar charts so users can gain a wider view on the performance of the business. 

# Technologies Used 

### Tools 

- [Gitpod](https://www.gitpod.io/) - IDE used to develop this project.
- [Github](https://github.com/) - Store and share all project code remotely.
- [PIP](https://pypi.org/project/pip/) - Used to install tools needed for this project.
- [Stripe](https://stripe.com/en-gb) - Used to process credit card payments
- [Amazon AWS](https://s3.console.aws.amazon.com/s3/buckets/counter-ms4?region=eu-west-2&tab=objects) - Used to store static and media files.
- [PostgreSQL](https://www.postgresql.org/) - Used for the production db.
- [SQLite3](https://www.sqlite.org/index.html) - Used for the development db.
- [JQuery](https://jquery.com/) - Used for DOM manipulation. 
- [Bootstrap](https://getbootstrap.com/) - Used to create the structure and UI for the website and make the website responsive.
- [Font Awesome](https://fontawesome.com/) - Used to provide icons for the website. 
- [Google Fonts](https://fonts.google.com/) - Used to style the website fonts. 
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - Used to handle an integrated set of Django applications addressing authentication, registration and account management.
- [Django](https://www.djangoproject.com/)  - Used to construct, build and render pages. 
- [Django Crispy Forms](https://www.djangoproject.com/)  - Application to help to manage and render Django forms.
- [Heroku](https://www.heroku.com/what)  - Cloud platform used to host the website.

### Languages
This project uses HTML, CSS, Javascript and Python to programme the website. 

# Testing
Testing information can be found in a seperate [Testing](readme/testing/testing.md) file.

# Deployment

## Heroku

To deploy the site on Heroku, please see below steps:

1. Install gunicorn, psycopg2-binary and dj-database-url using PIP3.
2. Create a requirements.txt and freeze the required modules
3. Created a Procfile and add "web: gunicorn counter.wsgi:application". 
4. Then in the command line  
git add, git commit and git push to make these changes to your GitHub repository.
5. Log into your Heroku account and created a new app.
Go to the Resource tab in Heroku and add Heroku Postgres.
6. In the new Heroku app under settings add to the Reveal Config File:

| KEY | VALUE |
| ------|-----------|
| AWS_ACCESS_KEY_ID| VALUE|
| AWS_SECRET_ACCESS_KEY| VALUE|
| DATABASE_URL | VALUE |
| EMAIL_HOST_PASS | VALUE| 
| EMAIL_HOST_USER| VALUE|
| SECRET_KEY| VALUE|
| STRIPE_PUBLIC_KEY	 | VALUE |
| STRIPE_SECRET_KEY | VALUE |
| STRIPE_WH_SECRET	| VALUE| 
| USE_AWS | VALUE |

7. Add your new PostgreSQL link to your database in settings.py 
8. Make your migrations in the terminal in order to migrate the database models to the Postgres database and load the data.
9. Remember to add heroku config:set DISABLE_COLLECTSTATIC=1 into the terminal so that Heroku doesn't collect the static data.
10. Add heroku app to the allowed hosts in your settings.py
11. In Stripe, added the Heroku app udpate subscription URL as a new webhook.
12. Updated the settings.py with the new Stripe environment variables and email settings.

# Credit 

### Media
- All images for the site were obtained from [Unsplash](https://unsplash.com/).

# Acknowledgement
- I received inspiration for this project from a number of different websites:
    - [Xero](https://www.xero.com/uk/)
    - [QuickBooks](https://quickbooks.intuit.com/uk/oa/?ds_rl=1263531&cid=ppc_G_QB_UK_GGL_B_Quickbooks_Core_Exact_Search_ALL_quickbooks_txt&ds_rl=1263531&gclid=CjwKCAjwu5CDBhB9EiwA0w6sLS0cZbnNCNwDQFvEn-i_CLx3eRA0_uuLdm7tG7h_KHR4BwVZ1Xnp5RoCJDQQAvD_BwE&gclsrc=aw.ds)
