from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from instagleo.forms import AddStudentForm, UpdateStudentForm, AddCourseForm, UpdateCourseForm
from instagleo.models import Student, Course
from instagleo.utils import calculate_gpa


class Students(TemplateView):
    template_name = 'students.html'

    def get_context_data(self, **kwargs):
        students = Student.objects.all()
        context = {"students": students}
        return context


class AddStudent(FormView):
    form_class = AddStudentForm
    success_url = reverse_lazy('students')
    template_name = 'add_student.html'

    def form_valid(self, form):
        form.save()
        return super(AddStudent, self).form_valid(form)


class UpdateStudent(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students')
    template_name = 'update_student.html'

    def get_object(self, queryset=None):
        student = Student.objects.get(id=self.kwargs['pk'])
        return student


class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('students')

    def get(self, request, *args, **kwargs):
        student = Student.objects.filter(id=self.kwargs['pk'])
        if student:
            return self.post(request, *args, **kwargs)
        return Http404


class Courses(TemplateView):
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        students = Student.objects.all()
        context = {"students": students}
        return context


class AddStudentCourse(FormView):
    form_class = AddCourseForm
    success_url = reverse_lazy('courses')
    template_name = 'add_courses.html'

    def form_valid(self, form):
        form.save()
        return super(AddStudentCourse, self).form_valid(form)


class UpdateCourse(FormView):
    model = Student
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses')
    template_name = 'update_course.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateCourse, self).get_form_kwargs()
        course = Course.objects.get(id=self.kwargs['course_id'])
        student = Student.objects.get(id=self.kwargs['pk'])
        kwargs.update({'course': course, 'student': student})
        return kwargs

    def form_valid(self, form):
        student = Student.objects.get(id=self.kwargs['pk'])
        form.save(student)
        return super(UpdateCourse, self).form_valid(form)


class GPACalculator(TemplateView):
    template_name = 'calculate_gpa.html'


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class CalculateGPA(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def post(self, request, *args, **kwargs):
        roll_no = request.POST.get('roll_no')
        course_no = request.POST.get('course_no', None)
        try:
            student = Student.objects.get(roll_no=roll_no)
            if course_no:
                try:
                    course_name = Course.objects.get(course_no=course_no).name
                except:
                    return Response("Course number is wrong.")
                marks = student.marks.get(course_name)
                gpa = calculate_gpa(float(marks))
                return Response(student.name + ' cgpa in ' + course_name + ' is: ' + gpa + '.')
            else:
                mark_list = []
                for key, mark in student.marks.items():
                    mark_list.append(float(mark))
                if mark_list:
                    marks = sum(mark_list)/len(mark_list)
                    gpa = calculate_gpa(marks)
                    return Response(student.name + ' cgpa in all subject is: ' + gpa + '.')
                return Response('This student does not have any marks entered.')
        except:
            return Response("Student does not exists.")
