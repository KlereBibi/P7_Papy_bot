"use strict"

let myForm = document.querySelector("#user-text-form");
myForm.addEventListener("submit", function(event) {
    event.preventDefault();
    fetch("/ajax", {
        method: "POST", 
        body: new FormData(myForm),
    })
});
