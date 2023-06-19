from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import reverse

app_name = 'ticketSummary'
urlpatterns = [
    path('', views.home, name='home'),
    path('show-text/', views.show_text, name='show_text'),
    path('export_to_word/<str:ticketId>/<str:problem>/<str:solution>/',
         views.export_to_word, name='export-to-word'),
    path('names/', views.dropdown_view, name='name-list'),
    path('tickets/', views.tickets_view, name='tickets-table'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
