from django.db import models
from .utility import nearestpairpoints



# Coordinat model class , represtation of application table in the database.
class Coordinates(models.Model):
    submitted_coordinate = models.CharField(max_length=1000000)
    closet_paircoordinates= models.CharField(blank = True,max_length=1000000,editable =False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = "Coordinates"
    
  
    """  Save method is being overidden because field closet_paircoordinates need to be populated automatically 
    by result of operations performed on field submitted_coordinate if the field contain only one point by  default, autopopulation 
    of (submitted_x,submit_y) and origin is autopopulated"""


    def  save(self, *args, **kwargs):
        if not self.id:
            listtoworkon = list(eval(self.submitted_coordinate))
            string = str(listtoworkon)
            count = 0
            substring= '),'
            count = string.count(substring)
            if count > 0:
                self.closet_paircoordinates = str(list(nearestpairpoints(listtoworkon))).strip('[]')
            else:
                 self.closet_paircoordinates = string + "(0 ,0)"
        super(Coordinates,self).save(*args, **kwargs)


    def __str__ (self):
        #return cordinate list and closet pair from the list
       return str(self.submitted_coordinate + " closet pair points-> "+ self.closet_paircoordinates)



