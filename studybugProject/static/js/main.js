
function chk_i(e){
    console.log(e.classList);
        if(e.classList.contains("active")) e.classList.remove("active");
        else {
            e.classList.add("active"); 
        }
}

 
function pu_close(){ 
    $(".bg").hide();
    $(".pop_up").hide();  
}

function _back(){
    history.back();
}