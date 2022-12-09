from django.views.generic import ListView, DetailView
from .models import Author, Category, Posts, Comment
from datetime import datetime

class AuthorsList(ListView):
    model = Author
    ordering = 'name'
    template_name = 'authors.html'
    context_object_name = 'authors'

class CategorysList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'categorys.html'
    context_object_name = 'categorys'

class PostsList(ListView):
    model = Posts
    ordering = 'author'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
class CommentsList(ListView):
    model = Comment
    ordering = 'posts'
    template_name = 'comments.html'
    context_object_name = 'comments'

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Posts
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'