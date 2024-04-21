# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)


## Code Validation

[Back to top](#testing)
### HTML Testing

I used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

![html validation](./test-images/html-validator-no-erros.png)

| HTML Source Code/Page | Errors | Warnings |
| ---- | ------ | -------- |
| Home | 0 | 0 |
| All Books (including filtering and sorting) | 0 | 0 |
| Book Detail | 0 | 0 |
| Register | 0 | 0 |
| Log In | 0 | 0 |
| Logout| 0 | 0 |
| Profile | 0 | 0 |
| Product Management | 0 | 1 warning: Consider avoiding viewport values that prevent users from resizing documents |
| Edit Product | 0 | 1 warning: Consider avoiding viewport values that prevent users from resizing documents |
| Our Team | 0 | 0 |
| Team Management | 0 | 1 warning: Consider avoiding viewport values that prevent users from resizing documents |
| Edit Team | 0 | 1 warning: Consider avoiding viewport values that prevent users from resizing documents |
| Our Events | 0 | 0 |
| Event Management | 0 | 0 |
| Edit Event | 0 | 0 |
| Order History | 0 | 0 |
| Bag - Empty | 0 | 0 |
| Bag - Products | 0 | 0 |
| Checkout | 0 | 0 |
| Admin Panel (including all categories and templates) | 0 | 1 warning: Consider avoiding viewport values that prevent users from resizing documents |
| Get in Touch | 0 | 0 |


| Feature | admin | forms | models | urls | views | extra |
|---------|----------|----------|-----------|---------|----------|-------|
| Bag | n/a | n/a | n/a | none ![python validation](./test-images/bag-urls.py.png) | none ![python validation](./test-images/bag-views.py.png) | none ![python validation](./testing-images/article_widgets_py.png)  |

| Checkout | none ![python validation](./test-images/checkout-admin.py.png) | none ![python validation](./testing-images/checkout_forms_py.png) | none ![python validation](./testing-images/checkout_models_py.png) | none ![python validation](./testing-images/checkout_urls_py.png) | none ![python validation](./testing-images/checkout_views_py.png) | none ![python validation](./testing-images/checkout_signals_py.png), none ![python validation](./testing-images/checkout_wh_py.png), none ![python validation](./testing-images/checkout_webhooks_py.png)  |
| Contact | n/a | none ![python validation](./testing-images/contact_forms_py.png) | n/a | none ![python validation](./testing-images/contact_urls_py.png) | none ![python validation](./testing-images/contact_views_py.png) | n/a  |
| Enquiry |  none ![python validation](./testing-images/enquiry_admin_py.png) | none ![python validation](./testing-images/enquiry_forms_py.png) | none ![python validation](./testing-images/enquiry_models_py.png) | none ![python validation](./testing-images/enquiry_urls_py.png) | none ![python validation](./testing-images/enquiry_views_py.png) | n/a |
| Home | n/a |n/a | n/a | none ![python validation](./testing-images/home_urls_py.png) | none ![python validation](./testing-images/home_views_py.png) | n/a  |
| Newsletter | n/a |n/a | n/a | none ![python validation](./testing-images/newsletter_urls_py.png) | none ![python validation](./testing-images/newsletter_views_py.png) | n/a  |
| Products | none ![python validation](./testing-images/product_admin_py.png) | none ![python validation](./testing-images/product_forms_py.png) | none ![python validation](./testing-images/product_models_py.png) | none ![python validation](./testing-images/product_urls_py.png) | none ![python validation](./testing-images/product_views_py.png) | none ![python validation](./testing-images/product_widgets_py.png)  |
| Profile |  n/a | none ![python validation](./testing-images/profile_forms_py.png) | none ![python validation](./testing-images/profile_models_py.png) | none ![python validation](./testing-images/profile_urls_py.png) | none ![python validation](./testing-images/profile_views_py.png) | n/a |
| Review |  none ![python validation](./testing-images/review_admin_py.png) | none ![python validation](./testing-images/review_forms_py.png) | none ![python validation](./testing-images/review_models_py.png) | none ![python validation](./testing-images/review_urls_py.png) | none ![python validation](./testing-images/review_views_py.png) | n/a |
| Wishlist | none ![python validation](./testing-images/wishlist_admin_py.png) | n/a| none ![python validation](./testing-images/wishlist_models_py.png) | none ![python validation](./testing-images/wishlist_urls_py.png) | none ![python validation](./testing-images/wishlist_views_py.png) | none ![python validation](./testing-images/wishlist_contexts_py.png)  |