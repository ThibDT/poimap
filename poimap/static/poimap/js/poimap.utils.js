function len(obj) {
    var size = 0;
    for (let key in obj) {
        if (obj.hasOwnProperty(key)) {
            size++;
        }
    }
    return size;
};

function resizeBbox (bbox, factor) {
    var currentXDistance = (bbox[2] - bbox[0]);
    var currentYDistance = (bbox[3] - bbox[1]);
    var newXDistance = currentXDistance * factor;
    var newYDistance = currentYDistance * factor;
    var xChange = newXDistance - currentXDistance;
    var yChange = newYDistance - currentYDistance;

    var lowX = bbox[0] - (xChange / 2);
    var lowY = bbox[1] - (yChange / 2);
    var highX = (xChange / 2) + bbox[2];
    var highY = (yChange / 2) + bbox[3];

    var sized = [lowX, lowY, highX, highY];
    return sized;
}

L.Marker.prototype.fetchGeoInfo = function(labelId) {
    $.ajax({
        dataType: "json",
        url: "https://maps.googleapis.com/maps/api/geocode/json",
        data: {
            latlng : this.getLatLng().lat+","+this.getLatLng().lng,
            language : 'fr',
            location_type : 'GEOMETRIC_CENTER',
            key : "AIzaSyAThNRSpWOhnA2EGSeshFqLolrTPQx1hjo"
        },
        success: function(data){
            if(data.status == "OK"){
                if(data.results.length > 0) {
                    var poiResult = data.results[0];
                    $(labelId+" span.geo-text").text(poiResult.formatted_address);
                    $(labelId+" input").val(poiResult.formatted_address);
                }
            }
        }
    });
}

L.Marker.prototype.applyDragEventListener = function (currentPath, markerOptions) {
    this.on('drag', function(e) {
        var nearest = leafletKnn(currentPath).nearest(e.target.getLatLng(),1)[0];
        this.setLatLng([nearest.lat, nearest.lon]);
    });
    this.on('dragend', function(e) {
        this.fetchGeoInfo(markerOptions.labelId)
    });
}