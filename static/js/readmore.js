
function readmoreFunction(id) {

  var x=document.getElementById(id);
		console.log(id)
    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}
