from django.shortcuts import render, get_object_or_404
from .models import MCQ,Class,Subject,Chapter,Articless,QuillPost
from .form import AddMCQForm, add_mcq_form,add_new_class,add_subject_name,add_chapter_name,MyForm
from django.contrib.sessions.models import Session



from django.http import HttpResponse
from django.views import View

class AsyncView(View):
    def get(self,request):

        return render(request,'login.html',{})



def PostView(request):
    form=AddMCQForm()

    if request.method =="POST":
        
    
        form = AddMCQForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            content=form.cleaned_data['mcq_question']

            print(title)
            print(content)
            form=MyForm()

            add_data=Articless(title=title,content=content)
            add_data.save()
    return render(request,'postView.html',{
        'form':form,
        'post':Articless.objects.all()
        })

# Create your views here.
def chapter_1_views(request):
    if request.method=="POST":
        p= request.POST.get('mcq')
        print(p)
    
    chapter_1_value = MCQ.objects.all
    context = {
        'value':chapter_1_value,

    }
    return render(request,'chapter_1.html', context)

def ClassView(request):
    if request.method =="POST":
    
        form = add_new_class(request.POST)
        if form.is_valid():
            class_name=form.cleaned_data['class_name']
            add_class=Class(class_name=class_name)
            add_class.save()
            form = add_new_class()
            print(f"Successfully Added {class_name}")
    else:
        form = add_new_class()
    class_name=Class.objects.all
    print(class_name)
    return render(request,'index_view.html',{
        "class_name":class_name,
        "form":form}
        )



def SubView(request,class_id):
    class_obj = Class.objects.get(id=class_id)
    if request.method =="POST":
    
        form = add_subject_name(request.POST)
        if form.is_valid():
            subject_name=form.cleaned_data['subject_name']
            add_subject=Subject(subject_name=subject_name, class_name=class_obj)
            add_subject.save()
            form = add_subject_name()
            print(f"Successfully Add {add_subject}")
    else:
        form = add_subject_name()
    subject_name=Subject.objects.filter(class_name=class_id)
    # subject_name=get_object_or_404(Subject, id=1)
    print(subject_name)
    return render(request,'subject_view.html',{
        "subject_name":subject_name,
        "form":form
        }
        )

def ChapterViews(request,subject_id):
    # class_obj = Class.objects.get(id=class_id)
    subject_obj = Subject.objects.get(id=subject_id)
    if request.method =="POST":
    
        form = add_chapter_name(request.POST)
        if form.is_valid():
            chapter_name=form.cleaned_data['chapter_name']
            add_chapter=Chapter(chapter_name=chapter_name, subject_name=subject_obj)
            add_chapter.save()
            form = add_chapter_name()
            print(f"Successfully Add {add_chapter}")
    else:
        form = add_chapter_name()
    chapter_name=Chapter.objects.filter(subject_name=subject_obj)
    # subject_name=get_object_or_404(Subject, id=1)
    print(chapter_name)
    return render(request,'chapter_view.html',{
        "chapter_name":chapter_name,
        "form":form
        }
        )

