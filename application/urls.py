from django.urls import path
from .views import sign_up, index, UpdateNoteView, NoteListView, NoteDetailView, AddNoteView, DeleteNoteView, \
    UpdateCategoryView, CategoryListView, CategoryDetailView, AddCategoryView, DeleteCategoryView

urlpatterns = [
    path('', index, name='index'),
    path('registration/sign_up', sign_up, name='sign_up'),
    path('note_list_view', NoteListView.as_view(), name='note_list_view'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note_detail_view'),
    path('add_note/', AddNoteView.as_view(), name='add_note_view'),
    path('note/edit/<int:pk>', UpdateNoteView.as_view(), name='update_note_view'),
    path('note/<int:pk>/delete/', DeleteNoteView.as_view(), name='delete_note_view'),
    path('category_list_view', CategoryListView.as_view(), name='category_list_view'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail_view'),
    path('add_category/', AddCategoryView.as_view(), name='add_category_view'),
    path('category/edit/<int:pk>', UpdateCategoryView.as_view(), name='update_category_view'),
    path('category/<int:pk>/delete/', DeleteCategoryView.as_view(), name='delete_category_view'),
]
