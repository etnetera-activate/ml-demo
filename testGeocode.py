import googlemaps
import pickle
import json
import plotly.plotly as py
import plotly.graph_objs as go

print "Loading dataset ..."
with open('./data-out/dataset.row.pickle', 'rb') as data:
     locations = pickle.load(data)

gmaps = googlemaps.Client(key='GET-YOUR-OWN-KEY')

for loc in (locations[1], locations[50]):
    print loc
    reverse_geocode_result = gmaps.reverse_geocode((loc['latitude'], loc['longitude']))
    print("\t=>%s" % reverse_geocode_result[0]['formatted_address'])
    #print json.dumps(reverse_geocode_result, indent = 4)
