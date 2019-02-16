$.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  var expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function checkCookie() {
  var user = getCookie("username");
  if (user != "") {
    alert("Welcome again " + user);
  } else {
    user = prompt("Please enter your name:", "");
    if (user != "" && user != null) {
      setCookie("username", user, 365);
    }
  }
}

var user = getCookie("cart_id");
if (user != "") {
    console.log("Welcome again ");
}
else{
    setCookie("cart_id", -1, 360)
    console.log("setcookie thanh -1 thanh cong");
}
function add_cart(item_id, quantity){

    $.ajax({
        type: 'POST',
        url: '/cart/add/',
        data: JSON.stringify({
            "item_id": item_id,
             "quantity": quantity,
             "cart_id": getCookie("cart_id")
            }),
        contentType: "application/json",
        dataType: 'json'
         }).done(function(data, statusText, xhr){
            console.log(data);
           var status = xhr.status;                //200
           // var head = xhr.getAllResponseHeaders(); //Detail header info
            if(status==200){
                setCookie("cart_id", data, 360)
                console.log('set coookie thanh cong='+data)
                location.reload();
            }else{
                console.log('error');
            }

        });
}

