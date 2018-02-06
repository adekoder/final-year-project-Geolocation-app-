function getUserDeviceLocation(success,error)
{
    if(navigator.geolocation)
    {
       navigator.geolocation.getCurrentPosition(success,error);
    }
}




