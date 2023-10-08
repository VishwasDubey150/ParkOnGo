from django.db import models

# Create your models here.

# vehicle class 

class User(models.Model):
    name = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length = 10)
    license = models.CharField(max_length=15)
    longitude = models.FloatField()
    longitude_from = models.CharField(max_length = 1, choices = [
        ('E','E'),('W','W')
    ])
    latitude = models.FloatField()
    latitude_from = models.CharField(max_length = 1, choices = [
        ('N','N'),('S','S')
    ])

    def __str__(self):
        return self.name

class Locality(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    longitude_from = models.CharField(max_length = 1, choices = [
        ('E','E'),('W','W')
    ])
    latitude = models.FloatField()
    latitude_from = models.CharField(max_length = 1, choices = [
        ('N','N'),('S','S')
    ])

    def __str__(self):
        return self.name

class Parking(models.Model):
    choices = [
        (1,'Not Satisfied'),
        (2,'Not Up to the Mark'),
        (3,'Average'),
        (4,'Good'),
        (5,'Excellent')

    ]
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    longitude_from = models.CharField(max_length = 1, choices = [
        ('E','E'),('W','W')
    ])
    latitude = models.FloatField()
    latitude_from = models.CharField(max_length = 1, choices = [
        ('N','N'),('S','S')
    ])
    available = models.IntegerField()
    total = models.IntegerField()
    rating = models.IntegerField(choices=choices)
    user_visited = models.ManyToManyField(User)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=12)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length = 100)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)

class Local_Business(models.Model):
    choices = [
        (1,'Not Satisfied'),
        (2,'Not Up to the Mark'),
        (3,'Average'),
        (4,'Good'),
        (5,'Excellent')

    ]
    charChoices = [
        ('food','food'),
        ('grocery','grocery'),
        ('Chemist','Chemist'),
    ]
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    longitude_from = models.CharField(max_length = 1, choices = [
        ('E','E'),('W','W')
    ])
    latitude = models.FloatField()
    latitude_from = models.CharField(max_length = 1, choices = [
        ('N','N'),('S','S')
    ])
    rating = models.IntegerField(choices=choices)
    type = models.CharField(choices = charChoices,max_length=25)
    locality = models.ForeignKey(Locality,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Stations(models.Model):
    choice = [
        (1,'Not Satisfied'),
        (2,'Not Up to the Mark'),
        (3,'Average'),
        (4,'Good'),
        (5,'Excellent')

    ]
    choices = [
        ('charging','Charging'),
        ('Gas stations','Gas stations')
    ]
    name = models.CharField( max_length=50)
    type = models.CharField(choices= choices,max_length = 50)
    longitude = models.FloatField()
    longitude_from = models.CharField(max_length = 1, choices = [
        ('E','E'),('W','W')
    ])
    latitude = models.FloatField()
    latitude_from = models.CharField(max_length = 1, choices = [
        ('N','N'),('S','S')
    ])
    rating = models.IntegerField(choices=choice)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    payment = models.FloatField()
    is_payment_done = models.BooleanField(choices = [
        (False, 'No'),
        (True,'Yes')
    ])
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Parking = models.ForeignKey(Parking,on_delete=models.CASCADE)
    # qr 
    payment_via = models.CharField(max_length=50)

# Settings