from django.db import models

class Movies(models.Model):
  title = models.CharField(max_length=255)
  director = models.CharField(max_length=50)
  release_date= models.DateField(auto_now_add=True)
  duration_minutes = models.IntegerField()
  synopsis = models.TextField()
  genre = models.TextField()

  def __str__(self):
    return self.title
  
class Review(models.Model):
  movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
  user = models.CharField(max_length=30)
  review = models.TextField()
  review_date = models.DateField()
  score = models.IntegerField()

  def __str__(self):
    return self.user
