from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Staff, Course,Exam,Result
from django.shortcuts import get_object_or_404

# Create your views here.
def main (request):
    return render (request, 'main.html')
def staff (request):
    staff_list = Staff.objects.all()
    context = {'staff_list': staff_list}
    return render(request, 'staff/staff.html', context)
    



def add_staff (request):
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        department= request.POST.get('department')
        course= request.POST.get('course')
        

        if not all([]):
            messages.error(request, "All fields  are required.")
            return redirect("add_course")

        Staff.objects.create(
            username=name,
            email = email,
            course=course,
            department=department
        )
        messages.success(request, "Staff added successfully!")
        return redirect ('staff')
    return render (request, 'staff/add_staff.html')
def update_staff(request, staff_id):
    staff = get_object_or_404(Staff, staff_id=staff_id)

    # Extract options from model class
    departments = [dept[0] for dept in Staff.departmentlist]
    courses = [course[0] for course in Staff.courselist]

    if request.method == 'POST':
        staff.username = request.POST.get('name', staff.username)
        staff.email = request.POST.get('email', staff.email)
        staff.department = request.POST.get('department', staff.department)
        staff.course = request.POST.get('course', staff.course)
        
        staff.save()
        messages.success(request, "Staff updated successfully!")
        return redirect('staff')

    return render(request, 'staff/update_staff.html', {
        'staff': staff,
        'departments': departments,
        'courses': courses
    })

def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, staff_id=staff_id)

    if request.method == "POST":
        staff.delete()
        messages.success(request, f"Staff member '{staff.username}' has been deleted.")
    
    return redirect('staff')# Redirect to staff list page
def course(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'course/course.html', context)


def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        department = request.POST.get('department')
        staff_name = request.POST.get('staff_name')
        staff_email = request.POST.get('staff_email')

        # Check if any field is empty
        if not all([course_name, department, staff_name, staff_email]):
            messages.error(request, "All fields are required.")
            return render(request, 'course/add_course.html')

        # Create a new course
        course = Course.objects.create(
            course_name=course_name,
            department=department,
            staff_name=staff_name,
            staff_email=staff_email
        )
        
        messages.success(request, "Course added successfully!")
        return redirect('course')  # Replace with the actual URL name to list courses

    return render(request, 'course/add_course.html')

def update_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)

    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        department = request.POST.get('department')
        staff_name = request.POST.get('staff_name')
        staff_email = request.POST.get('staff_email')

        # Validate required fields (department can be optional)
        if not all([course_name, staff_name, staff_email]):
            messages.error(request, "Course name, staff name, and email are required.")
            return redirect('update_course', course_id=course_id)

        # Update the course
        course.course_name = course_name
        course.department = department  
        course.staff_name = staff_name
        course.staff_email = staff_email
        course.save()

        messages.success(request, "Course updated successfully!")
        return redirect('course')

    # If GET request, render the form with existing data
    return render(request, 'course/update_course.html', {'course': course})
def delete_course(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, course_id=course_id)
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('course')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('course')

def exam (request):
    exam_list = Exam.objects.all()
    return render (request, 'exam/exam.html',{'exam_list':exam_list})
def add_exam (request):
    if request.method == 'POST':
        exam_name = request.POST.get('exam_name')
        course = request.POST.get('course')
        date = request.POST.get('date')
        duration = request.POST.get('duration')

        # Check if any field is empty
        if not all([exam_name, course, date, duration]):
            messages.error(request, "All fields are required.")
            return render(request, 'course/add_course.html')

        # Create a new course
        exam = Exam.objects.create(
            exam_name=exam_name,
            course=course,
            date=date,
            duration=duration
        )
        
        messages.success(request, "Exam added successfully!")
        return redirect('exam')
    return render (request, 'exam/add_exam.html')
def update_exam (request, exam_id):
    exam = get_object_or_404(Exam, exam_id=exam_id)
    if request.method == 'POST':
        exam_name = request.POST.get('exam_name')
        course = request.POST.get('course')
        date = request.POST.get('date')
        duration = request.POST.get('duration')

        # Check if any field is empty
        if not all([exam_name, course, date, duration]):
            messages.error(request, "All fields are required.")

        exam.exam_name=exam_name
        exam.course=course
        exam.date=date
        exam.duration=duration
        exam.save()
        messages.success(request ,"Exam updated successfully!")
        return redirect('exam')

    return render (request, 'exam/update_exam.html', {'exam':exam})
def delete_exam (request, exam_id):
    if request.method == 'POST':
        exam = get_object_or_404(Exam, exam_id=exam_id)
        exam.delete()
        return redirect('exam')
   
def result (request):
    result_list = Result.objects.all()
    context = {'result_list' : result_list}
    return render (request, 'result/result.html', context)


def add_result(request):
    courses = Course.objects.all()
    exams = Exam.objects.all()

    if request.method == "POST":
        student_id = request.POST['student_id']
        student_name = request.POST['student_name']
        course_id = request.POST['course']
        exam_id = request.POST['exam']
        score = float(request.POST['score'])
        grade = request.POST['grade']

        course = get_object_or_404(Course, id=course_id)
        exam = get_object_or_404(Exam, id=exam_id)

        Result.objects.create(
            student_id=student_id,
            student_name=student_name,
            course=course,
            exam=exam,
            score=score,
            grade=grade,
        )

        return redirect('result')  # redirect to result list

    return render(request, 'result/add_result.html', {'courses': courses, 'exams': exams})




def update_result(request, student_id):
    result = get_object_or_404(Result, student_id=student_id)
    courses = Course.objects.all()
    exams = Exam.objects.all()

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        course_id = request.POST.get('course')
        exam_id = request.POST.get('exam')
        score = request.POST.get('score')
        grade = request.POST.get('grade')

        if not all([student_name, course_id, exam_id, score, grade]):
            messages.error(request, "All fields are required!")
        else:
            course = get_object_or_404(Course, id=course_id)
            exam = get_object_or_404(Exam, id=exam_id)

            result.student_name = student_name
            result.course = course
            result.exam = exam
            result.score = float(score)
            result.grade = grade
            result.save()

            messages.success(request, "Result updated successfully!")
            return redirect('result')

    context = {
        'result': result,
        'courses': courses,
        'exams': exams
    }
    return render(request, 'result/update_result.html', context)


def delete_result (request , student_id):
    if request.method == 'POST':
        result = get_object_or_404(Result, student_id=student_id)
        result.delete()
        messages.success(request, "Result has been deleted")
        return redirect('result')
   