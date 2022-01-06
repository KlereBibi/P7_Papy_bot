"use strict"

document.getElementById("form").addEventListener("submit", getValue);

function getValue() {
    let a = document.getElementById("adresse").value;
    alert(a);
}
