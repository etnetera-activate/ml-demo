import json
from datetime import datetime
import sys
import pickle

# parse data history from Google takeout
# go to https://takeout.google.com and export location history in JSON format

input_file_name = "./data-in/Historie polohy.json"
print("Parsing %s" % input_file_name)
input_file = open (input_file_name)
json_array = json.load(input_file)
source_locations = json_array["locations"]

locations = []      #ukladani po radcich, kde kazdy radek je json
locations_data = {} #ukladani po sloupcich 
locations_data['timestamp'] = []
locations_data['datetime'] = []
locations_data['year'] = []
locations_data['month'] = []
locations_data['day'] = []
locations_data['weekday'] = []
locations_data['week'] = []
locations_data['hour'] = []
locations_data['latitude'] = []
locations_data['longitude'] = []
locations_data['accuracy'] = []
locations_data['altitude'] = []
locations_data['verticalAccuracy'] = []
locations_data['velocity'] = []
locations_data['locationStrLonLatRounded'] = []

for item in source_locations:
    pct = len(locations) * 100 /len(source_locations) 

    sys.stdout.write("\rPopulating locations: %d %%" % pct)
    sys.stdout.flush()

    store_details = {}
    store_details['timestamp'] = int(item['timestampMs'])
    datetime = datetime.fromtimestamp(store_details['timestamp']/1000)
    store_details['datetime'] = datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
    store_details['year'] = datetime.strftime("%Y")
    store_details['month'] = datetime.strftime("%m")
    store_details['day'] = datetime.strftime("%d")
    store_details['weekday'] = datetime.strftime("%w")
    store_details['week'] = datetime.strftime("%W")
    store_details['hour'] = datetime.strftime("%H")

    store_details['latitude'] = item['latitudeE7'] / 1e7
    store_details['longitude'] = item['longitudeE7'] / 1e7

    store_details['accuracy'] = item['accuracy']
    
    if 'altitude' in item:
        store_details['altitude'] = item['altitude']
    else:
        store_details['altitude'] = 0

    if 'verticalAccuracy' in item:
        store_details['verticalAccuracy'] = item['verticalAccuracy']
    else:
        store_details['verticalAccuracy'] = 0

    if 'velocity' in item:
        store_details['velocity'] = item['velocity']
    else:
        store_details['velocity'] = 0
        
    #rounded location
    store_details['locationStrLonLatRounded'] = "%f:%f" % (round(store_details['longitude'],5)+5e-6,round(store_details['latitude'],5)+5e-6)

    locations.append(store_details)
    
    locations_data['timestamp'].append(store_details['timestamp'])
    locations_data['datetime'].append(store_details['datetime'])
    locations_data['year'].append(store_details['year'])
    locations_data['month'].append(store_details['month'])
    locations_data['day'].append(store_details['day'])
    locations_data['weekday'].append(store_details['weekday'])
    locations_data['week'].append(store_details['week'])
    locations_data['hour'].append(store_details['hour'])
    locations_data['latitude'].append(store_details['latitude'])
    locations_data['longitude'].append(store_details['longitude'])
    locations_data['accuracy'].append(store_details['accuracy'])
    locations_data['altitude'].append(store_details['altitude'])
    locations_data['verticalAccuracy'].append(store_details['verticalAccuracy'])
    locations_data['velocity'].append(store_details['velocity'])
    locations_data['locationStrLonLatRounded'].append(store_details['locationStrLonLatRounded'])


print()
print("Parsed %d entries" % len(locations))
print("Example row: %s" % locations[1])

print("Saving to dataset.csv")
import csv
with open('./data-out/dataset.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerow(['year','month','day','weekday','week','hour','locationStrLonLatRounded', 'longitude','latitude'])
    for row in locations:
        writer.writerow([row['year'],row['month'],row['day'],row['weekday'],row['week'],row['hour'],row['locationStrLonLatRounded'], row['longitude'], row['latitude']])

print("Saving to file dataset.row.pickle")
with open('./data-out/dataset.row.pickle', 'wb') as output:
    pickle.dump(locations, output)

print("Saving to dataset.cols.pickle")
with open('./data-out/dataset.cols.pickle', 'wb') as output:
    pickle.dump(locations_data, output)

print("Done. Locations stored in './data-out' folder.")