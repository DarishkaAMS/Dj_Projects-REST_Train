from django.urls import path
from api_basic.views import article_list, article_detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    # path('article', article_list),
    path('article', ArticleAPIView.as_view()),
    # path('article_detail/<int:pk>', article_detail),
    path('article_detail/<int:id>', ArticleDetails.as_view()),
]