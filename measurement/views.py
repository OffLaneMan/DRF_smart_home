# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from measurement.models import Measurement, Sensor
from measurement.serializers import Measurement2Serializer, MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(APIView):
    def get(self, request):
        sens = Sensor.objects.all()
        ser = SensorDetailSerializer(sens, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SensorDetailSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class RetrieveUpdateAPIView(APIView):
    def patch(self, request, pk):
        sens = Sensor.objects.get(pk=pk)
        ser = SensorDetailSerializer(sens, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def get(self, request, pk):
        sens = Sensor.objects.get(pk=pk)
        ser = SensorDetailSerializer(sens)
        return Response(ser.data)


class CreateAPIView(APIView):
    def post(self, request):
        ser = Measurement2Serializer(data=request.data)
        if ser.is_valid():
            ser.save()
            sens = Sensor.objects.get(id=request.data['sensor'])
            ser = SensorDetailSerializer(
                sens, partial=True)
            return Response(ser.data)
        return Response(ser.errors)
