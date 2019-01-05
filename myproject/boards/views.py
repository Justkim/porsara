
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Question,Answer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewQuestionForm,NewAnswerForm
import datetime

from django.shortcuts import get_object_or_404, render

def home(request):
    questions = Question.objects.all()
    return render(request,'home.html', {'questions':questions})
from django.views.generic import ListView


def question_detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers=Answer.objects.filter(parent_question=question)


    return render(request,'question_detail.html', {'question': question,'answers':answers})




def add_question(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        if request.method == 'POST':
            form=NewQuestionForm(request.POST)
            if form.is_valid():

                question=form.save(commit=False)
                question.created_by=user
                question.updated_by=user
                question.created_at=datetime.datetime.now()
                question.save()
                return redirect('question_detail', question_id=question.pk)
        else:
            form = NewQuestionForm()

        return render(request, 'new_question.html', {'form': form})
    else:
        return redirect('login')

def add_answer(request,question_id1):
        user = request.user
        print(user)
        if user.is_authenticated:
            if request.method == 'POST':
                form = NewAnswerForm(request.POST)
                if form.is_valid():
                    answer = form.save(commit=False)
                    answer.created_by = user
                    answer.created_at = datetime.datetime.now()
                    answer.parent_question=get_object_or_404(Question, pk=question_id1)
                    answer.save()
                    return redirect('question_detail', question_id=question_id1)
            else:
                form = NewAnswerForm()

            return render(request, 'new_answer.html', {'form': form})
        else:
            return redirect('login')


class search(ListView):
    template_name = 'search_result.html'
    context_object_name = 'result'
    def get_queryset(self):
        name = self.request.GET.get('name_q')
        # name=request.GET.get('name_res')
        print('NAMEEEEEEEE', name)
        result=Question.objects.filter(title__contains=name)
        return result




	

# Create your views here.
