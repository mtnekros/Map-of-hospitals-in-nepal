import folium


# create map
m = folium.Map(location=[29.783417, -119.677808], tiles='OpenStreetMap', zoom_start=4)

video_url = r'https://www.mapbox.com/bites/00188/patricia_nasa.webm'
bounds = [[32, -130], [13, -100]]
# adding video layer
folium.raster_layers.VideoOverlay(video_url,
                                  bounds,
                                  opacity=1.0,
                                  control=True,
                                  name='Video Layer',
                                  autoplay=True,
                                  loop=True
                                  ).add_to(m)

# adding layer control
folium.LayerControl().add_to(m)

# save the map
m.save('video_map.html')
