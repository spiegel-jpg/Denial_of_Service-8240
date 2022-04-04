from urllib.parse import urlparse
import csv
with open('access.csv') as cf:
    r = csv.reader(cf,delimiter=',')

    with open('get.csv', 'w') as f:
        writer = csv.writer(f,delimiter=',')
        cr = iter(r)
        next(cr) #skipping first line of csv
        for row in cr:
            row[2]=urlparse(row[2]).path
            writer.writerow(row)
