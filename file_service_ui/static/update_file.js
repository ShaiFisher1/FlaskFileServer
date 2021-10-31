"use strict";
const myForm = document.getElementById("myForm");
const inpFile = document.getElementById("inpFile");

myForm.addEventListener("submit", async event => {
    event.preventDefault();
    const bodyForm = new FormData();
    bodyForm.append('file', inpFile.files[0]);

    const fileNumber = document.getElementById("fileNumber").value;

/*
 TODO - you need that the url will send this fileNumber and not "1".
 look up how to add varible to string.
 it supposed to be like "file number ${fileNumber}" but its not working for some reason
*/

    axios({method: "put", url: `http://127.0.0.1:5000/api/v1/files/${fileNumber}`, data: bodyForm, headers: { "Content-Type": "multipart/form-data" },})
        .then(() => {
          alert(`file number ${fileNumber} was updated with new file`);
        })
        .catch(() => {
          alert(`file with the id number: ${fileNumber} not exist`);
        });
})



