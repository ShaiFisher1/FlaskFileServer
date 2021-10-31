"use strict";
document.getElementById("cardsForm").onsubmit = function() {
    GetFileData();
    return false;
};

/*
 TODO - you need that the url will send this fileNumber and not "1".
 look up how to add varible to string.
 it supposed to be like "file number ${fileNumber}" but its not working for some reason
*/

async function GetFileData() {
    const fileNumber = document.getElementById("fileNumber").value;
    await axios.get(`http://127.0.0.1:5000/api/v1/files/${fileNumber}`).then((response) => {
        document.getElementById('my_iframe').src = `http://127.0.0.1:5000/api/v1/files/${fileNumber}`;
        alert(`file number ${fileNumber} was downloaded`);
    }).catch((error) => {
        console.log("error", error);
        alert(`file with the id number: ${fileNumber} not exist`);
    })
}
