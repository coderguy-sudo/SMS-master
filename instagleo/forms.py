from django import forms
from django.forms import Select

from instagleo.models import Student, Course


class AddStudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name',
        }
    ))
    roll_no = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Roll Number',
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }
    ))

    class Meta:
        model = Student
        fields = ('name', 'roll_no', 'email')

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = False
        self.fields['roll_no'].label = False
        self.fields['email'].label = False

    def save(self, commit=True):
        student = super(AddStudentForm, self).save(commit=False)
        student.name = self.cleaned_data['name']
        student.roll_no = self.cleaned_data['roll_no']
        student.email = self.cleaned_data['email']
        student.save()
        return student


class UpdateStudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name',
        }
    ))
    roll_no = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Roll Number',
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }
    ))

    class Meta:
        model = Student
        fields = ('name', 'roll_no', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateStudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = False
        self.fields['roll_no'].label = False
        self.fields['email'].label = False


class AddCourseForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=Select(attrs={'class': 'form-control'}),
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=Select(attrs={'class': 'form-control'}),
    )
    marks = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Marks',
        }
    ), required=False)

    def __init__(self, *args, **kwargs):
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.fields['marks'].label = False

    def clean(self):
        student_name = self.cleaned_data['student']
        course_name = self.cleaned_data['course']
        courses = Student.objects.get(name=student_name).courses.all()
        for course in courses:
            if course.name == course_name.name:
                raise forms.ValidationError("This student already have this course")
        return self.cleaned_data

    def save(self):
        student = self.cleaned_data['student']
        course = self.cleaned_data['course']
        marks = self.cleaned_data['marks']
        if marks:
            if bool(student.marks):
                student.marks.update({course.name: marks})
            else:
                student.marks = {course.name: marks}
        student.courses.add(course)
        student.save()
        return student


class UpdateCourseForm(forms.Form):
    marks = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Marks',
        }
    ))

    def __init__(self, *args, **kwargs):
        self.course = kwargs.pop("course")
        self.student = kwargs.pop("student")
        super(UpdateCourseForm, self).__init__(*args, **kwargs)
        self.fields['marks'].label = False

    def save(self, student):
        marks = self.cleaned_data['marks']
        if marks:
            if bool(student.marks):
                student.marks.update({self.course.name: marks})
            else:
                student.marks = {self.course.name: marks}
        student.save()
        return student
