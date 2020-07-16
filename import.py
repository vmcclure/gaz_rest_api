import csv, os, sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'gaz_rest_api.settings'

import django

django.setup()

from table_manage.models import Deviation
import datetime

data = csv.reader(open('task5.csv'),delimiter=';')
format = '%Y-%m-%d %H:%M:%S'

for line in data:
    if line[0] == '':
        continue
    deviation = Deviation()
    deviation.region = line[6]
    deviation.object_id = line[7]
    deviation.product_id = line[10]
    deviation.shift_number =line[1]
    deviation.shiftbegt =  datetime.datetime.strptime(line[8], format)
    deviation.shiftendt = datetime.datetime.strptime(line[9], format)
    deviation.reception = int(line[2][:-2])
    deviation.shipment = int(line[3][:-2]) if line[3] != '' else 0
    deviation.deviation = line[12][:-2]
    deviation.version = line[11]
    deviation.save()