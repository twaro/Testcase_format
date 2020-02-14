from django.db import models
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class TimeStamped(models.Model):
    creation_date = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False, default=now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = now()

        self.last_modified = now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Testcase(TimeStamped):
    title_text = models.CharField(max_length=1000)
    testcase_text = RichTextUploadingField(default="Type here...")

    def __str__(self):
        return self.title_text

class Section(models.Model):
    testcase = models.ForeignKey(Testcase, on_delete=models.CASCADE)
    section_text = models.CharField(max_length=30000)

    def __str__(self):
        return self.section_text