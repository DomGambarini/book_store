# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Validation](#javascript-validation)
    - [CSS Testing](#css-testing)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsiveness Test](#responsiveness-test)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)


## Code Validation

[Back to top](#testing)
### HTML Testing

I used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

![html validation](./test-images/html-validator-no-errors.png)

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| All Books (including filtering and sorting) | 0 | 0 |
| Book Detail | 0 | 0 |
| Register | 0 | 0 |
| Log In | 0 | 0 |
| Logout| 0 | 0 |
| Profile | 0 | 0 |
| Product Management | 0 | 0 |
| Edit Product | 0 | 0 |
| Our Team | 0 | 0 |
| Team Management | 0 | 0 |
| Edit Team | 0 | 0 |
| Our Events | 0 | 0 |
| Event Management | 0 | 0 |
| Edit Event | 0 | 0 |
| Order History | 0 | 0 |
| Bag - Empty | 0 | 0 |
| Bag - Products | 0 | 0 |
| Checkout | 0 | 0 |
| Admin Panel (including all categories and templates) | 0 | ![html validation](./test-images/html-validator-warning-admin-panel.png) |
| Get in Touch | 0 | 0 |


### Python Testing
[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files.


| Feature               | admin                                       | forms                                       | models                                      | urls                                        | views                                       | extra                                      |
|-----------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|--------------------------------------------|
| Bag                   | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/bag-urls.py.png) | none ![python validation](./test-images/bag-views.py.png) | n/a |
| Checkout              | none ![python validation](./test-images/checkout-admin.py.png) | none ![python validation](./test-images/checkout-forms.py.png) | none ![python validation](./test-images/checkout-models.py.png) | none ![python validation](./test-images/checkout-urls.py.png) | none ![python validation](./test-images/checkout-views.py.png) | none ![python validation](./test-images/checkout-signals.py.png), none ![python validation](./test-images/checkout-webhook-handler.py.png), none ![python validation](./test-images/checkout-webhook.py.png) |
| Contact               | n/a                                         | none ![python validation](./test-images/contact-forms.py.png) | n/a                                         | none ![python validation](./test-images/contact-urls.py.png) | none ![python validation](./test-images/contact-views.py.png) | n/a                                        |
| Events                | none ![python validation](./test-images/events-admin.py.png) | none ![python validation](./test-images/events-forms.py.png) | none ![python validation](./test-images/events-models.py.png) | none ![python validation](./test-images/events-urls.py.png) | none ![python validation](./test-images/events-views.py.png) | n/a                                        |
| Home                  | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/home-urls.py.png) | none ![python validation](./test-images/home-views.py.png) | n/a                                        |
| Indie Book Emporium  | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/indie-book-emporium-urls.py.png) | n/a                                         | ![python validation](./test-images/indie-book-emporium-settings.py.png) |
| Products              | none ![python validation](./test-images/product-admin.py.png) | none ![python validation](./test-images/product-forms.py.png) | none ![python validation](./test-images/product-models.py.png) | none ![python validation](./test-images/product-urls.py.png) | none ![python validation](./test-images/product-views.py.png) | none ![python validation](./test-images/product-widget.py.png) |
| Profile               | n/a                                         | none ![python validation](./test-images/profile-forms.py.png) | none ![python validation](./test-images/profile-models.py.png) | none ![python validation](./test-images/profile-urls.py.png) | none ![python validation](./test-images/profile-views.py.png) | n/a                                        |
| Team                  | none ![python validation](./test-images/team-admin.py.png) | none ![python validation](./test-images/team-forms.py.png) | none ![python validation](./test-images/team-models.py.png) | none ![python validation](./test-images/team-urls.py.png) | none ![python validation](./test-images/team-views.py.png) | n/a                                        |


