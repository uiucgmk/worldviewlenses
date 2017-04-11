function increment(id) {
    var divName = "emoji-" + id;
    var count = document.getElementById(divName).innerHTML;
    count = parseInt(count);
    count = count + 1;
    document.getElementById(divName).innerHTML = count;  
}
