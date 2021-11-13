import folium
map = folium.Map(location=[-20.16291007051114, 57.52132921046838], tiles = "Stamen Terrain") 

feature_group = folium.FeatureGroup(name="My Map")
feature_group.add_child(folium.Marker(location=[-20.26291007051114,57.72132921046838], popup="Hi I am a marker", icon=folium.Icon(color='green')))
map.add_child(feature_group)

map.save("Map1.html")