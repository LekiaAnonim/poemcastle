from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Poem, Collection

# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'index.html'


class MainView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        featured_poems = Poem.objects.filter(add_to_featured_poems=True)
        collections = Collection.objects.all()
        
        context['featured_poems'] = featured_poems
        context['collections'] = collections
        return context
    

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        collections = Collection.objects.all()
        context['collections'] = collections
        return context
    
class CollectionPoemView(ListView):
    model = Poem
    template_name = "collection_poem.html"

    def get_queryset(self):
        collection = get_object_or_404(Collection, slug=self.kwargs.get('slug'))
        return Poem.objects.filter(collection=collection)

    def get_context_data(self, *args, **kwargs):
        context = super(CollectionPoemView,
                        self).get_context_data(**kwargs)
        collection = get_object_or_404(Collection, slug=self.kwargs.get('slug'))
        collection_poems = Poem.objects.filter(collection=collection)

        collections = Collection.objects.all()
        

        context['collections'] = collections
        context['collection'] = collection
        context['collection_poems'] = collection_poems
        return context
    
class PoemListView(ListView):
    model = Poem
    template_name = "poems.html"


    def get_context_data(self, *args, **kwargs):
    
        # Call the base implementation first to get the context
        context = super(PoemListView, self).get_context_data(**kwargs)

        poems = Poem.objects.all()
        collections = Collection.objects.all()
        context['collections'] = collections
        context['poems'] = poems
        return context

class PoemDetail(DetailView):
    model = Poem
    template_name = 'poem_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        collections = Collection.objects.all()
        poems =Poem.objects.all()
        context['poems'] = poems
        context['collections'] = collections
        return context