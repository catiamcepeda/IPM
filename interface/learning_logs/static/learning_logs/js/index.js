var currentValue = 0;
function unidade_us(myRadio) {
    alert(currentValue);
    currentValue = myRadio.val();
    
}

function dropdown_1(val){
    var y = document.getElementsByName('dist');
    var aNode = y[0].innerHTML=val;
}   

function dropdown_2(val){
    var y = document.getElementsByName('conc');
    var aNode = y[0].innerHTML=val;
}   

function dropdown_3(val){
    var y = document.getElementsByName('freg');
    var aNode = y[0].innerHTML=val;
}   

function onSearch(val){
    var y = document.getElementsByClassName('us_s');
    y[0].innerHTML=val.style.visibility = "visible" ;
}   