def MCQAdd(request, chapter_id):
    chapter_obj=Chapter.objects.get(id=chapter_id)
    if request.method =="POST":
        form = add_mcq_form(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            mcq_question=form.cleaned_data['mcq_question']
            option_a=form.cleaned_data['option_a']
            option_b=form.cleaned_data['option_b']
            option_c=form.cleaned_data['option_c']
            option_d=form.cleaned_data['option_d']
            print(mcq_question)
            print(option_a)
            add_mcq_=MCQ(
    
            chapter_field=chapter_obj,
            question_text=mcq_question,
            options_A=option_a,
            options_B=option_b,
            options_C=option_c,
            options_D=option_d,
            answer="N/A",
            status="N/A"

            
            )
            add_mcq_.save()

            form = add_mcq_form()
    else:
        form = add_mcq_form()
    chapter_obj=Chapter.objects.get(id=chapter_id)

    mcq = MCQ.objects.filter(chapter_field=chapter_obj)


    return render(request,'add_mcq.html',{'form':form,"mcq":mcq})

def MCQView(request,chapter_id):
    chapter_obj=Chapter.objects.get(id=chapter_id)

    mcq = MCQ.objects.filter(chapter_field=chapter_obj)
    context = {
        'value':mcq,

    }
    return render(request,'question_view.html', context)

def cart_handale(request):
    if request.method == "GET":
        remove_mcq_id=request.GET.get("remove_mcq")
        mcq_id=request.GET.get("mcq")
        if remove_mcq_id != None and remove_mcq_id in request.session.get("cart"):
            request.session['cart'].remove(remove_mcq_id)
            request.session.save()

        if 'cart' not in request.session:
            request.session['cart'] = []
        if mcq_id != None:
            if mcq_id not in request.session.get("cart"):
                request.session['cart'].append(mcq_id)
            request.session.save()
    question_ids = request.session.get("cart")

    if question_ids is None:
        questions=None
    else:
        questions = MCQ.objects.filter(id__in=question_ids)

    # if question_ids != None:

    #     questions = MCQ.objects.filter(id__in=question_ids)
    # else:
    #     questions=None


    return questions,question_ids

def Home(request):
    questions,question_ids=cart_handale(request)
    mcq=MCQ.objects.all()
    context = {
        "question_ids":question_ids,
        "questions":questions,
        'value':mcq,
        'classlist':Class.objects.all(),
        'subjectlist':Subject.objects.all(),
        'chapterlist':Chapter.objects.all(),

    }
    return render(request,'question_view.html', context)


def PrintView(request):
    questions,question_ids=cart_handale(request)
    mcq=MCQ.objects.all()
    context = {
        "question_ids":question_ids,
        "questions":questions,
        'value':mcq,
        'classlist':Class.objects.all(),
        'subjectlist':Subject.objects.all(),
        'chapterlist':Chapter.objects.all(),

    }
    return render(request,'print_view.html', context)

def ClassViewFilter(request,class_id):
    questions,question_ids=cart_handale(request)
    class_obj=Class.objects.filter(id=class_id)
    mcq=[]
    for sub_obj in class_obj:
        for chap_obj in Subject.objects.filter(class_name=sub_obj):
            for mcq_ in Chapter.objects.filter(subject_name=chap_obj):
                mcq.extend(iter(MCQ.objects.filter(chapter_field=mcq_)))

    # for sub_obj in class_obj:
    #     for chap_obj in Subject.objects.filter(class_name=sub_obj):
    #         for mcq_ in Chapter.objects.filter(subject_name=chap_obj):
    #             for m in MCQ.objects.filter(chapter_field=mcq_):
    #                 mcq.append(m)


    context = {
        "question_ids":question_ids,
        "questions":questions,
        'value':mcq,
        'classlist':Class.objects.all(),
        'subjectlist':Subject.objects.all(),
        'chapterlist':Chapter.objects.all(),

    }
    return render(request,'question_view.html', context)


def SubjectViewFilter(request,subject_id):
    questions,question_ids=cart_handale(request)
    subject_obj=Subject.objects.filter(id=subject_id)
    mcq=[]
    for chap_obj in subject_obj:
        for mcq_ in Chapter.objects.filter(subject_name=chap_obj):
            for m in MCQ.objects.filter(chapter_field=mcq_):
                mcq.append(m)

    context = {
        "question_ids":question_ids,
        "questions":questions,
        'value':mcq,
        'classlist':Class.objects.all(),
        'subjectlist':Subject.objects.all(),
        'chapterlist':Chapter.objects.all(),

    }
    return render(request,'question_view.html', context)

def ChapterViewFilter(request,chapter_id):
    questions,question_ids=cart_handale(request)
    chapter_obj=Chapter.objects.filter(id=chapter_id)
    mcq=[]
    for mcq_ in chapter_obj:
        for m in MCQ.objects.filter(chapter_field=mcq_):
            mcq.append(m)

    context = {
        "question_ids":question_ids,
        "questions":questions,
        'value':mcq,
        'classlist':Class.objects.all(),
        'subjectlist':Subject.objects.all(),
        'chapterlist':Chapter.objects.all(),

    }
    return render(request,'question_view.html', context)
