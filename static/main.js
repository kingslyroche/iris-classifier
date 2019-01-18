var slider1 = document.getElementById("sepal_length");
var output1 = document.getElementById("sepal_length_output");
output1.innerHTML = slider1.value;

slider1.oninput = function() {
  output1.innerHTML = this.value;
}

var slider2 = document.getElementById("sepal_width");
var output2 = document.getElementById("sepal_width_output");
output2.innerHTML = slider2.value;

slider2.oninput = function() {
  output2.innerHTML = this.value;
}

var slider3 = document.getElementById("petal_length");
var output3 = document.getElementById("petal_length_output");
output3.innerHTML = slider3.value;

slider3.oninput = function() {
  output3.innerHTML = this.value;
}

var slider4 = document.getElementById("petal_width");
var output4 = document.getElementById("petal_width_output");
output4.innerHTML = slider4.value;

slider4.oninput = function() {
  output4.innerHTML = this.value;
}