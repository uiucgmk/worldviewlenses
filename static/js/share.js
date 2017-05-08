function shareFunction(shareid) {
     var whowhy;
     whowhy_data= prompt("WHO and WHY do you want to share this? ","");
     var id_share=shareid.split("\t\t");

     if (whowhy_data==""){
     	alert("Error - No anwser")
     }
     else{
		  alert("Successfully Submitted!")
	     $.post( "/share", { 'shareid[]': id_share, whowhy: whowhy_data} );
     }
	 
    }
