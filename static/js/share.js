function shareFunction(shareid) {
     
     var id_share=shareid.split("\t\t");

     alert("Shared!")
	$.post( "/share", { 'shareid[]': id_share} );
     
	 
    }
