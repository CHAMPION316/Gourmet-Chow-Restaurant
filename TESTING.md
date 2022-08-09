### UX Testing

| ID |  User wants to... | Issue Number | Comments
|--|--|--| -- |
| 01 | Edit or Delete booking | [Issue #13](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/13 "Issue #13") | Edit or delete bookings if plans in life change
| 02 | Contact page | [Issue #12](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/12 "Issue #12") | Contact page with information of the store
| 03 | Place a reservation | [Issue #11](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/11 "Issue #11") | Place a reservation with no double bookings
| 04 | Login in System | [Issue #9](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/9 "Issue #9") | Login system that allows you to view your bookings and make reservations
| 05 | Select guests size | [Issue #3](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/3 "Issue #3") | Select how many guests will be coming


## Automated Testing
This is the part of creating the application, I have found hard to get my head around. I have spent a lot of time reading the [django docs](https://docs.djangoproject.com/en/4.0/topics/testing/ "docs") and using the Code Institue lectures to try and help me, but unfortunately, I can admit I have a very long way to go until I'm comfortable creating these.

| App | File Name | Number of Tests | Results
|--|--|--|--
|checkout|test_models.py|6| NONE
|checkout|test_urls.py|3| NONE
|products|test_views.py|3| NONE


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
| [Issue #14](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/14 "Issue #14") | Time picker | Issue rendering the clock on the component which is giving a console error as well |
| [Issue #15](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/15 "Issue #15") | Fluid Table | Table for bookings is not fluid on medium to smaller devices, need to scroll left and right |
| [Issue #16](https://github.com/CHAMPION316/Gourmet-Chow-Restaurant/issues/16 "Issue #16") | Google Maps | Google map doesn't show up and some times it does you need to refresh the page, no idea why it does this |


## Unfixed Bugs

There are two errors that I am getting in the console when inspecting the application through Chrome.


* [Error one](docs/bugs/tempus-error.png "error") appears on all pages across the application
* [Error two](docs/bugs/type-error.png "error") appears on all pages across the application