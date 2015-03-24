from django.db import models

### Model for Vehicle 
class Vehicle(models.Model):
  trim_id	= models.IntegerField()
  year 		= models.IntegerField()
  make 		= models.CharField(max_length=32)
  model 	= models.CharField(max_length=16)
  trim_name 	= models.CharField(max_length=256)

  def __str__(self):
      return "Vehicle  Year: %s, Make: %s, Model: %s, Trim Name: %s, Trim Id: %s" % \
	      (self.year,
	       self.format_str(self.make),
	       self.format_str(self.model),
	       self.format_str(self.trim_name),
	       self.trim_id)

  def format_str(self, field):
      return field.replace('\"','')


### Model for Vehicle Serial Number Patterns
class VSNPattern(models.Model):
   pattern = models.CharField(max_length=16)
   vehicle = models.ForeignKey(Vehicle)

   def __str__(self):
       return "Pattern %s, Vehicle Trim Id %s" % (self.pattern, self.vehicle.trim_id)


 
