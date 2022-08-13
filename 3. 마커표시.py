import folium

map = folium.Map(location=[37,127],zoom_start=7)

marker=folium.Marker([37.591234104,127.034705638],
                     popup='고려대학교',
                     icon=folium.Icon(color='blue'))

marker.add_to(map)
map.save(r'F:\OneDrive - 천안중앙고등학교\pythonworkspace\PROJECT\대학지도제작PRJ\university_map.html')