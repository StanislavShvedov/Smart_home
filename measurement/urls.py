from django.urls import path
from measurement.views import CreateSensorView, SensorView, MakeMeasurementView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors', CreateSensorView.as_view()),
    path('measurement', MakeMeasurementView.as_view()),
    path('sensor/<pk>', SensorView.as_view()),
]
