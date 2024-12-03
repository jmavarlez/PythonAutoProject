import csv
import json

class csvtojson:
    def __init__(self):
        self.ballclub = []

    def fetchcsvdata(self, file):
        self.ballclub = list(csv.DictReader(file, fieldnames=['club', 'city', 'country'], lineterminator='\n'))
        file.close()
        return(self.ballclub)

    def converttojson(self, ballclubdata, file):
        json.dump(ballclubdata,file)
        file.close()

ctj = csvtojson()
csvfile = open('csv_file.csv', 'r')
jsonfile = open('json_file.json', 'w')
ctj.converttojson(ctj.fetchcsvdata(csvfile), jsonfile)



