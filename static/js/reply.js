function subreplyFunction(id){

  var reply=document.getElementById(id).value;
  
  var id_reply=id.split("\t\t");  
  
  $.post( "/replycomment", { 'all_data[]': id_reply, reply_data: reply } );
  alert("Your reply is saved!");
  document.getElementById(id).value="";
}
function replyFunction(id) {
  
  var x=document.getElementById(id);

    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}