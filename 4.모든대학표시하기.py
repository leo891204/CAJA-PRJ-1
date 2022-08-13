import imp
import pandas as pd
import folium
from folium.plugins import MiniMap
from folium.plugins import MarkerCluster



filepath = r'F:\OneDrive - 천안중앙고등학교\pythonworkspace\PROJECT\대학지도제작PRJ\학교주소좌표전환결과최종본.xlsx'
excel_file=pd.read_excel(filepath,engine='openpyxl', header=None)

excel_file.columns = ['학교이름', '주소', 'x', 'y', '웹페이지']

name_list = excel_file['학교이름'].to_list()
addr_list = excel_file['주소'].to_list()
position_x_list = excel_file['x'].to_list()
position_y_list = excel_file['y'].to_list()

web_list = excel_file['웹페이지']

map=folium.Map(location=[37,127],zoom_start=7)
for i in range(len(name_list)):
    if position_x_list[i] != 0:
        marker=folium.Marker([position_y_list[i],position_x_list[i]],
                             popup='<pre><b>'+name_list[i]+'<b></pre>'+'<pre>'+addr_list[i]+'</pre>'+'<pre>'+web_list[i]+'</pre>',
                             icon = folium.Icon(color='red', icon='star'))
        marker.add_to(map)


minimap = MiniMap() 
minimap.add_to(map)

map.save(r'F:\OneDrive - 천안중앙고등학교\pythonworkspace\PROJECT\대학지도제작PRJ\korea_university_map.html')