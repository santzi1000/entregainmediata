from django.urls import path

from procesos import views 

app_name = "procesos"
urlpatterns = [
    path("procesos", view=views.procesos, name="proceso-list"),
    path("proceso/add", view=views.create_procesos, name="proceso-add"),
]