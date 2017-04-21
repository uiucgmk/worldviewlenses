function increment(id) {
    var divName = "emoji-" + id;
   
    
    var countstr = document.getElementById(divName).innerHTML;
    var countarr=countstr.split(":");
    var count = countarr[1];
 	
 	var sentiment=countarr[0];
 	
 	//count can be only 0 or 1
 	//count = count + 1;
	
 	if (count=='0'){
   		count='1';
	} else {
		count='0';
	}


	    document.getElementById(divName).innerHTML = sentiment+":"+count;  
}
