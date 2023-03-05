from django.urls import path

from .ajex_data import print_card
from . import views

urlpatterns = [
     path('print_card/', print_card, name='print_card'),

    # # path('', views.AsyncView.as_view(), name='login' ),
    # path('', views.Home, name='homepage' ),
    # path('print', views.PrintView, name='printpage' ),
    # # path('', views.PostView, name='PostView' ),
    # path('classlist', views.ClassView, name='classlistpage' ),
    # path('classviewfilter/<int:class_id>', views.ClassViewFilter, name='classviewfilterpage' ),
    # path('subjectviewfilter/<int:subject_id>', views.SubjectViewFilter, name='subjectviewfilterpage' ),
    # path('chapterviewfilter/<int:chapter_id>', views.ChapterViewFilter, name='chapterviewfilterpage' ),
    # # path('question_view', views.question_view, name='question_view' ),
    # path('subject_view/<int:class_id>', views.SubView, name='subject_list_page' ),
    # path('chapter_view/<int:subject_id>', views.ChapterViews, name='chapter_list_page' ),
    # path('mcq_view/<int:chapter_id>', views.MCQView, name='mcq_list_page' ),
    # path('mcq_add/<int:chapter_id>', views.MCQAdd, name='mcq_add_page' ),
    # # path('viewmcq', views.chapter_1_views, name='viewpage' ),
    
]
