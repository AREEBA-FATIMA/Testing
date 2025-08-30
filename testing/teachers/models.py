from django.db import models

class Teacher(models.Model):
    # ========== Personal Information ==========
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    permanent_address = models.TextField()
    current_address = models.TextField(blank=True, null=True)
    marital_status = models.CharField(max_length=20, choices=[
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed')
    ], blank=True, null=True)

    # Meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Draft or Final
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class TeacherEducation(models.Model):
    # ========== Education Qualification ==========
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="educations")
    level = models.CharField(max_length=100, choices=[
        ('Secondary', 'Secondary'),
        ('Higher Secondary', 'Higher Secondary'),
        ('Graduation', 'Graduation'),
        ('Diploma', 'Diploma'),
        ('M.Phil', 'M.Phil'),
        ('Ph.D.', 'Ph.D.'),
        ('Other', 'Other'),
    ])
    institution_name = models.CharField(max_length=255)
    year_of_passing = models.PositiveIntegerField()
    subjects_specialization = models.CharField(max_length=255, blank=True, null=True)
    grade_percentage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.teacher.full_name} - {self.level}"


class TeacherExperience(models.Model):
    # ========== Work Experience ==========
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="experiences")
    institution_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)
    subjects_taught = models.CharField(max_length=255, blank=True, null=True)
    classes_taught = models.CharField(max_length=255, blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    total_years_experience = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.teacher.full_name} - {self.institution_name}"


class TeacherSummary(models.Model):
    # ========== Current Summary ==========
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name="summary")
    current_role = models.CharField(max_length=255, blank=True, null=True)
    classes_sections_taught = models.CharField(max_length=255, blank=True, null=True)  # dropdown option
    subjects_taught = models.CharField(max_length=255, blank=True, null=True)          # dropdown option
    additional_responsibilities = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Summary - {self.teacher.full_name}"
