// Smooth scroll to section
$(document).ready(function(){
    $('a[href^="#"]').on('click', function(e){
        e.preventDefault();
        var target = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 1000);
    });
});

// Form submission handling
$(document).ready(function(){
    $('#contact-form').submit(function(e){ // Change the selector to target the contact form
        e.preventDefault();
        
        // Collect form data
        var formData = $(this).serialize();
        
        // Example: AJAX request to handle form submission
        $.ajax({
            type: 'POST',
            url: 'your-form-handler.php', // Replace 'your-form-handler.php' with your actual form handler URL
            data: formData,
            success: function(response){
                // Handle successful form submission
                $('.sent-message').text('Your message has been sent. Thank you!');
                $('.sent-message').show();
            },
            error: function(xhr, status, error){
                // Handle form submission error
                console.error(xhr.responseText);
                $('.error-message').text('Error occurred while sending your message. Please try again later.');
                $('.error-message').show();
            }
        });
    });
});
