import altair
import pandas as pd
import json

address = r'Data\HealthFacilityDataNepal.geojson'

# storing the features in geojson file to a dictionary
features = {}
with open(address) as in_file:
    features = json.load(in_file)['features']

# making a new dictionary of required information only
hfData = {'district': [],
          'lat': [],
          'long': [],
          'hfType': []
          }
# reading from features to hfData
count = 0
for f in features:
    dist_name = f['properties']['DIST_NAME']
    hf_type = f['properties']['HF_TYPE']
    if dist_name == 'Udayapur':
        count += 1
        if count > 300:
            continue
    if dist_name is None or hf_type is None:
        continue
    hfData['district'].append(f['properties']['DIST_NAME']),
    hfData['lat'].append(f['geometry']['coordinates'][1]),
    hfData['long'].append(f['geometry']['coordinates'][0]),
    hfData['hfType'].append(hf_type)

# converting to dict to pd.DataFrame
hfData_pd = pd.DataFrame(hfData)

chart = altair.Chart(hfData_pd).mark_circle().encode(
    latitude='lat:Q',
    longitude='long:Q',
    color='hfType'
).properties(
    height=500,
    width=700
)


(chart | chart.mark_bar().encode(x='district:O', y='count()').properties(width=1000).interactive()).serve()
