var now_factors = document.querySelectorAll('.now-factor');
var rounded_pills = document.querySelectorAll('.rounded-pill');

for(i=0; i<now_factors.length; i++){
    if (now_factors[i].innerHTML == '0&nbsp;minutes ago'){
        now_factors[i].innerHTML = 'now';}
}