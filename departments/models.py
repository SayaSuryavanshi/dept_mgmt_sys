from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)  # Active/Inactive

    def __str__(self):
        return self.dept_name
