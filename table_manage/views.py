from rest_framework.decorators import api_view
from table_manage.models import Deviation
import json
from django.db.models import Q
import datetime
from  rest_framework.response import Response
from table_manage.serializers import DeviationDetailSerializer


@api_view(["GET"])
def get_table(request):
    if 'filter' in request.query_params and request.query_params['filter']:
        filter = request.query_params['filter']
        filter = json.loads(filter)
        deviation = Deviation.objects.filter(**filter)
    else:
        deviation = Deviation.objects.all()

    if 'find' in request.query_params and request.query_params['find']:
        query = request.query_params['find']
        try:
            date = datetime.datetime.strptime(query, '%Y-%m-%d %H:%M:%S')
        except:
            date = None
        deviation = deviation.filter(Q(region__icontains=query) |
                                     Q(object_id__icontains=query) |
                                     Q(product_id__icontains=query) |
                                     Q(shift_number__icontains=query) |
                                     Q(shiftbegt=date) |
                                     Q(shiftendt=date) |
                                     Q(shipment=int(query) if query.replace("-","").isdigit() else None) |
                                     Q(reception=int(query) if query.replace("-","").isdigit() else None) |
                                     Q(deviation=int(query) if query.replace("-","").isdigit() else None)
                                     )

    if 'sort' in request.query_params and request.query_params['sort']:
        deviation = deviation.order_by(*request.query_params['sort'].split(','))
    serializer = DeviationDetailSerializer(deviation,many=True)

    return Response(serializer.data)