[Back to top](#testing)

### JavaScript Validation

[JSHint](https://jshint.com/) was used to validate the JavaScript code.

| Page | Screenshot | Errors | Warnings |
|---------|----------|----------|-----------|
| Bag - Quantity Update/Remove Script | ![Bag update/remove js](./test-images/bag-update-remove.js.png) | none | none |
| Checkout - Stripe Script | ![Stripe elements](./test-images/checkout-stripe.js.png) | none | none |
| Products - Quantity Input Script | ![Product quantity script](./test-images/product-quantity-input-script.png) | none  | none |

[Back to top](#testing)
### CSS Testing
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS files.
Both base.css and checkout.css files passed. ![CSS Validation](./test-images/css-validator.png)

#### Browser Compatibility

- Safari 16.4.1
- Chrome 120.0.6099.199
- Firefox 122.0

#### Devices

- iPhone SE
- iPhone XR
- iPhone S2 Pro
- iPhone SE14 Pro Max
- Pixel 7
- Samsung Galaxy S8+
- Samsung Galaxy S20 Ultra
- Ipad Mini
- Ipad Pro
- Ipad Air
- Surface Pro 7
- Surface Duo
- Galaxy Fold
- Samsung Galaxy A51/71
- Nest Hub Max
- Nest Hub
- iPhone 4
- iPhone 6/7/8

## Fixed Bugs

1. Mismatched Checkout Forms: Initially, the checkout forms did not align with the order model, resulting in errors. Specifically, the form included a postcode field that was absent in the order class.
1. Category Model Misspelling: The category model encountered issues due to a misspelling in its implementation.
1. Event Form Image Rendering: The event form model failed to render images to the template. This occurred because although the form's enctype was set to multipart/form-data, I overlooked adding request.FILES in the view. Consequently, the absence of this caused a 200 response without highlighting the error.
1. Static Files Deployment Error: A deployment error arose when attempting to deploy static files to the AWS S3 bucket. This was traced back to a user not being created during the bucket creation process.
1. Heroku Deployment Issue: Deployment to Heroku faced obstacles due to a configuration error. The Heroku URL in the allowed hosts contained 'https://', which needed removal to function correctly.
1. Stripe Webhook Error: The Stripe webhook encountered a 400 HTTP error, stemming from incorrect email functionality setup for registration and order confirmation. Addressing this required updating the Python version to 3.11.9, along with configuring the runtime.txt file accordingly. Additionally, setting ACCOUNT_EMAIL_VERIFICATION to 'mandatory' resolved the error at the webhook endpoint and restored email functionality for the site.


### Results from Lighthouse
| Page | Validation Results |
| ---- | ---------- |
| Home | [Home Page Score](./test-images/lighthouse-homepage.png) |
| Get in Touch | [Get in Touch Us Score](./test-images/lighthouse-getintouch.png) |
| Get in Touch, Thank You | [Get in Touch Us Thank You Score](./test-images/lighthouse-thank-you.png) |
| Products | [Products Score](./test-images/lighthouse-all-products.png) |
| Product Detail | [Products Score](./test-images/lighthouse-product-detail.png) |
| Add Product | [Add Product](./test-images/lighthouse-add-product.png) |
| Edit Product | [Edit Product](./test-images/lighthouse-edit-product.png) |
| Event | [Event](./test-images/lighthouse-event-page.png) |
| Add Event | [Add Event](./test-images/lighthouse-add-event.png) |
| Edit Event | [Edit Event](./test-images/lighthouse-edit-event.png) |
| Team | [Team](./test-images/lighthouse-team-page.png) |
| Edit Team | [Edit Team](./test-images/lighthouse-edit-team.png) |
| Add Team | [Add Team](./test-images/lighthouse-add-event.png) |
| Admin Dashboard | [Admin Dashboard](./test-images/lighthouse-admin.png) |
| Shopping Bag | [Shopping Bag Score](./test-images/lighthouse-shopping-bag.png) |
| Checkout | [Checkout Score](./test-images/lighthouse-checkout.png) |
| Checkout Success | [Checkout Score](./test-images/lighthouse-checkout-success.png) |
| Profile | [Profile Score](./testing-images/lighthouse-my-profile.png) |
| Sign In | [Sign In Score](./test-images/lighthouse-sign-in.png) |
| Register | [Register](./test-images/lighthouse-register.png) |
| Sign Out | [Sign Out Score](./test-images/lighthouse-sign-out.png) |

## Manual Testing

### As a User Logged Out

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Top Nav menu user logged out | The free shipping treshold | It corresponds to the value set in the settings.py file. | Pass |
| Top Nav menu user logged out | Copy / paste url that requires authentification e.g. Product Management | Generates toast error pop up | Pass |
| Top Nav menu user logged out | Copy / paste url that requires authentification e.g. admin panel | Generates error pop up | Pass |
| Top Nav menu user logged out | Click search in search bar with no text entered  | Loads toast error | Pass |
| Top Nav menu user logged out | Click Account menu | Dropdown displays Register and login | Pass |
| Top Nav menu user logged out | Click Account / Login | Displays login page | Pass |
| Top Nav menu user logged out | Click Account / Register | Displays register page | Pass |
| Top Nav menu user logged out | Click Shopping bag icon | Displays empty bag page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Top Nav menu user logged out | Main navigation collapses into a hamburger on small screens | Displays hamburger icon | Pass |
| Top Nav menu user logged out | Click brand logo | Displays homepage | Pass |
| Top Nav menu user logged out | Click brand logo | Displays homepage | Pass |
| Top Nav menu user logged out | Home link displays in hamburger dropdown only | Displays home link in dropdown | Pass |
| Top Nav menu user logged out | Click home link | Displays homepage | Pass |
| Top Nav menu user logged out | Click brand logo | Displays homepage | Pass |
| Top Nav menu user logged out | Click books dropdown link | Displays dropdown: Fiction, non-fiction, children and teens links | Pass |
| Top Nav menu user logged out | Click fiction link | Displays books within the fiction category | Pass |
| Top Nav menu user logged out | Click non-fiction link | Displays books within the non-fiction category | Pass |
| Top Nav menu user logged out | Click children and teens link | Displays books within the children and teens category | Pass |
| Top Nav menu user logged out | Click All books link | Displays books within all books category | Pass |
| Top Nav menu user logged out | Click children and teens link | Displays books within the children and teens category | Pass |
| Top Nav menu user logged out | Click all products dropdown link | Displays dropdown: By Price, By Category, All products links | Pass |
| Top Nav menu user logged out | Click By Price link | Displays books By Price in ascending order | Pass |
| Top Nav menu user logged out | Click By Category link | Displays books By Category in ascending order | Pass |
| Top Nav menu user logged out | Click About dropdown link | Displays dropdown: Our Team, Our Events, Get in Touch links | Pass |
| Top Nav menu user logged out | Click Our Team Link link | Displays our team page | Pass |
| Top Nav menu user logged out | Click Our Events link | Displays our events page | Pass |
| Top Nav menu user logged out | Click Get in touch page link | Displays our get in touch form | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Books / All Products page user logged out | Image and info displayed for each book | Card display correct image and info | Pass |
|  Books / All Products page user logged out | Click product / book image | Display books detail page | Pass |
|  Books / All Products page user logged out | Click product / book image | Display books detail page | Pass |
|  Books / All Products page user logged out | Click category link: fiction, non-fiction, childrenand teens in books | Display the correct category of books | Pass |

[Back to top](#testing)

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Product detail page user logged out | Image and info displayed for each book | Card displays correct image and info | Pass |
|  Product detail page user logged out | Click product / book image | Displays image in new tab | Pass |
|  Product detail page user logged out | Click category link | Displays category appropiate product page | Pass |
|  Product detail page user logged out | Click increment and decrement button and 'add to bag' | Updates bag as expected | Pass |
|  Product detail page user logged out | Manually enter quantity and 'add to bag' | Updates bag accordingly | Pass |
|  Product detail page user logged out | Try entering a quantity above 100 or less than one | Displays error message | Pass |
|  Product detail page user logged out | Click keep shopping | Return to all products page | Pass |
|  Product detail page user logged out | Click add to bag | Toast with bag and delivery cost information is displayed. | Pass |
|  Product detail page user logged out | Click add to bag to check delivery fee functionality | If over £30 displays delivery is free. If under £30 displays how much to spend for free delivery | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Shopping bag user logged out | Click on shopping bag with no products | Display shopping bag is empty | Pass |
|  Shopping bag user logged out | Add products and check shopping bag | Displays correct titles, images, quantity, price and subtotal | Pass |
|  Shopping bag user logged out | Changing quantity of product in bag and click upadte | Display toast message with product updates | Pass |
|  Shopping bag user logged out | Change quantity manually and click update | Display toast message with product updates | Pass |
|  Shopping bag user logged out | Enter a decimal number fo quanity and update | Displays 500 error message | Pass |
|  Shopping bag user logged out | Click remove | Product is removed and toast message displayed | Pass |
|  Shopping bag user logged out | Remove all items from bag | Toast message displayed and shopping bag displays "Your bag is empty" | Pass |
|  Shopping bag user logged out | Click keep shopping | Returns to all products page | Pass |
|  Shopping bag user logged out | Click secure checkout | Displays checkout form | Pass |
|  Shopping bag user logged out | Adding product to an empty bag | Shopping bag icon changes from blue to green | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Checkout user logged out | Products, image, price and delivery cost displayed | All working accordingly | Pass |
|  Checkout user logged out | Place an order with an invalid email | Displays error message | Pass |
|  Checkout user logged out | Option to register or login at the bottom of the form | Links work as required | Pass |
|  Checkout user logged out | Option to register or login at the bottom of the form | Links work as required | Pass |
|  Checkout user logged out | Click adjust bag button | Leads to shopping bag page | Pass |
|  Checkout user logged out | Click complete order when input fields not complete | Displays "Please fill in this field" | Pass |
|  Checkout user logged out | Enter text in phone number field and process order | Accepts and processes order | Fail |
|  Checkout user logged out | Enter numbers in name field and process order | Accepts and processes order | Fail |
|  Checkout user logged out | Enter an invalid card number | Displays you card number is incomplete | Pass |
|  Checkout user logged out | Click complete order with fields completed correctly | Processes order | Pass |
|  Checkout user logged out | Form completed with stripe test card details | Toast message displayed with order number, information and email confirmation | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Checkout Success user logged out | Products, image, price and delivery cost displayed | All working accordingly | Pass |
|  Checkout Success user logged out | Webhook event checked in Stripe dashboard | Successful | Pass |
|  Checkout Success user logged out | Click "Return to our bookstore" | Redirects to all products page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Get in Touch Page user logged out | Click Get In Touch link | The correct form is displayed | Pass |
|  Get in Touch Page user logged out | Enter invalid email address | Error message displayed | Pass |
|  Get in Touch Page user logged out | Try sendng form with no data | Returns please fill in field | Pass |
|  Get in Touch Page user logged out | Click cancel button | Returns to homepage | Pass |
|  Get in Touch Page user logged out | Complete form correctly and click send message | djangoproject618@gmail.com recieves email and toast success message displayed | Pass |
|  Get in Touch Page user logged out | Complete form correctly and click send message | Redirects to Thank You page | Pass |
|  Get in Touch Page user logged out | Click on an empty input field | Input field becomes highlighted blue | Pass |

[Back to top](#testing)

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Footer user logged out | Click social icons | each icon opens in seperate tab | Pass |
|  Footer user logged out | Adjust screen size | Footer displays responsive design | Pass |


 Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Events page user logged out | Click events page link | Display the event page | Pass |
|  Events page user logged out | The event card displays an event name, host, date, time, duration and description of the event | Yes, clearly display these features | Pass |
|  Events page user logged out | Adjust screen size | Event page displays responsive design | Pass |


 Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Events page user logged out | Click events page link | Display the event page | Pass |
|  Events page user logged out | The event card displays an event name, host, date, time, duration and description of the event | Yes, clearly display these features | Pass |
|  Events page user logged out | Adjust screen size | Event page displays responsive design | Pass |
|  Events page user logged out | Click my account and Event Management not displayed | Event Management only visible for superuser | Pass |
|  Events page user logged out | Add and edit links only visible for superuser | Links not visible | Pass |


 Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
|  Team page user logged out | Click Team page link | Display the Team page | Pass |
|  Team page user logged out | The event card displays a team member name, position and bio | Yes, clearly display these features | Pass |
|  Team page user logged out | Adjust screen size | Team page displays responsive design | Pass |
|  Team page user logged out | Click my account and Team Management not displayed | Team Management only visible for superuser | Pass |
|  Team page user logged out | Add and edit links only visible for superuser | Links not visible | Pass |


### As a User Logged In

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Top Nav menu user logged in | Click Profile icon in main nav menu | Loads My Profile page | Pass |
| My Profile user logged in | User can see delivery info if previously saved and chronological order history | Yes, it displays this info | Pass |
| My Profile menu user logged in | Order history displays link to order number and order confirmation | Yes, it displays this info | Pass |
| My Profile menu user logged in | Click order history number link | Correclty displays the order confirmation | Pass |
| My Profile menu user logged in | Change default delivery data and click update information | Correclty displays updated values in field with a toat success message | Pass |
| My Profile menu user logged in | Change default delivery data and click update information | Correctly displays updated values in field with a toat success message | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Checkout user logged in | Displays users saved address with the name field left blank | Yes, the details are prefilled | Pass |
| Checkout user logged in | Bottom of the form displays a checkbox that saves delivery information | Yes, checkbox visible | Pass |
| Checkout user logged in | Update details at checkout with save information checkbox ticked and click secure checkout | Visit My Profile and delivery info updated | Pass |


[Back to top](#testing)


### Logged in as Admin

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| My Account | Displays Product management, Event Management, Team Management nav links | Yes, nav links are displayed | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Products | Edit and delete below product item links displayed when logged in as admin | Yes, edit and delete links displayed below product in all products and product details page are displayed | Pass |
| Products | Click edit link button | Displays edit product page | Pass |
| Products | Click delete link button | Product deletes and toast message displayed "Product deleted" | Pass |

| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Product Management Edit page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Product Management Edit page | Enter letters in price field | Does not allow this action | Pass |
| Product Management Edit page | Click dropdown | Displays correct dropdown category list items | Pass |
| Product Management Edit page | Click remove image and Update product | Image removed from product | Pass |
| Product Management Edit page | Click select image and select a image file | Image uploaded to product and only allows an image file to be selected | Pass |
| Product Management Edit page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Product Management Edit page | Click Update product | Displays toast message "Successully updated product" | Pass |
| Product Management Edit page | Click cancel button | Returns to all products page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Products | Click edit link button | Displays edit product page | Pass |
| Product Management Add Product page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Product Management Add Product page | Enter letters in price field | Does not allow this action | Pass |
| Product Management Add Product page | Click dropdown | Displays correct dropdown category list items | Pass |
| Product Management Add Product page | Click select image and select a image file | Image uploaded to product and only allows an image file to be selected | Pass |
| Product Management Add Product page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Product Management Add Product page | Fill form out correctly and click Add Product | Displays toast message "Successully added product" | Pass |
| Product Management Add Product page | Click cancel button | Returns to all products page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Event Management Edit page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Event Management Edit page | Enter letters in duration, event and time field | Does not allow this action | Fail |
| Event Management Edit page | Click choose file and select a file | Image uploaded to event page and only allows an image file to be selected | Fail |
| Event Management Edit page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Event Management Edit page | Fill form out correctly and click Update Event | Displays toast message "Successully updated event" | Fail |
| Event Management Edit page | Click cancel button | Returns to all events page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Event Management Add Event page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Event Management Add Event page | Enter letters in duration, event and time field | Does not allow this action | Fail |
| Event Management Add Event page | Click select image and select a image file | Image uploaded to product and only allows an image file to be selected | Fail |
| Event Management Add Event page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Event Management Add Event page | Click Add Event | Displays toast message "Successully added event" | Pass |
| Event Management Add Event page | Click cancel button | Returns to all products page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Team Management Edit page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Team Management Edit page | Enter letters in duration, Team and time field | Does not allow this action | Fail |
| Team Management Edit page | Click choose file and select a file | Image uploaded to Team page and only allows an image file to be selected | Fail |
| Team Management Edit page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Team Management Edit page | Fill form out correctly and click Update Team | Displays toast message "Successully updated Team" | Fail |
| Team Management Edit page | Click cancel button | Returns to Team page | Pass |


| Test Feature | Test Action | Expected Result | Result |
| ------------ | ----------- | --------------- | ------ |
| Team Management Add Team member page | Submit form with an empty required field | Generates error message "please fill in field" | Pass |
| Team Management Add Team member page | Enter letters in duration, Team and time field | Does not allow this action | Fail |
| Team Management Add Team member page | Click select image and select a image file | Image uploaded to product and only allows an image file to be selected | Fail |
| Team Management Add Team member page | Click a field within the form | Input field highlighted in blue for UX | Pass |
| Team Management Add Team member page | Click Add Team | Displays toast message "Successully added Team Member" | Pass |
| Team Management Add Team member page | Click cancel button | Returns to Team page | Pass |

