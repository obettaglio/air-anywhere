///// Datalist dropdown template found on Treehouse Blog: 
///// <http://blog.teamtreehouse.com/creating-autocomplete-dropdowns-datalist-element>

// Get the <datalist> and <input> elements.
var dataList = document.getElementById('airport-list');
var input = document.getElementById('origin-airport-field');

// Create a new XMLHttpRequest.
var request = new XMLHttpRequest();

// Handle state changes for the request.
request.onreadystatechange = function(response) {
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var jsonOptions = JSON.parse(request.responseText);

      // Loop over the JSON array.
      jsonOptions.forEach(function(item) {
        // Create a new <option> element.
        var option = document.createElement('option');
        // Set the value using the item in the JSON array.
        option.value = item;
        // Add the <option> element to the <datalist>.
        dataList.appendChild(option);
      });

      // Update the placeholder text.
      input.placeholder = "Select your airport";
    } else {
      // An error occured.
      input.placeholder = "Couldn't load datalist options";
    }
  }
};

// Update the placeholder text.
input.placeholder = "Select your airport";

// Convert CSV file to JSON.
airportsJSON = csvToJSON('/static/data/airports.csv');

// Set up and make the request.
request.open('GET', airportsJSON, true);
request.send();
