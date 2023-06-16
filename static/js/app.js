let lang1Dropdown = document.getElementById('lang1');
let lang2Dropdown = document.getElementById('lang2');
let textInput = document.getElementById('text');
let translationOutput = document.getElementById('translation');
let submitButton = document.getElementById('submit');
let input_lang = "";
let output_lang = "";
let input_text = "";
let output_text = "";

// get the language values from dropdowns
lang1Dropdown.addEventListener('change', function() { 
    input_lang = lang1Dropdown.value;
    console.log("source language: "+input_lang);
})

lang2Dropdown.addEventListener('change', function() { 
    output_lang = lang2Dropdown.value;
    console.log("target language: "+output_lang);
})



/* when submit button is pressed get the source language, target language
   source text, target text and send it to the server using an ajax xhr request */
submitButton.addEventListener('click', function() {
    
    // update the values for language and text
    input_lang = lang1Dropdown.value;
    output_lang = lang2Dropdown.value;
    input_text = textInput.value;
    console.log("source language: "+input_lang);
    console.log("target language: "+output_lang);
    console.log("source text: "+input_text);

   // create a new FormData object
    var formData = new FormData();

    // add the 3 strings to the form data
    formData.append('input_lang', input_lang);
    formData.append('output_lang', output_lang);
    formData.append('input_text', input_text);

    // send the AJAX request
    $.ajax({
    url: '/translate', // replace with your Flask endpoint URL
    type: 'POST',
    data: formData,
    processData: false,
    contentType: false,
    success: function(response) {
        console.log(response); // handle the response from the server
        output_text = response;
        translationOutput.value = output_text;
    },
    error: function(xhr, status, error) {
        console.log(error); // handle any errors
    }
    });

})