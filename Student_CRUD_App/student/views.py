from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin

from django.contrib import messages
from django.db.models import Sum
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from .models import Student
from .forms import StudentForm
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request,'student/home.html')



class StudentCreateView(CreateView):
    form_class=StudentForm
    model=Student
    context_object_name='model'
    template_name='student/student_create_view.html'
    success_url=reverse_lazy('list')

class StudentListView(ListView):
   
    model=Student
    context_object_name='models'
    template_name='student/student_list_view.html'
    
   
    paginate_by = 2

    def get_queryset(self):
        return Student.objects.order_by('-id')

class StudentDetailView(DetailView):
    form_class=StudentForm
    model=Student
    context_object_name='object'
    template_name='student/student_detail_view.html'
    

class StudentUpdateView(UpdateView):
    form_class=StudentForm
    model=Student
    context_object_name='object'
    template_name='student/student_update_view.html'
    success_url=reverse_lazy('list')

class StudentDeleteView(DeleteView):
   
    model=Student
    context_object_name='model'
    template_name='student/student_delete_view.html'
    success_url=reverse_lazy('list')
    


def search(request):
    query = request.GET['query']
    print(type(query))


    #data = query.split()
    data = query
    print(len(data))
    if( len(data) == 0):
        return redirect('list')
    else:
                a=data
                # Searching for It
                qs5 =Student.objects.filter(id__iexact=a).distinct()
                qs6 =Student.objects.filter(id__exact=a).distinct()

                qs7 =Student.objects.all().filter(id__contains=a)
                qs8 =Student.objects.select_related().filter(id__contains=a).distinct()
                qs9 =Student.objects.filter(id__startswith=a).distinct()
                qs10 =Student.objects.filter(id__endswith=a).distinct()
                qs11 =Student.objects.filter(id__istartswith=a).distinct()
                qs12 =Student.objects.all().filter(id__icontains=a)
                qs13 =Student.objects.filter(id__iendswith=a).distinct()




                files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)


                # word variable will be shown in html when user click on search button
                word="Searched Result :"
                print("Result")

                print(res)
                files = res




                page = request.GET.get('page', 1)
                paginator = Paginator(files, 10)
                try:
                    files = paginator.page(page)
                except PageNotAnInteger:
                    files = paginator.page(1)
                except EmptyPage:
                    files = paginator.page(paginator.num_pages)
   


                if files:
                    return render(request,'student/result.html',{'files':files,'word':word})
                return render(request,'student/result.html',{'files':files,'word':word})




