import json
import inspect


class jsonData:
    def loaddata(datafile):
        testname = inspect.stack()[1][3]
        with open(datafile, 'r') as read:
            datadict = dict(json.load(read))
        return datadict[testname]


