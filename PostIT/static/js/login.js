var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("btn");
var box_height = document.getElementsById("form-box");

function register() {
  x.style.left = "-400px";
  y.style.left = "50px";
  z.style.left = "130px";
  box_height = "520px";
}
function login() {
  x.style.left = "50px";
  y.style.left = "450px";
  z.style.left = "0px";
  box_height = "480px";
}
