"use strict";
const validEmailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
const cardsContainer = document.createElement("div");
document.body.appendChild(cardsContainer);
clearAllCards();
loadCardsData();

document.getElementById("cardsForm").onsubmit = onSubmitUserElements;

function createCard(user) {
    let elements = createCardElement();

    setCardAttribute(elements);
    setCardInnerHTML(elements, user);
    appendCardToContainer(elements);
    elements.deleteButton.addEventListener("click", () => deleteUserCard(user.Id));
}

function createCardElement() {
    const cardElement = document.createElement("div");
    const fileNumberElement = document.createElement("div");
    const fileDataElement = document.createElement("div");
    const deleteButtonElement = document.createElement("button");

    return { card: cardElement, fileNumber: fileNumberElement, fileData: fileDataElement, deleteButton: deleteButtonElement };
}

async function setCardInnerHTML(elements, user) {
    elements.fileData.innerHTML = user.fileData;
    elements.fileNumber.innerHTML = user.fileNumber;
    elements.deleteButton.innerHTML = "delete";
}

function appendCardToContainer(elements,) {
    elements.card.appendChild(elements.fileNumber);
    elements.card.appendChild(elements.fileData);
    elements.card.appendChild(elements.deleteButton);
    cardsContainer.appendChild(elements.card);
}

function setCardAttribute(elements) {
    Object.values(elements).forEach((element) => element.setAttribute("class", "input-div"));

    elements.card.setAttribute("class", 'cardStyle');
    elements.deleteButton.setAttribute("class", "delete-butten-style");
}

function deleteUserCard(userIdInUsersArr) {
    const storage = localStorage.getItem("Cards") ?? "[]";
    const users = JSON.parse(storage);
    users.splice(userIdInUsersArr, 1);
    localStorage.setItem('Cards', JSON.stringify(users));
    clearAllCards();
    loadCardsData();
}

async function validateInput() {
    const fileNumber = document.getElementById("fileNumber").value;
    const fileData = await GetFileData(fileNumber);
    return { fileNumber: fileNumber, fileData: fileData };
}

async function onSubmitUserElements() {
    addCardToLocalStorage(await validateInput());
    clearAllCards();
    loadCardsData();
}
 
async function addCardToLocalStorage(userData) {
    const user = { fileNumber: userData.fileNumber, fileData: userData.fileData };
    const storage = localStorage.getItem("Cards") ?? "[]";
    const users = JSON.parse(storage);

    users.push(user);
    localStorage.setItem('Cards', JSON.stringify(users));
}

function loadCardsData() {
    const storage = localStorage.getItem("Cards") ?? "[]";
    const users = JSON.parse(storage);

    showAllCards(users);
}

function showAllCards(users) {
    let currentUserId = 0;
    users.forEach((user) => {
        const newCard = {fileNumber: user.fileNumber, fileData: user.fileData, id: currentUserId++};
        createCard(newCard);
    });
}

function clearAllCards() {
    cardsContainer.innerHTML = "";
}

async function GetFileData(fileNumber) {
    console.log("hello")
//    axios.get('http://127.0.0.1:5000/api/v2/files/2').then((res) => {
    console.log("in then");
    }).catch((error) => {
        console.log("in catch error");
    })
//    console.log("res", res)
//    return res
    return "maya is the best"
}