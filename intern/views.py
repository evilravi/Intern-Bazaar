from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Q
from .models import Internship, Student , Post
from django.views.generic import CreateView,DeleteView,UpdateView, View, ListView , DetailView
from django.core.urlresolvers import reverse_lazy
from .forms import Userform


def index(request):
    all_internship = Internship.objects.all()
    return render(request, 'intern/index.html', {'all_internship': all_internship})

class apply(CreateView):
    model = Student
    fields = ['email_id', 'resume_file']
    template_name = 'intern/apply.html'


def contact(request):
    return render(request, 'intern/contact.html')


def new(request):
    ur_internship = Internship.objects.filter(user=request.user)
    return render(request, 'intern/ur_index.html', {'ur_internship': ur_internship})


class detail(DetailView):
    model = Internship
    template_name = 'intern/detail.html'

class ap_detail(DetailView):
    model = Internship
    template_name = 'intern/in_detail.html'


class create_internship(CreateView):
    model = Internship
    fields = ['company', 'company_logo', 'Post', 'about', 'role', 'time', 'benefits', 'skills']

class update_internship(UpdateView):
    model = Internship
    fields = ['company', 'company_logo', 'Post', 'about', 'role', 'time', 'benefits', 'skills']

class delete_internship(DeleteView):
    model = Internship
    success_url = reverse_lazy('intern:index')

class UserFormView(View):
    form_class = Userform
    template_name = 'intern/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit= False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username , password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('intern:index')
        return render(request, self.template_name, {'form': form})

def base(request):
    all_internship = Internship.objects.all()
    return render(request, 'intern/base.html', {'all_internship': all_internship})

def internship(request):
    all_internship = Internship.objects.all()
    return render(request, 'intern/internship.html', {'all_internship': all_internship})

def home(request):
    all_internship = Internship.objects.all()
    return render(request, 'intern/home.html', {'all_internship': all_internship})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                internship = Internship.objects.filter(user=request.user)
                return render(request, 'intern/base.html', {'internship': internship})
            else:
                return render(request, 'intern/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'intern/login.html', {'error_message': 'Invalid login'})
    return render(request, 'intern/login.html')