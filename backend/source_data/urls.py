from django.urls import path

from . import views

urlpatterns = [
    path('get_source_types', views.get_source_types),
    path('source_forms', views.SourceFormTemplateList.as_view()),
    path('source_forms/<str:type>', views.SourceFormTemplateDetail.as_view()),
    path('sources', views.SourceList.as_view()),
    path('sources/<int:pk>', views.SourceDetail.as_view()),
]