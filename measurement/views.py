from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# @api_view(['GET', 'POST'])
# def create_sensor_view(request):
#     sensors = Sensor.objects.all()
#     sensor_list = SensorSerializer(sensors, many=True)
#     return Response(sensor_list.data)

# class CreateSensorView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         sensor_list = SensorSerializer(sensors, many=True)
#         return Response(sensor_list.data)
#
#     def post(self, request):
#         new_sensor = Sensor.objects.create(
#             name=request.data['name'],
#             description=request.data['description'],
#         )
#
#         return Response({'post': model_to_dict(new_sensor)})

class CreateSensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        new_sensor = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description'],
        )

        new_measurement = Measurement.objects.create(
            sensor_id=request.data['sensor_id'],
            temperature=request.data['temperature']
        )

        return Response({'post': model_to_dict(new_sensor)})

class MakeMeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        new_measurement = Measurement.objects.create(
            sensor_id_id=request.data['sensor_id'],
            temperature=request.data['temperature']
        )

        return Response({'post': model_to_dict(new_measurement)})

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
