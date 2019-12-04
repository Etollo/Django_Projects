from django.views.generic import View
from django.shortcuts import render

from .forms import TagForm, PostForm, ProjectForm
from .utils import *


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


class ProjectDetail(ObjectDetailIDMixin, View):
    model = Project
    template = 'blog/project_justification_detail.html'
