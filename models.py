from django.db import models

class Intake(models.Model):  # Class name should follow PascalCase by convention
    id = models.IntegerField(primary_key=True)  # 3-digit ID as primary key
    name = models.CharField(max_length=20)  # Name with max length 20
    age = models.IntegerField()  # Corrected: Add parentheses to define the field
    email = models.EmailField(max_length=255, unique=True)  # Email field with validation and uniqueness
    mobile = models.BigIntegerField(unique=True, help_text="Enter a valid mobile number")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter in YYYY-MM-DD format")
    gender = models.CharField(max_length=10, choices=[('male', 'male'), ('female', 'female')])  # Use choices for gender
    division = models.CharField(max_length=20)  # Division field
    firstvote=models.CharField(max_length=10)

    class Meta:
        db_table = "user_details"  # Fixed typo in table name
        managed = True  # Set to True if Django should manage the table (False if table is created manually)
