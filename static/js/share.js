function shareFunction(shareid) {
     var whowhy;
     whowhy_data= prompt("Describe the person you want to share this comment with and explain why","");
     data2= prompt("Is the person you just answered similar to you or different? Type S (for Similar) or D (for Different)","S or D");
      
    while (data2!="S"&&data2!="s"&&data2!="D"&&data2!="d"){
        alert("Error - Your answer is not S or D")
        data2= prompt("Is the person you just answered similar to you or different? Type S (for Similar) or D (for Different)","S or D");
     }


     whowhy_data=whowhy_data+" : "+data2

     var id_share=shareid.split("\t\t");

     if (whowhy_data==""){
     	alert("Error - No anwser")
     }
     else{
		  alert("Successfully Submitted!")
	     $.post( "/share", { 'shareid[]': id_share, whowhy: whowhy_data} );
     }
	 
    }
