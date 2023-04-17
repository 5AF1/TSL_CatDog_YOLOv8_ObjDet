$(document).ready(function() {

    // Get reference to drop container element
    var dropContainer = document.getElementById('drop-container');
    // Disable default drag and drop behavior when dragging over or ending the drag on the drop container
    dropContainer.ondragover = dropContainer.ondragend = function() {
        return false;
    };
  
    // Handle file drop event
    dropContainer.ondrop = function(e) {
      e.preventDefault();
      // Load the dropped image
      loadImage(e.dataTransfer.files[0])
  }

  
    // Handle file selection through browse button
    $("#browse-button").change(function() {
        // Load the selected image
        loadImage($("#browse-button").prop("files")[0]);
    });
  

    // Initialize modal window
    $('.modal').modal({
        // Prevent modal from being dismissed by clicking outside the modal window
        dismissible: false,
        // Function to be executed when modal is opened
        ready: function(modal, trigger) {
            // Send an AJAX POST request to server with base64 encoded image data
            $.ajax({
                type: "POST",
                url: '/detect/api_request/',
                data: {
                    'image64': $('#img-card-1').attr('src')
                },
                dataType: 'text',
                success: function(data) {
                    // Load the statistics data on successful response from server
                    loadStats(data)
                }
            }).always(function() {
                // Close the modal window when the AJAX request is completed
                modal.modal('close');
            });
        }
    });

   

    // Handle click event for 'Go Back' button
    $('#go-back').click(function() {
        // Clear the image source and statistics table
        $('#img-card-1').removeAttr("src");
        $('#stat-table').html('');
        // Switch to the drag and drop container card
        switchCard(0);
    });

    // Handle click event for 'Go Start' button
    $('#go-start').click(function() {
        // Remove the results element and clear the statistics table
        var elem = document.getElementById("result");
        elem.parentNode.removeChild(elem);
        $('#stat-table').html('');
        // Switch to the drag and drop container card
        switchCard(0);
    });

    // Handle click event for 'Show' button
    $('#show').click(function() {
        // Switch to the image view container card
        switchCard(3);
        // Add timestamp to the image URL to bypass browser caching
        var timestamp = new Date().getTime();
        var el = document.getElementById("#img-card-2");
        var queryString = "?t=" + timestamp;
        el.src = "http://127.0.0.1:8000/detect/detector/static/test.jpeg" + queryString;
    });


    // Handle click event for 'Upload' button
    $('#upload-button').click(function() {
        // Open the modal window
        $('.modal').modal('open');
    });
  });
  
  // Function to switch between container cards
  switchCard = function(cardNo) {
    // Define the container class names
    var containers = [".dd-container", ".uf-container", ".dt-container", ".it-container"];
    
    // Get the visible container based on the cardNo parameter
    var visibleContainer = containers[cardNo];
    
    // Loop through all the containers
    for (var i = 0; i < containers.length; i++) {
      // Set opacity of the container based on whether it's the visible container or not
      var opacity = (containers[i] === visibleContainer) ? '1' : '0';
      
      // Animate the opacity of the container
      $(containers[i]).animate({
        opacity: opacity
      }, {
        duration: 200,
        queue: false,
      }).css("z-index", opacity);
    }
  }
  
  loadImage = function(file) {
    // Create a new file reader object
    var reader = new FileReader();
  
    // Define a function to execute once the file has been read
    reader.onload = function(event) {
      // Set the source of the image to the data URL of the file
      $('#img-card-1').attr('src', event.target.result);
    }
  
    // Read the file as a data URL
    reader.readAsDataURL(file);
  
    // Switch to the next container card
    switchCard(1);  
  }

  
  loadStats = function(jsonData) {
    // Switch to the statistics container card
    switchCard(2);
    
    // Parse the JSON data
    var data = JSON.parse(jsonData);
    
    // Get the objects data from the JSON
    var objects = data["objects"];
    
    // If the API call was successful
    if (data["success"] == true) {
      // Create a new div element to hold the JSON data
      var elem = document.createElement("div");
      elem.innerHTML = jsonData;
      elem.setAttribute('id', 'result');
      
      // Add the div element to the result-text container
      document.getElementById("result-text").appendChild(elem);
    }
  }
