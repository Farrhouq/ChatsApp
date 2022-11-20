var now_factors = document.querySelectorAll('.now-factor');
var rounded_pills = document.querySelectorAll('.rounded-pill');

for(i=0; i<now_factors.length; i++){
    if (now_factors[i].innerHTML == '0&nbsp;minutes ago'){
        now_factors[i].innerHTML = 'now';}
}


camera_icon = document.getElementById('camera_icon')
    document.onload(
        camera_icon.style.display = 'none'
    )
    function preview_image(event) {
        var reader = new FileReader();
        reader.onload = function () {
            var output = document.getElementById('camera_icon');
            output.style.display = 'block'
            output.style.backgroundImage = "url('" + reader.result + "')";
        }
        reader.readAsDataURL(event.target.files[0]);
    }