from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import SignUpForm, NoteForm, CategoryForm
from .models import Note, Category


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


class NoteListView(ListView):
    model = Note
    template_name = 'note_list_view.html'
    paginate_by = 4

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteListView, self).dispatch(*args, **kwargs)


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail_view.html'
    paginate_by = 6

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteDetailView, self).dispatch(*args, **kwargs)


class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'add_note_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddNoteView, self).dispatch(*args, **kwargs)


class UpdateNoteView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'update_note_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateNoteView, self).dispatch(*args, **kwargs)


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'delete_note_view.html'
    success_url = reverse_lazy('note_list_view')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteNoteView, self).dispatch(*args, **kwargs)


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list_view.html'
    paginate_by = 6

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryListView, self).dispatch(*args, **kwargs)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryDetailView, self).dispatch(*args, **kwargs)


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddCategoryView, self).dispatch(*args, **kwargs)


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'update_category_view.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateCategoryView, self).dispatch(*args, **kwargs)


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category_view.html'
    success_url = reverse_lazy('category_list_view')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteCategoryView, self).dispatch(*args, **kwargs)
