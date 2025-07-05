from django.urls import path
from .views import FixtureCreateView

urlpatterns = [
    path('/api/admin/fixtures', FixtureCreateView.as_view(), name='fixture-create'),
]
