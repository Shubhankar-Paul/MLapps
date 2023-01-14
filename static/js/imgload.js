const filepicker = document.getElementById('filepicker');

fileloaded = document.getElementById('file-loaded');
fileloaded.style.display="none"

filepicker.addEventListener('change', (event) => {
  const  target = event.target; 

  if (target.value && event.target.files[0].type.startsWith("image/")) {
    
    fileloaded = document.getElementById('file-loaded');
    fileloaded.style.display="block"

    filenotloaded = document.getElementById('file-not-loaded');
    filenotloaded.style.display="none"


    var preview = document.getElementById('PreviewImageID');
    preview.src = URL.createObjectURL(event.target.files[0]);

    
    var closebtn = document.getElementById('closebtn');
    closebtn.addEventListener('click', () => {

      target.value="";

      fileloaded = document.getElementById('file-loaded');
      fileloaded.style.display="none"
      
      filenotloaded = document.getElementById('file-not-loaded');
      filenotloaded.style.display="block"

    });

} else {

    fileloaded = document.getElementById('file-loaded');
    fileloaded.style.display="none"

    filenotloaded = document.getElementById('file-not-loaded');
    filenotloaded.style.display="block"

   
  }
});


