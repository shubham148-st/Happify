from django.db import models
from django.contrib.auth.models import User




class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    journal = models.TextField()
    happiness = models.IntegerField( default=3)
    img = models.ImageField(upload_to="pics", blank=True)
    audio = models.FileField(upload_to="audio", blank=True)
    location = models.CharField(max_length=50, blank=True)
    additional = models.FileField(upload_to="extras", blank=True)

    def __str__(self):
        return f"Journal Entry {self.id} - Happiness: {self.get_happiness_display()}"
    



class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User model
    journal = models.TextField(blank=True, null=True)
   
class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journal_entries")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    happiness = models.IntegerField()
    img = models.ImageField(upload_to="pics", blank=True)
    audio = models.FileField(upload_to="audio", blank=True)
    location = models.CharField(max_length=50, blank=True)
    additional = models.FileField(upload_to="extras", blank=True)

    def __str__(self):
        return f"Journal Entry {self.id} - Happiness: {self.get_happiness_display()}"

