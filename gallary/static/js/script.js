function validateform(){
    x=document.forms["loginform"]["email"].value;
    if (x==""){
        document.getElementById("inputEmail3").placeholder="enter valid email";
        document.getElementById("inputEmail3").style.border="3px solid red";
        var p=document.getElementById("valid");
        p.innerHTML="enter valid email";
        p.style.color="red";
        p.style.fontFamily="vardana";
        return false;
    }
    
}