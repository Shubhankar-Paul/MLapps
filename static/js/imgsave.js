var dbtn = document.getElementById('D-btn');
dbtn.addEventListener('click', () => {
  const imagePath  = document.getElementById('pred').src;
  if (imagePath) {
    var typesave = document.getElementsByName('typesave');   
    for(i = 0; i < typesave.length; i++) {
      if(typesave[i].checked) {
        saveAs(imagePath, typesave[i].value);  //imagePath.substring(imagePath.lastIndexOf('/')+1);
        //downloadImage(imagePath);
      }
    }
  }  
});

function downloadImage(url) { 
  fetch(url, {
    mode : 'no-cors',
  })
  .then(response => response.blob())
  .then(blob => {
    let blobUrl = window.URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.download = url.replace(/^.*[\\\/]/, '');
    a.href = blobUrl;
    document.body.appendChild(a);
    a.click();
    a.remove();
  });
}; 