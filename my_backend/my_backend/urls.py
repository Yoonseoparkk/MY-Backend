"""
URL configuration for my_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# URL 패턴을 정의하는 리스트
urlpatterns = [
    # Django 관리자 사이트에 대한 URL
    path("admin/", admin.site.urls),
    path('free_community/', include('free_community.urls')),
    path('account/', include('account.urls')),
    path('kakao_oauth/', include('kakao_oauth.urls')),
    path('google_oauth/', include('google_oauth.urls')),
    path('naver_oauth/', include('naver_oauth.urls')),
    path('survey/', include('survey.urls')),
    path('user_analysis/', include('user_analysis.urls')),
    path('subscription/', include('subscription.urls')),
    path('purchase/', include('purchase.urls')),
    path('redis_token/', include('redis_token.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('custom_strategy_history/', include('custom_strategy_history.urls')),
    path('viewCount/', include('viewCount.urls')),
    path('free_community_comment/', include('free_community_comment.urls')),
    path('ai_request/', include('ai_request.urls')),
    path('tosspayments/', include('tosspayments.urls')),
    path('smart_content/', include('smart_content.urls')),
    path('growth_blog/', include('growth_blog.urls')),
    path('like_count/', include('like_count.urls')),
    path('keyword_search/', include('keyword_search.urls')),
]
