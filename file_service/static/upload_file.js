"use strict";
const myForm = document.getElementById("myForm");
const inpFile = document.getElementById("inpFile");

myForm.addEventListener("submit", event => {
    event.preventDefault();

    const bodyForm = new FormData();

    bodyForm.append('file', inpFile.files[0]);


/*
 TODO - you need that the url will send this fileNumber and not "1".
 look up how to add varible to string.
 it supposed to be like "file number ${fileNumber}" but its not working for some reason
*/

    axios({
        method: "post",
        url: "http://127.0.0.1:5000/api/v1/files",
        data: bodyForm,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then( (response) =>{
          alert(response.data);
        })
        .catch(() => {
          alert(`upload failed`);
        });

})