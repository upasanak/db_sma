from django.db import models

class UploadFile(models.Model):
    your_name = models.CharField(max_length=70)
    py_file = models.FileField(upload_to='media')
    #py_file = models.FileField(upload_to="savedfile", blank=True)

    #csv_file = models.FileField(upload_to="media", blank=True)

    def __str__(self):
        return self.your_name