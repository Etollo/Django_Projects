from django.db.models import Q
from django.views.generic import View, ListView
from django.shortcuts import render
from pip._vendor.distlib.compat import raw_input
from pip._vendor.msgpack.fallback import xrange

from .forms import TagForm, PostForm, ProjectForm
from .utils import *

import random as random_number


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def project_justification_list(request):
    project_justification = Project.objects.all()
    return render(request, 'blog/project_justification_list.html',
                  context={'project_justification': project_justification})


class ProjectJustificationCreate(ObjectCreateMixin, View):
    model_form = ProjectForm
    template = 'blog/project_justification_create_form.html'


# Метод Монте Карло
def monte_carlo(n):
    N = n
    M = 0
    for i in xrange(N):
        six = 0
        r1 = random_number.randint(1, 6)
        if r1 == 6:
            six += 1
        if six >= 2:
            M += 1

    p = float(M) / N
    return p


class ProjectJustificationDetail(ObjectDetailIDMixin, View):
    model = Project
    template = 'blog/project_justification_detail.html'


class SearchResultsView(ListView):
    model = News
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(
            Q(news__startswith=query) | Q(news__icontains=query)
        )
        return object_list


def news_list(request):
    news = News.objects.all()
    return render(request, 'blog/news_list.html', context={'news': news})


class NewsDetail(View):
    model = News
    template = 'blog/news_detail.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        return render(request, self.template, context={self.model.__name__.lower(): obj})
