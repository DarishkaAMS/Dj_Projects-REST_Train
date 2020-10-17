from django.urls import path, include
from api_basic.views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, \
    ModelArticleViewSet
#GenericArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ModelArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),

    # path('article', article_list),
    path('article', ArticleAPIView.as_view()),

    # path('article_detail/<int:pk>', article_detail),
    path('article_detail/<int:id>', ArticleDetails.as_view()),

    path('generic/article/<int:id>', GenericAPIView.as_view()),
]