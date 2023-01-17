from django.db import models


# Create your models here.

# null = true, blank=true - bu majburiy emas degani
class Post(models.Model):
    rasm = models.ImageField(upload_to='images/talaba', blank=True, null=True)
    sarlavha = models.CharField(max_length=100,help_text="Matn")
    vaqt = models.DateTimeField(auto_now_add=True)
    text = models.TextField(help_text="Matn")

    def __str__(self):
        return self.sarlavha
    

    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"


    
     


            
    


 
        

    

    
    