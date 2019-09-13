from InstaAPP.models import Post
from rest_framework import generics
from api.serializers import PostSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer