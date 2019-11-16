
function chk_i(e,n){
    active = n;
        if(e.classList.contains(active)) e.classList.remove(active);
        else {
            e.classList.add(active); 
        }
}

function cchk_i(e,c){
    console.log(e.classList); 
    if(e.classList.contains(c)) e.classList.remove(c);
    else {
        $("."+c).removeClass(c);
        e.classList.add(c); 
    }
}
 
function pu_close(){ 
    $(".bg").hide();
    $(".pop_up").hide();  
}

function _back(){
    history.back();
}