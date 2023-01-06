from geopy.geocoders import GoogleV3
from geopy import distance
geolocator = GoogleV3(api_key="AIzaSyDks2ISyIBq1r49dFD_IHkYCKl1FLihSJE") #api key
def find_distance(location1_name, location2_name):
    location1 = geolocator.geocode(location1_name)
    location2 = geolocator.geocode(location2_name)
    if (location1 != None and location2 != None ):
        distance_between_locations = distance.distance((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).kilometers
        print(f"The distance between {location1_name} and {location2_name} is {distance_between_locations} km.")
        return f"The distance between {location1_name} and {location2_name} is {distance_between_locations} km."
    else:
        print("Invalid input location")
        return "Invalid input location"
    