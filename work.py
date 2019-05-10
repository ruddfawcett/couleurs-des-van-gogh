import csv

info = open('./data/van-gogh-works-colors.csv')

for row in csv.DictReader(info):
    print(row)
