from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.convert_html_to_markdown, name='convert_html_to_markdown'),
    path('convert-md/', views.convert_markdown_to_html, name='convert_markdown_to_html'),
]