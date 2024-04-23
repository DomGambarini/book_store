# book_store
# Indie Book Emporium

Welcome to the **Indie Book Emporium**, your gateway to a world of undiscovered literary gems. Our e-commerce platform specializes in offering unique, captivating books from lesser-known publishers and writers, providing avid readers with access to titles not found in mainstream bookstores.

## Why Choose Indie Book Emporium?

At Indie Book Emporium, we believe in the power of storytelling and the magic of books that might not have a home on the shelves of larger retailers. Our selection includes a variety of alternative titles across genres, ensuring that there’s something intriguing for every reader.

## Community and Events

In addition to our diverse book collection, we are proud to host storytelling events for children, fostering a love for reading in the next generation and creating community ties through the joy of stories.

---

Join us in exploring the world of indie books, enhancing your reading experience, and discovering your next favorite author!

![Mock Up](documentation/website-images/mock-up.png)

# Table of Contents

- [Store-Goals] (#store-goals)

## Store Goals

### Indie Book Emporium is designed to achieve the following

- Establish **Indie Book Emporium** as a leading online destination for alternative and independently published books.

- Build a loyal customer base through, excellent customer service, quality products

- Continually expand the inventory to include a wider range of books from Independent publishers and lesser-known authors

- Boost overall sales through effective marketing and promotions

- Penetrate niche markets by targeting specific demographics interested in alternative and indie literature

- Increase user engagement through interactive features such as reviews, forums, social media

### Customer Goals

- Customers aim to find unique, lesser-known books that aren't available in mainstream bookstores.

- Customers expect the website to be easy to navigate, search, and make purchases with minimal hassle.

- Customers seek comprehensive information about the books, including detailed descriptions, author biographies, to make informed decisions.

- Customers want fast and reliable delivery options that ensure their books arrive in good condition and on time.

- Customers need a secure and straightforward checkout process to safeguard their personal and payment information.

## User Stories

### Viewing and Navigation
- As a visitor, I want to easily understand the main purpose of the Indie Book Emporium, so I can decide if I want to explore their book collection.
- As a customer, I want to easily navigate the website from any device (mobile/tablet/desktop), so I can access the bookstore anywhere.
- As a user, I want to see highlighted categories (e.g., new arrivals, most popular, staff picks) on the homepage, so I can quickly browse books that might interest me.
- As a user, I want to access detailed information about each book, including description, author, publication date, to help me make better purchasing decisions.

### Registration and User Accounts
- As a new user, I want to register for an account easily using my email address, so I can manage my purchases and receive updates.
- As a user, I want to log in to my account with a username and password, so that I can access my personal settings and history.
- As an account holder, I want to be able to reset my password if I forget it, to ensure I can regain access to my account.
- As a registered user, I want to be able to view my past orders and their statuses, so I can track what I have bought and when.

### Sorting and Searching
- As a user, I want to search for books by title, author, or keyword, so that I can find specific items I'm interested in.
- As a user, I want to filter search results by genre and price to find books that meet my criteria.

### Purchasing and Checkout
- As a customer, I want to add books to my cart easily from any listing or book detail page, so I can continue shopping without interruptions.
- As a customer, I want to view and modify the contents of my shopping cart, including quantities or removing items, before proceeding to checkout.
- As a customer, I want to check out through a simple, secure process, so I can confidently make purchases.
- As a customer, I want to receive a confirmation email after I make a purchase, so I can be sure my order has been processed.


## Technologies Used
### Languages

- [Python](https://www.python.org/) - Used for adding functionality to the application.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

### Frameworks and Software

- [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites.
- [Django](https://www.djangoproject.com/) - An MVT framework used to create the Tennis Buddies site.
- [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
- [Github](https://github.com/) - Used for hosting the repository.
- [Projects in GitHub](https://github.com/DomGambarini) - Used for project managament.
- [Heroku](https://heroku.com/) - Used for deploying the application.
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - Used to generate tables in Markdown.
- [Favicon Converter](https://favicon.io/favicon-converter/) - used to create a favicon in correct format.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
- [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used for responsiveness check.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used for debugginf and responsiveness testing.
- [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation python code.
- [Lucid Charts](https://lucidchart.com/) - for creating my ERD Diagram
- [AWS](https://aws.amazon.com/) - used for holding images and email sending sfunctionality
- [Stripe](https://stripe.com/en-cz) - used for providing a payment method to the store


### Python Packages
- asgiref==3.8.0
- boto3==1.34.77
- botocore==1.34.77
- certifi==2024.2.2
- cffi==1.16.0
- charset-normalizer==3.3.2
- cryptography==42.0.5
- defusedxml==0.7.1
- dj-database-url==0.5.0
- Django==3.2.25
- django-allauth==0.61.1
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.14.2
- gunicorn==21.2.0
- idna==3.6
- jmespath==1.0.1
- oauthlib==3.2.2
- packaging==24.0
- pillow==10.2.0
- psycopg2==2.9.9
- pycparser==2.21
- PyJWT==2.8.0
- python-dateutil==2.9.0.post0
- python-dotenv==1.0.1
- python3-openid==3.2.0
- pytz==2024.1
- requests==2.31.0
- requests-oauthlib==1.4.0
- s3transfer==0.10.1
- setuptools==69.2.0
- six==1.16.0
- sqlparse==0.4.4
- stripe==8.9.0
- typing_extensions==4.10.0
- urllib3==2.2.1


## Project Deployment

- To set up Django along with the necessary libraries, execute the following commands:

  * `pip3 install 'django<4' gunicorn`
  * `pip3 install dj_database_url psycopg2`

<details><summary><b>Library Installation Guide</b></summary>

![Library Installation](./readme-images/heroku_step_4.png)
</details><br>

- Following the installation, generate a requirements file:

  * `pip3 freeze --local > requirements.txt` - This command captures and lists the installed libraries in `requirements.txt`.

<details><summary><b>Generate Requirements File</b></summary>

![Generate Requirements](./readme-images/heroku_step_5.png)
</details><br>

- Proceed to create your project:

  * `django-admin startproject YOUR_PROJECT_NAME .` - Initiates your Django project.

<details><summary><b>Project Initialization</b></summary>

![Project Initialization](./readme-images/heroku_step_6.png)
</details><br>

- Next, establish your application within the project:

  * `django-admin startapp APP_NAME` - This command creates your application.

<details><summary><b>Application Setup</b></summary>

![Application Setup](./readme-images/heroku_step_7.png)
</details><br>

- To set up a superuser, enter the following command:
  `python3 manage.py createsuperuser`

  You'll be prompted to enter user details to complete the superuser setup.

- It's time to integrate the application in your project’s `settings.py` file:

<details><summary><b>Integrate Application in Settings</b></summary>

![Settings Integration](./readme-images/heroku_step_8.png)
</details><br>

- Proceed with the initial migration and start the server to ensure everything is operational. Use these commands:

  * `python3 manage.py migrate` - Applies database migrations.
  * `python3 manage.py runserver` - Starts the development server. To verify, use the 'open browser' button shown post command execution.

- Create an `env.py` file at the root level and include the necessary environment variables. Ensure this file is listed in your `.gitignore` to protect sensitive data:

  ```python
  import os

  os.environ["DATABASE_URL"] = "insert your own ElephantSQL database URL here"
  os.environ["SECRET_KEY"] = "enter a random secret key here"
