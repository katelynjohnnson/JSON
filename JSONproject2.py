from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import json

infile = open('US_fires_9_14.json', 'r')
outfile = open('readable_9_14.json', 'w')

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

bright, lons, lats, hover_texts = [], [], [], []

for f in fire_data:
    br = f['brightness']
    if br in ['brightness'] > 450:
        print(br)
    lon = f['longitude']
    lat = f['latitude']
    title = f['acq_date']
    bright.append(br)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(bright)
print(lons)
print(lats)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*f for f in bright],
        'color':bright,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]

my_layout = Layout(title='US Fires - 9/14/2020 through 9/20/2020')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='usfire14to20.html')
