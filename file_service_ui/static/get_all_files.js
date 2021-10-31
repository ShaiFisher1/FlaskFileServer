"use strict";
document.getElementById("allfiles").onsubmit = function() {
    GetAllFiles();
    return false;
};

/*
 TODO - you need that the url will send this fileNumber and not "1".
 look up how to add varible to string.
 it supposed to be like "file number ${fileNumber}" but its not working for some reason
*/

async function GetAllFiles() {
    await axios.get(`http://127.0.0.1:5000/api/v1/files`).then((response) => {
    for (const [key, value] of Object.entries(response.data)) {
            const res = document.createElement("P");         
            res.innerText = `${key}: ${value}`;    
            document.body.appendChild(res);

          }
    }).catch(() => {
        alert(`there are no files`);
    })
}
