from django.db import models
from django.db.models.base import Model

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=12)
    contact = models.IntegerField()


    def __str__(self):
        return "%s"%(self.username)

class PlayerScore(models.Model):
    run_perball= models.IntegerField()
    Total_run = models.IntegerField()

    def __str__(self):
        return "%d %d"%(self.run_perball,self.Total_run)

class ComputerScore(models.Model):
    run_perball= models.IntegerField()
    Total_run = models.IntegerField()
    def __str__(self):
        return "%d %d "%(self.run_perball,self.Total_run)

class RPSModel(models.Model):
    player1 = models.IntegerField()
    player2 = models.IntegerField()

    def __str__(self):
        return "%d %d "%(self.player1,self.player2)

