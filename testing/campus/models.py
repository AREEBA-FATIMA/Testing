from django.db import models

class Campus(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("temporary_closed", "Temporary Closed"),
    ]

    # General Information
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    governing_body = models.CharField(max_length=255, blank=True, null=True)

    # About Campus
    registration_no = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    grades_offered = models.CharField(max_length=255, help_text="e.g. Grade 1 - Grade 12")
    languages_of_instruction = models.CharField(max_length=255, help_text="e.g. English, Urdu")
    academic_year_start = models.DateField()
    academic_year_end = models.DateField()
    capacity = models.PositiveIntegerField(help_text="Maximum student capacity")

    # Academic Structure
    classes_per_grade = models.PositiveIntegerField(default=0)
    avg_class_size = models.PositiveIntegerField(default=0)
    num_students = models.PositiveIntegerField(default=0)
    num_teachers = models.PositiveIntegerField(default=0)
    num_rooms = models.PositiveIntegerField(default=0)
    total_classrooms = models.PositiveIntegerField(default=0)

    # Labs & Facilities
    science_labs = models.JSONField(default=dict, blank=True, null=True,
        help_text="{'biology': 1, 'chemistry': 1, 'physics': 1}")
    computer_labs = models.PositiveIntegerField(default=0)
    library = models.BooleanField(default=False)
    toilets_male = models.PositiveIntegerField(default=0)
    toilets_female = models.PositiveIntegerField(default=0)
    toilets_accessible = models.PositiveIntegerField(default=0)
    facilities = models.TextField(blank=True, null=True)
    power_backup = models.BooleanField(default=False)
    internet_wifi = models.BooleanField(default=False)

    # Other Info
    established_date = models.DateField(blank=True, null=True)
    campus_address = models.TextField(blank=True, null=True)

    # Staff Summary (non-editable, should be calculated dynamically)
    total_teachers = models.PositiveIntegerField(default=0)
    total_non_teaching_staff = models.PositiveIntegerField(default=0)
    teacher_student_ratio = models.CharField(max_length=20, blank=True, null=True)
    staff_contact_hr = models.CharField(max_length=100, blank=True, null=True)
    admission_office_contact = models.CharField(max_length=100, blank=True, null=True)

    # Draft system
    is_draft = models.BooleanField(default=True)

    # System Fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code})"
