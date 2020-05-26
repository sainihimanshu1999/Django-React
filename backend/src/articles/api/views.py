from rest_framework.generics import ListAPIViews, RetrieveAPIView
from articles.model import Article
from .serializers import ArticleSerializer


class ArticleListView(ListAPIViews):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
