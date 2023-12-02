var message_timeout = document.getElementById("message-timer");

setTimeout(function () {
    
    message_timeout.style.display = "none";

}, 2500);


$(".bars").click(() => {
    $(".mobile__nav__fade__and__show__circle").toggleClass("open");
    $(".mobile__nav__fade__and__show").toggleClass("open");
    $(".bars").toggleClass("toggle")
    
})