from django.urls import path

from apps.main_app.views import ItemView


urlpatterns = [
    path('item/', ItemView.as_view()),
]