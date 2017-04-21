function shareFunction(shareid) {
     var whowhy; 
     whowhy_data= prompt("WHO and WHY do you want to share this? ","Who / Why");
	 var id_share=shareid.split("\t\t");
 	  
     $.post( "/share", { 'shareid[]': id_share, whowhy: whowhy_data} );
    }