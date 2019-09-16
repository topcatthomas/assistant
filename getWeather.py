from geopy.geocoders import Nominatim
import datapoint
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("southgate")
api_key = 'db5dfa10-ec3f-41b6-a4f1-380cb204b194'
conn = datapoint.connection(api_key = api_key)
site = conn.get_nearest_forecast_site(location.latitude, location.longitude)
forecast = conn.get_forecast_for_site(site.id, "daily")
for day in forecast.days:
    print("\n%s" % day.date)

    # Loop through time steps and print out info
    for timestep in day.timesteps:
        print(timestep.date)
        print(timestep.weather.text)
        print("%s%s%s" % (timestep.temperature.value,
                          '\xb0', #Unicode character for degree symbol
                          timestep.temperature.units))