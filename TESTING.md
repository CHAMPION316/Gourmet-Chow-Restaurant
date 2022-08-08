## Code Validation

### HTML
| File Name | File Path | Result | W3C | Comments |
|--|--|--|--|--|
| base.html | templates/restaurant/index.html | PASS | [link](docs/html-test/index-validation.png) ||
| menu.html | templates/restaurant/menu.html | PASS | [link](docs/html-test/menu-validation.png) ||
| add_booking.html | templates/restaurant/add_booking.html | Fail (widget) | [link](docs/html-test/add-booking-validation.png) | Input in a widget out of my control |
| contact.html | templates/restaurant/contact.html | PASS |[link](docs/html-test/contact-validation.png)  ||
| view_booking.html | templates/restaurant/view_booking.html | Fail (input in table) | [link](docs/html-test/view-booking-validation.png) | Input in a widget out of my control |
| edit_booking.html | templates/restaurant/edit_booking.html | 1-Error 2-Warnings | [link](docs/html-test/edit-booking-validation.png) | Input in a widget out of my control |
| delete_booking.html | templates/restaurant/delete_booking.html | 2-Errors 2-Warnings | [link](docs/html-test/delete-booking-validation.png) | Input in a widget out of my control |
| logout.html | templates/account/logout.html | PASS | [link](docs/html-test/logout-validation.png) ||
| login.html | templates/account/login.html | PASS | [link](docs/html-test/login-validation.png) ||


### Python
| File Name | File Path | Result | PEP8 | Comments |
|--|--|--|--|--|
| admin.py | reservations/admin.py | PASS | [link](docs/python-test/admin-validation.png) || 
| forms.py | reservations/forms.py | PASS | [link](docs/python-test/forms-validation.png) ||
| apps.py | reservations/apps.py | PASS | [link](docs/python-test/apps-validation.png) ||
| models.py | reservations/models.py | PASS | [link](docs/python-test/models-validation.png) ||
| views.py | reservations/views.py | PASS | [link](docs/python-test/views-validation.png) ||
| urls.py | bag/urls.py | PASS | [link](readme/docs/validation/python/bag/urls.png "link") ||

### CSS
| File Name | File Path | Result | W3C | Comments |
|--|--|--|--|--|
| base.css | static/css/style.css | PASS | [link](docs/css-test/style-validation.png) |[1 warnings](docs/css-test/css-warning.png)|


### JS
| File Name | File Path | Result | JSHint | Comments |
|--|--|--|--|--|
| script.js | static/js/script.js | PASS | [link](docs/js-test/script-validation.png) || [4 Warnings](docs/js-test/script-warning.png)
| contact.js | static/js/contact/contact.js | PASS | [link](docs/js-test/contact-validation.png) || [3 Warnings](docs/js-test/contact-warning.png)

\
&nbsp; 


## Bugs

| Issue Number |  Title | Comments 
|--|--|--|
| [Issue #26](https://github.com/sam-timmins/swanbourne_village_stores/issues/26 "Issue #26") | Navbar authentication links | Login and register links are stacked when the user is unauthenticated |
| [Issue #61](https://github.com/sam-timmins/swanbourne_village_stores/issues/61 "Issue #61") | Create product form slug error | When there is an error during creating a product, the slug error text shows and throws off the styling.|
| [Issue #51](https://github.com/sam-timmins/swanbourne_village_stores/issues/51 "Issue #51") | Dropdown Menu | The dropdown menu class has a style applied to it giving a max-width. |
| [Issue #110](https://github.com/sam-timmins/swanbourne_village_stores/issues/110 "Issue #110") | Webhooks | Webhooks are not working, getting a 401 error in Stripe |
| [Issue #129](https://github.com/sam-timmins/swanbourne_village_stores/issues/129 "Issue #129") | Edit works link in navbar not working | Edit works link in navbar not working, giving a 500 error |