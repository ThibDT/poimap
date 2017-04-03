if (!$) {
    $ = django.jQuery;
}

var map = null;
var field = null;

$(window).on('map:init', function(e) {
    map = e.originalEvent.detail.map;
    map.on('map:loadfield', function (me) {
        field = me.field
    });
});


$(document).ready(function(){

    $("#id_country").val("FR");
    var address = $("#id_address");
    var zipcode = $("#id_zipcode");
    var city = $("#id_city");

    var geoButton = $("<button type='button'>Geoloc</button>").click(function(){
        var country = $("#id_country option:selected");
        if(country.val() && zipcode.val() && address.val()){
            var addr = (address.val()+",+"+zipcode.val()+"+"+city.val()).replace(" ","+")
            $.ajax({
               dataType: "json",
               url: "https://maps.googleapis.com/maps/api/geocode/json",
               data: {
                   address : addr,
                   key : "AIzaSyAThNRSpWOhnA2EGSeshFqLolrTPQx1hjo"
               },
               success: function(data){
                   if(data.status == "OK"){
                       if(data.results.length > 0) {
                           var cityResult = data.results[0]
                           var lat = cityResult.geometry.location.lat;
                           var lng = cityResult.geometry.location.lng;
                           var marker = L.marker([lat, lng])
                           field.store.save(marker);
                           field.load();
                           map.panTo(new L.LatLng(lat, lng));
                           map.setZoom(17);
                       }
                   }
               }
           })
       }
    })
    $("fieldset.address").append(geoButton);

    // $("#id_address").on("keyup", function(e){
    //     var country = $("#id_country option:selected");
    //     if(country.val() && zipcode.val()){
    //         $.ajax({
    //             dataType: "json",
    //             url: "https://maps.googleapis.com/maps/api/geocode/json",
    //             data: {
    //                 address : (address.val()+",+"+zipcode.val()+"+"+city.val()).replace(" ","+"),
    //                 key : "AIzaSyAThNRSpWOhnA2EGSeshFqLolrTPQx1hjo"
    //             },
    //             success: function(data){
    //                 if(data.status == "OK"){
    //                     if(data.results.length > 0) {
    //                         var cityResult = data.results[0]
    //                         var lat = cityResult.geometry.location.lat;
    //                         var lng = cityResult.geometry.location.lng;
    //                         var marker = L.marker([lat, lng])
    //                         field.store.save(marker);
    //                         field.load();
    //                         map.panTo(new L.LatLng(lat, lng));
    //                         map.setZoom(11);
    //                     }
    //                 }
    //             }
    //         });
    //     }
    // });
    //
    // $("#id_city, #id_zipcode").on("keyup", function(e){
    //     var country = $("#id_country option:selected");
    //     if(e.keyCode == 8){
    //         if(e.target.id == 'id_zipcode'){
    //             city.val("");
    //         }
    //         else if(e.target.id == 'id_city'){
    //             zipcode.val("");
    //         }
    //         return
    //     }
    //     if(country.val() && (zipcode.val().length == 5 || city.val().length > 2)){
    //         data = {
    //             username : "atiberghien",
    //             country : country.val(),
    //         }
    //         if(e.target.id == 'id_zipcode'){
    //             data["postalcode"] = zipcode.val();
    //         }
    //         else if(e.target.id == 'id_city'){
    //             data["placename"] = city.val();
    //         }
    //
    //         $.ajax({
    //             dataType: "json",
    //             url: "http://api.geonames.org/postalCodeSearchJSON",
    //             data: data,
    //             success: function(data){
    //                 if(data.postalCodes.length > 0) {
    //                         var cityResult = data.postalCodes[0]
    //                         if(e.target.id == 'id_zipcode' || cityResult.placeName.toLowerCase() == city.val().toLowerCase()){
    //                             city.val(cityResult.placeName)
    //                         }
    //                         zipcode.val(cityResult.postalCode)
    //                         var marker = L.marker([cityResult.lat, cityResult.lng])
    //                         field.store.save(marker);
    //                         field.load();
    //                         map.panTo(new L.LatLng(cityResult.lat, cityResult.lng));
    //                         map.setZoom(10);
    //                 }
    //             }
    //         });
    //     };
    // });
});