"use strict";
const myForm = document.getElementById("myForm");
const inpFile = document.getElementById("inpFile");

myForm.addEventListener("submit", async event => {
  
  // prevents a page refresh, we don't want to send the form fields on the backend
    event.preventDefault();
    
    const bodyForm = new FormData();
    bodyForm.append('file', inpFile.files[0]);

    // why is this getelement is not on top with the others
    const fileNumber = document.getElementById("fileNumber").value;

    // the content-type header provides the client with the actual content type of the returned content. it returns a promise
    // todo how does it know when failed or suceedd
    axios({method: "put", url: `http://127.0.0.1:5000/api/v1/files/${fileNumber}`, data: bodyForm, headers: { "Content-Type": "multipart/form-data" },})
        .then((response) => {
          if (response.data == '-1') {
            alert(`file number ${fileNumber} was not found`);
          } else {
            alert(`file number ${fileNumber} was updated with new file`);
          }
        })
        .catch(() => {
          alert(`Update Failed`);
        });
})



