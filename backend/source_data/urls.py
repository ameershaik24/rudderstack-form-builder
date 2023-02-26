from django.urls import path

from . import views

urlpatterns = [
    path('source_forms', views.SourceFormTemplateList.as_view()),
    path('source_forms/<str:source_type>', views.SourceFormTemplateDetail.as_view()),
]