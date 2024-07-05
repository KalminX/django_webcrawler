from django.urls import path
from . import views

urlpatterns = [
    path('crawl/', views.crawl_view, name='crawl_view'),
    path('crawl/result/', views.crawl_result_view,
         name='crawl_result_view')
]
