//===========================GLOBAL====================================

// Initializing tooltips
$(document).ready(function () {
  $('[data-toggle="tooltip"]').tooltip();

  //navbar inner dropdown
  $('.dropdown-submenu a.dropdown-item').on("click", function (e) {
    $(this).next('ul').toggle();
    e.stopPropagation();
    //e.preventDefault(); this stops a links from working
  });

  //scroll to top code------------------------------
  var mybutton = document.getElementById("myBtn");
  console.log(mybutton)
  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function () {
    scrollFunction()
  };

  function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      mybutton.style.display = "block";
    } else {
      mybutton.style.display = "none";
    }
  }
  // When the user clicks on the button, scroll to the top of the document
  function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }
});

// script for dark mode
$(".inner-switch").on("click", function () {
  if ($(".main-sec").hasClass("dark")) {
    $(".main-sec").removeClass("dark");
    $(".inner-switch").text("OFF");
  } else {
    $(".main-sec").addClass("dark");
    $(".inner-switch").text("ON");
  }
});
/*
 on(“click”, function() {…}) is an event handler that triggers the action inside the function when the user clicks the .inner-switch element,
 hasClass() checks if the .dark class is assigned to the .inner-switch element or not (this is based on the state of the toggle),
 removeClass() removes the .dark class from the HTML when the user switches to light mode,
 addClass() adds the .dark class to the HTML when the user switches to dark mode,
 text() sets the text of the label on the switch — it’s either “OFF” or “ON”.
*/