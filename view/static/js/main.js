"use strict"

let myForm = document.getElementById("user-text-form");

function postFormData(url, data) {
    return fetch(url, {
        method: "POST", 
        body: data,
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}

function addBodyElement(element, nameClass, Text) {
    let reference = document.getElementById('answer');
    let message = document.createElement(element);
    message.className = nameClass;
    message.innerHTML = Text;
    reference.appendChild(message)

}
function searchmap(latitude, longitude) {
    // Création d'options de carte 
    let reference = document.getElementById('answer');
    let newPicture = document.createElement('div');
    newPicture.className = 'map';
    let mapOptions = { 
        center: [latitude, longitude], 
        zoom: 10 
        } 
        // Création d'un objet de carte 
    let map = new L.map('map', mapOptions); 
        // Création d'un objet Layer 
    let layer = new L.TileLayer(' http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png' ); 
        // Ajout d'une couche à la carte 
    map.addLayer(layer); 
    let marker = new L.marker([latitude, longitude]).addTo(map);
    reference.appendChild(newPicture)

}

myForm.addEventListener("submit", function(event) {
    event.preventDefault();
    let userQuestion = document.getElementById('userText').value; //creer l'objet question utilisateur 
    addBodyElement('div', 'user', userQuestion); //et l'inserer
    //et vider le formulaire
    postFormData("/ajax", new FormData(myForm))
    .then (response => {
        let answer = response['papybot'] + response['extract'];
        addBodyElement('div', 'papy', answer);
        let reference = document.getElementById('answer');
        searchmap(51.958, 9.141);
        
        // Ici on veut mettre en place notre visuel
        // D'abord je cree la premiere div qui contient la reponse de grandpybot qui est dans response['papybot'] et response['extract']]^
        // Ici je cree une div de de classe map et je vais utiliser ca en tant qu'element
        //on passe cet element aux fonctions JS de creation de map
        // On insert les elements les uns apres les autres
    })
    
});
