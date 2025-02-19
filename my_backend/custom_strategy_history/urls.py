from django.urls import path, include
from rest_framework.routers import DefaultRouter

from custom_strategy_history.controller.views import CustomStrategyHistoryView

router = DefaultRouter()
router.register(r'custom_strategy_history', CustomStrategyHistoryView, basename='custom_strategy_history')

urlpatterns = [
    path('', include(router.urls)),
    path('save', CustomStrategyHistoryView.as_view({'post': 'saveCustomStrategyResult'}), name='save-custom-strategy-result'),
    path('read-latest', CustomStrategyHistoryView.as_view({'post': 'readLatestCustomStrategyResult'}), name='read-latest-custom-strategy-result'),
    path('read/<int:pk>', CustomStrategyHistoryView.as_view({'post': 'readCustomStrategyResult'}), name='read-custom-strategy'),
]