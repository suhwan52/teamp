from django.urls import path
from .views import FixtureCreateView, FixtureUpdateView, FixtureDeleteView, FixtureListView

urlpatterns = [
    path('api/admin/fixtures', FixtureCreateView.as_view(), name='fixture-create'),
    path('api/admin/fixtures/{itemId}', FixtureUpdateView.as_view(), name='fixture-undate'),
    path('api/admin/fixtures/{itemId}', FixtureDeleteView.as_view(), name='fixture-delete'),
    path('api/admin/fixtures/{itemId}', FixtureListView.as_view(), name='fixture-list'),
]
