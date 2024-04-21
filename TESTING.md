# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)


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


| Feature               | admin                                       | forms                                       | models                                      | urls                                        | views                                       | extra                                      |
|-----------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|--------------------------------------------|
| Bag                   | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/bag-urls.py.png) | none ![python validation](./test-images/bag-views.py.png) | none ![python validation](./test-images/article_widgets_py.png) |
| Checkout              | none ![python validation](./test-images/checkout-admin.py.png) | none ![python validation](./test-images/checkout-forms.py.png) | none ![python validation](./testing-images/checkout-models.py.png) | none ![python validation](./testing-images/checkout_urls_py.png) | none ![python validation](./test-images/checkout-views.py.png) | none ![python validation](./test-images/checkout-signals.py.png), none ![python validation](./test-images/checkout-webhook-handler.py.png), none ![python validation](./test-images/checkout-webhooks.py.png) |
| Contact               | n/a                                         | none ![python validation](./test-images/contact-forms.py.png) | n/a                                         | none ![python validation](./test-images/contact-urls.py.png) | none ![python validation](./test-images/contact-views.py.png) | n/a                                        |
| Events                | none ![python validation](./test-images/events-admin.py.png) | none ![python validation](./test-images/events-forms.py.png) | none ![python validation](./test-images/events-models_py.png) | none ![python validation](./test-images/events-urls.py.png) | none ![python validation](./test-images/events-views.py.png) | n/a                                        |
| Home                  | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/home-urls.py.png) | none ![python validation](./test-images/home-views.py.png) | n/a                                        |
| Indie Book Emporium  | n/a                                         | n/a                                         | n/a                                         | none ![python validation](./test-images/indie-book-emporium-urls.py.png) | n/a                                         | ![python validation](./test-images/indie-book-emporium-settings.py.png) |
| Products              | none ![python validation](./test-images/product-admin.py.png) | none ![python validation](./test-images/product-forms.py.png) | none ![python validation](./test-images/product-models.py.png) | none ![python validation](./test-images/product-urls.py.png) | none ![python validation](./testing-images/product-views.py.png) | none ![python validation](./testing-images/product-widget.py.png) |
| Profile               | n/a                                         | none ![python validation](./test-images/profile-forms.py.png) | none ![python validation](./test-images/profile-models.py.png) | none ![python validation](./test-images/profile-urls.py.png) | none ![python validation](./test-images/profile-views.py.png) | n/a                                        |
| Team                  | none ![python validation](./test-images/team-admin.py.png) | none ![python validation](./test-images/team-forms.py.png) | none ![python validation](./test-images/team-models.py.png) | none ![python validation](./test-images/team-urls.py.png) | none ![python validation](./test-images/team-views.py.png) | n/a                                        |

