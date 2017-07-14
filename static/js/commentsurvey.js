function popup_comment(interface,post){
  

  var link="";
  if (post=="3"){
//  link="https://goo.gl/forms/Zg9nG0XfY7XVRjiM2";
  link="https://goo.gl/forms/fgWD0oipEdjjCUN63";
 }else{ //post==5
 // link="https://goo.gl/forms/Zx7DbfFyjgWiJrMZ2";
  link="https://goo.gl/forms/pElQcZBGmUadGwTj1";
 }

  //var link="https://goo.gl/forms/vrqxPzOCBcT94QPz2";
/*if (interface=="w" && post=="1"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
 else if (interface=="w" && post=="2"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else if (interface=="w" && post=="3"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else  if (interface=="w" && post=="5"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else  if (interface=="c" && post=="1"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else  if (interface=="c" && post=="2"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else  if (interface=="c" && post=="3"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }
else  if (interface=="c" && post=="5"){
  link="https://goo.gl/forms/IGkiVFpYqP98tPdo2";
 }*/
  cuteLittleWindow = window.open(link, "littleWindow", "location=no,width=760,height=500");
}
