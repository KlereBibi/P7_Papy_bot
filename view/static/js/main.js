"use strict"

let myForm = document.querySelector("#user-text-form");

function postFormData(url, data) {
    return fetch(url, {
        method: "POST", 
        body: data,
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

myForm.addEventListener("submit", function(event) {
    event.preventDefault();
    //creer l'objet question utilisateur et l'inserer
    //et vider le formulaire
    postFormData("/ajax", new FormData(myForm))
    .then (response => {
        // Ici on veut mettre en place notre visuel
        // D'abord je cree la premiere div qui contient la reponse de grandpybot qui est dans response['papybot'] et response['extract']]^
        // Ici je cree une div de de classe map et je vais utiliser ca en tant qu'element
        //on passe cet element aux fonctions JS de creation de map
        // On insert les elements les uns apres les autres
    })
    
});
