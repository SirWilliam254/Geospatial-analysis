Geocoding is the process of converting addresses or locations into geographic coordinates (latitude and longitude) so that they can be plotted on a map. In Python, there are several libraries that you can use to geocode addresses and locations.

One popular library for geocoding in Python is Geopy. It is a simple and easy-to-use library that allows you to geocode addresses and locations using various services such as OpenStreetMap, Nominatim, and Google Maps. To use Geopy, you need to install the library first, then you can use it to geocode an address with a simple line of code like this:

```python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.latitude, location.longitude)
```

Another library you can use is GeoPy, it's a Python wrapper for several popular geocoding web services, such as Google Geocoding API, OpenStreetMap Nominatim, GeoNames, and others. You can use it in a similar way to Geopy

```python
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("175 5th Avenue NYC")
print(location.latitude, location.longitude)
```

Another popular library is reverse_geopy, it's useful if you want to geocode an address from a latitude, longitude pair, instead of the other way around.

It's important to note that some of the geocoding services may require an API key, which you will need to provide when using the library, also some of the services may have usage limit, depending on your usage you may need to look into paid plans.

Also, it's good to know that some geocoding services may not have full coverage of the world, or may not have the most recent and accurate data, so it's always a good idea to verify the results of geocoding against a known correct location.
