// Renders datepicker on the page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
});

function deferDateTimePicker_id_reservation_date_and_time() {
    if (window.jQuery && $.fn.datetimepicker) {
        $('#id_reservation_date_and_time').datetimepicker({
            "format": "L",
            "icons": {
                "time": "fa fa-clock-o"
            },
            "locale": "en-us"
        });
    } else {
        setTimeout(function () {
            deferDateTimePicker_id_reservation_date_and_time();
        }, 50);
    }
}

deferDateTimePicker_id_reservation_date_and_time();

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);