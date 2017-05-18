// Adding a student to the roster

function showDestinationAirport(result) {
    // check for invalid requests,
    // add destination information to results-div,
    // show results-div

    if (result.is_valid_request == false) {
        $('#destination').html("Please choose a valid airport from list.");

    } else {
        $('#destination').html("You're flying to: " + result.destination_name + " (" + result.destination_code + ")");
    }

    $('#results-div').show();
}

function getOriginAirport(evt) {
    // prevent submit button from redirecting,
    // send data to route via POST request,
    // call lockOriginAirportForm

    evt.preventDefault();

    var formInputs = {
        'origin_airport': $('#origin-airport-field').val()
    };

    $.post('/find-destination',
           formInputs,
           showDestinationAirport
           );
}

$('#find-destination-btn').on('click', getOriginAirport);
