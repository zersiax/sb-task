from django.views.generic.base import TemplateView

from books.models import Book

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Book.objects.all()[:5]
        return context
        