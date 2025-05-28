

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from common_App.models import Student, Courses, OngoingCourses
from django.contrib import messages

@staff_member_required
def admin_dashboard(request):
    if request.method == 'POST':
        # Handle course assignment
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        
        try:
            student = Student.objects.get(id=student_id)
            course = OngoingCourses.objects.get(id=course_id)
            student.Enrolled_Course.add(course)
            messages.success(request, f'Course assigned to {student.name} successfully!')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        
        return redirect('admin_dashboard')
    
    # Get all data
    students = Student.objects.all().prefetch_related('Enrolled_Course')
    courses = Courses.objects.all()
    ongoing_courses = OngoingCourses.objects.all().select_related('courseID', 'instractor', 'location')
    
    context = {
        'students': students,
        'courses': courses,
        'ongoing_courses': ongoing_courses,
    }
    return render(request, 'admin_dashboard.html', context)


def home(request):
    return render (request,'index.html')


