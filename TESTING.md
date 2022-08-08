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
