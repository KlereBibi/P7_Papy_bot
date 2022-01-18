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

function divformap (){
    let reference = document.getElementById('answer');
    let message = document.createElement('div');
    let randomId = Math.random()
    let uniqueId = randomId.toString();
    message.className = 'map'
    message.id = uniqueId;
    reference.appendChild(message)
    return uniqueId
}
function searchmap(latitude, longitude) {
    let id = divformap()
    let mapOptions = { 
        center: [latitude, longitude], 
        zoom: 10 
        } 
    let map = new L.map(id, mapOptions); 
    let layer = new L.TileLayer(' http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png' ); 
    map.addLayer(layer); 
    let marker = new L.marker([latitude, longitude]).addTo(map);
}

myForm.addEventListener("submit", function(event) {
    event.preventDefault();
    let userQuestion = document.getElementById('userText').value; //creer l'objet question utilisateur 
    addBodyElement('div', 'user', userQuestion); //et l'inserer
    //et vider le formulaire
    postFormData("/ajax", new FormData(myForm))
    .then (response => {
        let answer = response['papybot'] + response['extract'];
        let latitude = Number(response['latitude'])
        let longitude = Number(response['longitude'])
        addBodyElement('div', 'papy', answer);
        searchmap(latitude, longitude);
        
        
        // Ici on veut mettre en place notre visuel
        // D'abord je cree la premiere div qui contient la reponse de grandpybot qui est dans response['papybot'] et response['extract']]^
        // Ici je cree une div de de classe map et je vais utiliser ca en tant qu'element
        //on passe cet element aux fonctions JS de creation de map
        // On insert les elements les uns apres les autres
    })
    
});
