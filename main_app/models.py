from django.db import models
# from django.contrib.auth.models import User
from django.urls import reverse

# Define the possible choices for the category and creature type fields
CATEGORY_CHOICES = (
    ('Financial', 'Financial'),
    ('Personal Development', 'Personal Development'),
    ('Fitness', 'Fitness'),
    ('Productivity', 'Productivity'),
)

CREATURE_CHOICES = (
    ('Squirrel', 'Squirrel'),
    ('Owl', 'Owl'),
    ('Fox', 'Fox'),
    ('Beaver', 'Beaver'),
)

# Define default images for each category
# DEFAULT_IMAGES = {
#     'Financial': 'default_images/financial_default.jpg',
#     'Personal Development': 'default_images/personal_dev_default.jpg',
#     'Fitness': 'default_images/fitness_default.jpg',
#     'Productivity': 'default_images/productivity_default.jpg',
# }

class Goal(models.Model):
    # Primary key is automatically added as 'id' by Django
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    creature_type = models.CharField(max_length=10, choices=CREATURE_CHOICES)
    target_date = models.DateField()
    description = models.TextField(max_length=250, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('goal-detail', kwargs={'goal_id': self.id})

    # Here is where you specify the upload_to argument
    # image = models.ImageField(upload_to='goal_images/', blank=True, null=True)

    # def save(self, *args, **kwargs):
        # Assign default image based on category if no image is provided
        # if not self.image:
        #     self.image = DEFAULT_IMAGES.get(self.category, 'default_images/general_default.jpg')
        # super().save(*args, **kwargs)

    # def __str__(self):
    #     return f"{self.name} - {self.get_creature_type_display()}"
