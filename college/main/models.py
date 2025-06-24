from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Staff(models.Model):
    departmentlist = [
    ('IT & Networking', 'IT & Networking'),
    ('Repair & Maintenance', 'Repair & Maintenance'),
    ('Design & Multimedia', 'Design & Multimedia'),
    ('Accounting & Finance', 'Accounting & Finance'),
    ('Programming', 'Programming'),
    ('Web & App Development', 'Web & App Development'),
    ('English Language & Exam Prep', 'English Language & Exam Prep'),
    ('Marketing & Freelancing', 'Marketing & Freelancing'),
    ('Engineering & Robotics', 'Engineering & Robotics'),
    ('General Computer Skills', 'General Computer Skills')
] 

    courselist = [
    ('Mobile Repairing Course', 'Mobile Repairing Course'),
    ('Laptop Repairing', 'Laptop Repairing'),
    ('Computer Hardware Engineering', 'Computer Hardware Engineering'),
    ('MCSE-MCITP-Networking', 'MCSE-MCITP-Networking'),
    ('CCNA-CCNP', 'CCNA-CCNP'),
    ('CCTV', 'CCTV'),
    ('AutoCAD 20 & 30', 'AutoCAD 20 & 30'),
    ('3D Max', '3D Max'),
    ('Peach Tree, Quick Book, Tally', 'Peach Tree, Quick Book, Tally'),
    ('Web Designing & Development', 'Web Designing & Development'),
    ('MERN Stack', 'MERN Stack'),
    ('Android Application Course', 'Android Application Course'),
    ('Cloud Computing', 'Cloud Computing'),
    ('Bobotics', 'Bobotics'),
    ('Full Stack Graphic Designing', 'Full Stack Graphic Designing'),
    ('Adobe Illustrator', 'Adobe Illustrator'),
    ('Adobe Premiere Pro', 'Adobe Premiere Pro'),
    ('Spoken English', 'Spoken English'),
    ('IELTS', 'IELTS'),
    ('AT (English Spouse Visa Course)', 'AT (English Spouse Visa Course)'),
    ('Computer Course for Beginners', 'Computer Course for Beginners'),
    ('Computer Programming', 'Computer Programming'),
    ('Visual Basic', 'Visual Basic'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('Digital Marketing', 'Digital Marketing'),
    ('Freelancing Course', 'Freelancing Course'),
    ('SEO (Search Engine Optimization)', 'SEO (Search Engine Optimization)')
]



    staff_id = models.CharField(max_length=20, unique=True, blank=True,null=True)    
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=200 , choices=departmentlist, null=True)
    course = models.CharField(max_length=200 , choices=courselist,  null=True)
    created_at = models.DateTimeField(default=timezone.now)  # New field
    

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
    # First save to get an ID (if new instance)
        super().save(*args, **kwargs)
    
    # Then generate Staff_ID if it doesn't exist
        if not self.staff_id:
            self.staff_id = f"STAf-{str(self.id).zfill(4)}"
            # Save again but only update the employee_number field
            super().save(update_fields=['staff_id'])

class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    course_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100, blank=True, null=True)
    staff_name = models.CharField(max_length=200)
    staff_email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.course_name

    def save(self, *args, **kwargs):
    # First save to get an ID (if new instance)
        super().save(*args, **kwargs)
        if not self.course_id:
                self.course_id = f"CR-{str(self.id).zfill(4)}"
              
                super().save(update_fields=['course_id'])

class Exam(models.Model):
    exam_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    exam_name = models.CharField(max_length=200)
    course = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()                  
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.exam_name

    def save(self, *args, **kwargs):
    # First save to get an ID (if new instance)
        super().save(*args, **kwargs)
        if not self.exam_id:
                self.exam_id = f"EX-{str(self.id).zfill(4)}"
              
                super().save(update_fields=['exam_id'])


class Result(models.Model):
     student_id = models.IntegerField()
     student_name = models.CharField(max_length=120)
     course = models.ForeignKey(Course, on_delete=models.CASCADE)
     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
     score = models.FloatField()
     grade = models.CharField(max_length=2)
     created_at = models.DateTimeField(default=timezone.now)

     def __str__(self):
          return self.student_name
     
    

