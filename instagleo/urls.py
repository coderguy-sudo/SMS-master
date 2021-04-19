from django.urls import path

from instagleo.views import Students, AddStudent, UpdateStudent, DeleteStudent, Courses, AddStudentCourse, UpdateCourse, \
    GPACalculator, CalculateGPA

urlpatterns = [
    # students
    path('', Students.as_view(), name='students'),
    path('student/add', AddStudent.as_view(), name='add_student'),
    path('update/student/<pk>', UpdateStudent.as_view(), name='update_student'),
    path('delete/student/<pk>', DeleteStudent.as_view(), name='delete_student'),

    # courses
    path('courses', Courses.as_view(), name='courses'),
    path('course/add', AddStudentCourse.as_view(), name='add_student_course'),
    path('update/course/<pk>/<course_id>', UpdateCourse.as_view(), name='update_student_course'),

    # gpa
    path('gpa', GPACalculator.as_view(), name='gpa'),
    path('calculate/', CalculateGPA.as_view(), name='calculate'),
]
