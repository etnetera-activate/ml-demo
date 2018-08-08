import matplotlib.pyplot as plt
import pickle

print "Loading dataset ..."
with open('dataset.cols.pickle', 'rb') as data:
     locations = pickle.load(data)

plt.plot(locations['latitude'],locations['longitude'],'.', color="black")

plt.show()



