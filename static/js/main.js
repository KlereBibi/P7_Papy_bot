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
    let randomId = new Date();
    let uniqueId = randomId.toString();
    message.className = 'map'
    message.id = uniqueId;
    reference.appendChild(message)
    return uniqueId
}
function addBodyPicture(latitude, longitude) { 
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
    let userQuestion = document.getElementById('userText').value; 
    addBodyElement('div', 'user', userQuestion);
    document.getElementById('spinner').removeAttribute("class");
    postFormData("/ajax", new FormData(myForm))
   .then (response => {
        if (response['result'] === 'finded') {
            setTimeout(function(){
                document.getElementById("user-text-form").reset()
                document.getElementById('spinner').className = "hidden";
                let answer_papybot = response['papybot_adress']
                let adresse = response['adress']
                let remember_papybot = response['papybot'] 
                let answer = response['extract']; 
                let latitude = Number(response['latitude'])
                let longitude = Number(response['longitude'])
                addBodyElement('div', 'papy1', answer_papybot);
                addBodyElement('div', 'papy', adresse);
                addBodyPicture(latitude, longitude);
                addBodyElement('div', 'papy1', remember_papybot);
                addBodyElement('div', 'papy', answer);
                 }, 1500)
                ; }
        else {
            setTimeout(function(){
                document.getElementById("user-text-form").reset();
                document.getElementById('spinner').className = "hidden";
                let excuse = response['papysorry']
                let precision = response['papyprecision']
                addBodyElement('div', 'papy', excuse);
                addBodyElement('div', 'papy', precision);
                }, 1500)}
    }) 
});
