function increment(id) {
    var divName = "emoji-" + id;
    var count = document.getElementById(divName).innerHTML;
    count = parseInt(count);
 	//count can be only 0 or 1
 	//count = count + 1;
	
 	if (count==0){
   		count=1;
	} else {
		count=0;
	}
    document.getElementById(divName).innerHTML = count;  
}
