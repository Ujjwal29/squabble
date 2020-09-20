import pickle
import sockett
mydict = {1:"hello"}
mydict = pickle.dumps(mydict)
mydict =
print(mydict)
mydict = pickle.loads(mydict)
print(mydict)
