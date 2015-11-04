from geolocation.google_maps import GoogleMaps

key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'    #Google Maps Geocoding API key

def coordinates(address):
    coord=[]
    google_maps=GoogleMaps(api_key=key)
    location=google_maps.search(location=address)
    my_location=location.first()
    coord.append(my_location.lat)
    coord.append(my_location.lng)
    return coord
