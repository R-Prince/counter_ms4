# Testing

Back to [README](/README.md) file.

[Counter](https://counter-ms4.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#Automated-Testing)
2. [User Stories Testing](#User-Stories-Testing)
3. [Manual Testing](#Manual-Testing)
4. [Further Testing](#Further-Testing)

# Automated Testing 
- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML. 
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate the Javascript. Please see below main errors:
    - 3 warning which mostly consisted of missing semi-colons.


# User Stories Testing 

#### Client Stories

The following section goes through the user stories from the UX section of the readme. 

1. As a subscribed user, I want to easily be able to view information on what bills/invoices i currently have outstanding and what has been paid.
    1. Once users have logged in and created a profile. They are directed to a dashboard which deatils the information of this user story. The dashboard provides two table. One for invoice and one for bills - These detail any payment which haven't been made so users can easily identified payments they still need to make and by what date. 
2. As a subscribed user, I want to easily be able to create bills and invoices for customers. 
    1. Once on their dashboard there are two call to action buttons that allow users quick and easy access to creating either a bill or an invoice.
    2. With the help of crispy forms creating an invoice and bill is super easy and can be done with only a few clicks. 
3. As a subscribed user, I want to easily be able to create customers and update information when needed.
    1. Users can easily create new customers via the call to action button on the dashboard.
    2. With the help of crispy forms users can easily created customers following the simple form instructions and placeholders. 
    3. Users can easily update/edit and delete customers by simply clicking and viewing the customer they would like to perfrom the action on.
4. As a subscribed user, I want to easily be able to track bills and invoices for each customer I do business with.
    1. Users can easily keep track of bills and invoices for customers by simply navigating to the customer account page. Here invoices and bills are displayed in a form of a responsive table which is easy to read and digest. 
5. As a new visitor to the website, I want to make sure this service is right for me before I buy. 
    1. Each user when they sign up and create a profilel instanly recieve a 14-day free trial to use the platform and decide if the service is appropiate for there business needs. 

# Manual Testing 

## Profile App 
1. Successfully create a new user profile without any issues or errors.
    - Added more padding to the submit button for better UX experience.

2. Successfully edit a profile and update information without any issues.
3. Successfully navigate to the settings page with no issues so users can view and edit current profile. 

## Customer App
1. Successfully create new customers in database linked to the logged in user. 
2. Successfully edit and update customer information without no errors.
3. Successfully delete customer from user profile
    - Issue: as a foreign key was not used with user profile - Bills and Inovices related to the customer were still showing in the bills and invoice app. 

## Invoice App 
1. Successfully create a new invoice attached to a user profile and customer.
2. Invoice item lines successfully calculated and added to the relevant Invoice via foreign key.
3. Successfully edit/delete invoices in the database. 
4. Succesfully render the correct information in templated and views. 

## Bill App 
1. Successfully create a new bill attached to a user profile and customer.
2. Bill item lines successfully calculated and added to the relevant Bill via foreign key.
3. Successfully edit/delete Bills in the database. 
4. Succesfully render the correct information in templated and views. 

# Further Testing 

- Asked friends and family to test website on their own devices and report any errors.
- I viewed my website on several devices to check for any errors.
- I viewed website on Safari, Firefox and Chrome to check for any errors.
- I was planning on doing some django unit testing to test the apps, view, forms and models but sadly ran out of time. 