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

      // var lines = request.responseText.split("\n");
      // var result = [];
      // var headers = lines[0].split(",");

      // for (var i = 1; i < lines.length; i++) {
      //   var obj = {};
      //   var currentLine = lines[i].split(",");

      //   for (var j = 0; j < headers.length; j++) {
      //     obj[headers[j]] = currentLine[j];
      //   }

      //   result.push(obj);

      // }

      // resultJSON = JSON.stringify(result);
      // console.log(resultJSON);

      // console.log(request.responseText);

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
input.placeholder = "Loading...";

// Set up and make the request.
request.open('GET', '/static/data/airports.json', true);
request.send();
