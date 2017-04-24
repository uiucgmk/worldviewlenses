function shareFunction(shareid) {
     console.log('I am here1')
     var whowhy;
     whowhy_data= prompt("WHO and WHY do you want to share this? ","Who / Why");
     console.log('I am here2')
	 var id_share=shareid.split("\t\t");

     $.post( "/share", { 'shareid[]': id_share, whowhy: whowhy_data} );
    }
