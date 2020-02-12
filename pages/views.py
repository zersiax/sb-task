from django.views.generic.base import TemplateView
from django.db.models import Count,Subquery, OuterRef
from books.models import Book
import operator

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Book.objects.order_by('-id')[:5]
        context['top_rating_books'] = Book.objects.order_by('-rating')[:5]
        context['top_count_books'] =[]
        with_this_name =Book.objects.values('title').annotate(c=Count('title')).order_by('-c')[:5]
        for item in with_this_name:
            context['top_count_books'].append(Book.objects.filter(title = item['title']).first())
        return context
        