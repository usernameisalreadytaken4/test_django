from django.contrib import admin
from django.urls import path, include
import tg_bot_test.urls as tg_bot_test_urls
from test_django.views import IndexTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('', include(tg_bot_test_urls), name='tg_bot'),
]
