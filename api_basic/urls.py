from django.urls import path
from api_basic.views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article', article_list),
    path('article', ArticleAPIView.as_view()),

    # path('article_detail/<int:pk>', article_detail),
    path('article_detail/<int:id>', ArticleDetails.as_view()),

    path('generic/article/<int:id>', GenericAPIView.as_view()),
]