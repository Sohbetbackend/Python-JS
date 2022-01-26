const modal = document.getElementById("sayla");
const btn = document.querySelector("button");
const userName = document.getElementById('userName');
const userValue = document.getElementById('userValue');
const span = document.getElementById("close");
const item = document.getElementById("dd");
const fileUpload = document.getElementById('yourBtn');



btn.onclick = function() {
  modal.style.display = 'block'
}
span.onclick = function() {
  modal.style.display = 'none'
}

item.onlick = function() {
  modal.style.display = 'none'
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = 'none'
  }
}

item.addEventListener('click', () => {
  modal.style.display = 'none'
  btn.style.display = 'none'
  userName.style.display = 'block'
  userName.value = userValue
})

function getFile(){
  document.getElementById("upfile").click();
}

function sub(obj) {
  const file = obj.value;
  const fileName = file.split("\\");
  fileUpload.innerHTML = fileName[fileName.length - 1];
  document.myForm.submit();
  event.preventDefault();
}

// function btnOnclick() {
//   modal.style.display = 'block'
// }

// function spanOnclick() {
//   modal.style.display = 'none';
// }

// function windowOnclick(event) {
//   if (event.target == modal) {
//     modal.style.display = 'none'
//   }
// }