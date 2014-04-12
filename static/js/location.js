function getLocation()
{
    var position_option = {enableHighAccuracy: true,maximumAge: 30000,timeout: 20000};
    if(navigator.geolocation)
    {
      navigator.geolocation.getCurrentPosition(getPositionSuccess, getPositionError, position_option);  
    }
    else
    {
        alert("非常抱歉，该浏览器不支持定位");
    }
}

function getPositionSuccess( position )
{
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    alert( "您所在的位置： 纬度" + lat + "，经度" + lng );
    var country=""
    var province=""
    var city=""
    if(typeof position.address !== "undefined")
    {
        country = position.address.country;
        province = position.address.region;
        city = position.address.city;
        alert(' 您位于 ' + country + province + '省' + city +'市');
    }
    sendLocatin(lng,lat,country,province,city);
}

function getPositionError(error) 
{
    switch (error.code) {
        case error.TIMEOUT:
            alert("连接超时，请重试");
            break;
        case error.PERMISSION_DENIED:
            alert("您拒绝了使用位置共享服务，查询已取消");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("获取位置信息失败");
            break;
        }
}

function sendLocatin(lng,lat,country,province,city)
{
    $.ajax({
        type: "get",
        dataType: "text",
        async: true,
        timeout: 10000,
        url: "http://xiaozhufeng.sinaapp.com/wechat/tg/nearby?lng="+lng+"&lat="+lat+"&country="+country+"&province="+province+"&city="+city,
        success: function() {
            alert("success");
        }
    });
}
