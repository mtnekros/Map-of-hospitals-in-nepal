import pandas
import os
import folium

# district csv file reading
district_data_path = os.path.join('Data', 'district_pop.csv')
district_data = pandas.read_csv(district_data_path)

# json file
district = os.path.join('Data', 'district.geojson')

# create map
map_ = folium.Map(location=[28.188727, 84.053896], tiles='OpenStreetMap', zoom_start=7)

# create choropleth and add to map
folium.Choropleth(
    geo_data=district,
    name='Population',
    data=district_data,
    columns=['district', 'pop'],
    key_on='feature.properties.district',
    fill_color='BuGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population',
    highlight=True
).add_to(map_)

folium.LayerControl().add_to(map_)

map_.save('Choropleth.html')
