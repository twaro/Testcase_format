from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Testcase(models.Model):
    title_text = models.CharField(max_length=1000)
    last_update = models.DateTimeField("Last modified")
    testcase_text = RichTextUploadingField(default="Type here...")

    def __str__(self):
        return self.title_text

class Section(models.Model):
    testcase = models.ForeignKey(Testcase, on_delete=models.CASCADE)
    section_text = models.CharField(max_length=30000)

    def __str__(self):
        return self.section_text