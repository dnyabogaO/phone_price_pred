function getOSValue() {
    var uiBedrooms = document.getElementByName("uiOS");
    for(var i in uiOS) {
        if(uiOS[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; //invalid value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var phone_make = document.getElementById("uiphones");
    var OS = getOSValue();
    var ROM = document.getElementById("uiROM");
    var RAM = document.getElementById("uiRAM");
    var screen_size = document.getElementById("uiscreen_size");
    var back_camera = document.getElementById("uiback_camera");
    var front_camera = document.getElementById("uifront_camera");
    var Battery = document.getElementById("uiBattery");
    var Rating = document.getElementById("uiRating");
    var Likes = document.getElementById("uiLikes");
    var specs_score = document.getElementById("uispecs_score");

    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_phone_price";
    //var url = "/api/predict_phone_price";

    $.post(url, {
        phone_make: phones.value,
        OS: OS,
        ROM: ROM,
        RAM: RAM,
        screen_size: screen_size,
        back_camera: back_camera,
        front_camera: front_camera,
        Battery: Battery,
        Rating: Rating,
        Likes: Likes,
        specs_score: specs_score

    },function(data,status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "Ksh</h2>";
        console.log(status);
    });

}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_phone_names";
    $.get(url,function(data,status) {
        console.log("got response for get_phone_names request");
        if(data) {
            var phones = data.phones;
            var uiphones = document.getElementById("uiphones");
            $('#uiphones').empty();
            for(var i in phones) {
                var opt = new Option(phones[i]);
                $('#uiphones').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;