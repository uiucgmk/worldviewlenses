function shareFunction(shareid) {
     var whowhy; 
     whowhy_data= prompt("WHO and WHY do you want to share this? ","Who / Why");
	 var id=shareid.split("\t\t");
 	  
     $.post( "/share", { 'id[]': id, whowhy: whowhy_data} );
    }