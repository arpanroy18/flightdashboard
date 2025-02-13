from opensky_api import OpenSkyApi
import folium

api = OpenSkyApi()
states = api.get_states()

air_canada_flights = []
if states and states.states:
    for s in states.states:
        if s.callsign and s.callsign.strip().startswith(("ACA", "ROU", "JZA")):
            print(s)
            air_canada_flights.append(s)

# Create a map centered on North America with a dark theme
m = folium.Map(location=[56.130366, -106.346771], zoom_start=3, tiles='CartoDB dark_matter')

# Add markers for each Air Canada flight
for flight in air_canada_flights:
    if flight.latitude and flight.longitude:
        folium.Marker(
            [flight.latitude, flight.longitude],
            popup=f"Flight: {flight.callsign}<br>Altitude: {flight.baro_altitude} m",
            icon=folium.DivIcon(
                html=f'<div style="font-size: 24px; color: white;"><i class="fa fa-plane"></i></div>'
            )
        ).add_to(m)

# Save the map
m.save("air_canada_flights_map.html")

print(f"Total Air Canada flights: {len(air_canada_flights)}")

## hello
