function shareFunction(shareid) {
     var whowhy;
     whowhy_data= prompt("Describe the person you want to share this comment with and explain why","");
     
     var id_share=shareid.split("\t\t");


     if (whowhy_data == null || whowhy_data==""){
     	alert("Canceled")
     }
     else{
     	alert("Shared!")
	 	$.post( "/share", { 'shareid[]': id_share, whowhy: whowhy_data} );
     }
	 
    }
