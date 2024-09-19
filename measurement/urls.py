from django.urls import path

from measurement.views import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<int:pk>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', CreateAPIView.as_view()),
]
