import json
import os
import folium

# defining path to data
health_path = os.path.join('Data', 'HealthFacilityDataNepal.geojson')
district_path = os.path.join('Data', 'district.geojson')

# loading json files to dictionaries
health_facility_dict = {}
with open(health_path, 'r') as f:
    health_facility_dict = json.load(f)

district_dict = {}
with open(district_path, 'r') as f:
    district_dict = json.load(f)


# creating a map object
m = folium.Map(location=[28.188727, 84.053896], tiles='OpenStreetMap', zoom_start=7)
folium.TileLayer(tiles='Stamen Toner').add_to(m)

# making FeatureGroups/Layers
health_fac_layer = folium.FeatureGroup(name='Health Facilities')
district_layer = folium.FeatureGroup(name='District Boundaries')

# global tooltip message
tt_msg = 'Click for more info'

# facilities to be loaded
hf_to_load = ['Hospital', 'Central Hospital', 'Zonal Hospital']

# dictionary for colors a/c to fac_type
hf_color = {'Hospital': 'yellow', 'Central Hospital': 'red', 'Zonal Hospital': 'orange'}

# adding locations of heath posts to a list
for feature in health_facility_dict['features']:
    health_fac_type = feature['properties']['HF_TYPE']
    loc = feature['geometry']['coordinates'][::-1]
    if health_fac_type in hf_to_load:
        folium.Marker(
            location=loc,
            popup='Type: ' + health_fac_type,
            tooltip='click to see facility type',
            icon=folium.Icon(
                icon_color=hf_color[health_fac_type],
                color='lightgray',
                icon='glyphicon glyphicon-plus'
            )
        ).add_to(health_fac_layer)

# reversing long lat for district coordinate list
for feature in district_dict['features']:
    for coordinate in feature['geometry']['coordinates'][0][0]:
        coordinate.reverse()

# adding Polygons to district FeatureGroup
for feature in district_dict['features']:
    folium.vector_layers.Polygon(
        locations=feature['geometry']['coordinates'][0][0],
        popup='District Name: <strong>'+feature['properties']['district'] + '</strong>',
        fill=True,
        color='crimson',
        weight=0.5
    ).add_to(district_layer)


# adding layers to map
district_layer.add_to(m)
health_fac_layer.add_to(m)

# adding layer control to map
folium.LayerControl().add_to(m)

# save map
m.save('Hospitals In Nepal.html')
