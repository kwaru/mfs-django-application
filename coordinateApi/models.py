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
    
    #Overriding save method to populate closet points pair column
    def  save(self, *args, **kwargs):
        if not self.id:
            listtoworkon = list(eval(self.submitted_coordinate))
            string = str(listtoworkon)
            count = 0
            substring= '),'
            count = string.count(substring)
            print(listtoworkon)
            if count > 0:
                self.closet_paircoordinates = str(list(nearestpairpoints(listtoworkon)))
            else:
                 self.closet_paircoordinates = string + "(0 ,0)"
        super(Coordinates,self).save(*args, **kwargs)


    def __str__ (self):
        #return cordinate list and closet pair from the list
       return str(self.submitted_coordinate + " closet pair points-> "+ self.closet_paircoordinates)



