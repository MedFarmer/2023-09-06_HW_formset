from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy

class CreateCourse(CreateView):
    form_class = CourseForm
    template_name = 'course_create.html'
    success_url = reverse_lazy('list')    

class CreateStudent(CreateView):
    form_class = StudentForm
    template_name = 'student_create.html'
    success_url = reverse_lazy('list')

# CBV предсталение на классе
class CourseView(DetailView):
    model = Course
    template_name = 'course.html'    
    
    def get(self, request, **kwargs):
        formset = StudentFormSet()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['formset'] = formset
        return self.render_to_response(context)

    def post(self, request, **kwargs):
        formset = StudentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse_lazy('list'))
        
# Представление на функцие
def create_course(request):
    if request.method == "POST":
        formset = StudentFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect(reverse('list'))
    else:
        formset = StudentFormSet()
    return render(request, "course_form.html", {"formset": formset})
