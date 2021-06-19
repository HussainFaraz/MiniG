from django import forms
from accounts.form import RPSForm, UserForm,ComputerForm,PlayerForm
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import RPSModel, User,PlayerScore,ComputerScore
from django.contrib import messages
from django.db.models import Sum
import random
# Create your views here.
def introcric(request):
    return render(request,'Introcric.html')
def introRPS(request):
    return render(request,'IntroRPS.html')

def user(request):
    return render(request,'home.html')

def register(request):
   if request.method == "POST":
       username = request.POST['username']
       try:
            userdb = User.objects.get(username=username)
            messages.success(request,('User is already registered. Please login and proceed..'))
            return render(request,'Registeration.html')
       except:    
            form = UserForm(request.POST)
            if(form.is_valid()):
                form.save()
                return render(request,'Login.html')
            else:
                messages.success(request,('Please re-submit the form with the correct details..'))
                return render(request,'Registeration.html')
   else:
       return render(request,'registeration.html')
       
def login(request):
    if request.method == "POST":
        username = request.POST['username_login']
        password = request.POST['password_login']
        try:
            userdb = User.objects.get(username=username)         
            if(username==userdb.username and password==userdb.password):
                return render(request,'home.html',{'username':username})
            else:
                messages.success(request,('Login Failed.. Please check your username and password'))
                return render(request,'Login.html')
            
        except:
            messages.success(request,('Please Register yourself..'))
            return render(request,'Login.html')
    else:
        return render(request,'Login.html')

def toss(request):   
    if request.method=="POST":
        toss = ''
        toss_result = random.randint(0,1)
        valtail = request.POST['toss']
        if(toss_result==0):
            toss='Tails'
        else:
            toss='Heads'
       
        if(toss==valtail):
            messages.success(request,('You have won the toss'))
            messages.success(request,('What have you decided?'))
            return render(request,'tosswon.html')
        else:
            #messages.success(request,('Opponent has won the toss and decided to bat first'))
            return render(request,'oppbatfirst.html')
    else:
        return render(request,'cricket.html')

def battingprofile(request):
    if request.method=="POST":
        return render(request,'playerbatfirst.html')

def ballingprofile(request):
    if request.method=="POST":
        return render(request,'oppbatfirst.html')

def battingstart(request):
    #flag=PlayerScore.objects.aggregate(Sum('playerballfirst'))           
    bat = random.randint(0,6)
    form = PlayerScore(run_perball= bat,Total_run =0)
    form.save()
    if(bat!=0):
        currentscore =  PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        return render(request,'playerbatfirst.html',{'score':bat ,'currentscore':currentscore})
    else:
        cricdb= PlayerScore.objects.aggregate(Sum('run_perball'))             
        for i in cricdb.values():
            totalscore = int(i)
        scoreToWIn = totalscore+1
        #messages.success(request,('OUT!!!'))
        return render(request,'PlayerInningBreak.html',{'result':scoreToWIn})
        #opponent won

def battingsecond(request):
    totalcompscore=ComputerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
   
    bat = random.randint(0,6)
    form = PlayerScore(run_perball= bat,Total_run =0)
    form.save()
    #totalplayerscore = PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
    #if(totalplayerscore>totalcompscore):
      # return HttpResponse("You Won!!")
    if(bat!=0):
        currentscore = PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        return render(request,'playerbatsecond.html',{'score':bat,'currentscore':currentscore})
    else:
        totalplayerscore = PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        ComputerScore.objects.all().delete()
        PlayerScore.objects.all().delete()
        #messages.success(request,('OUT!!!')) 
        if(totalplayerscore>totalcompscore):
            rundifference = "1 wicket"
            return render(request,'result.html',{'result':totalplayerscore,'statement':"Congratulations!! You Won by",'rundifference':rundifference})
            #return HttpResponse("You Won!!")
        if(totalcompscore==totalplayerscore):
            return render(request,'result.html',{'result':totalplayerscore,'statement':"Match Tied"})
        else:
            rundifference = totalcompscore-totalplayerscore
            return render(request,'result.html',{'result':totalcompscore,'statement':"You Lost by ",'rundifference':rundifference,'statement2':"runs"})
            #return HttpResponse("Lost")
       #ball = battingstart(request,totalscore)
       # return HttpResponse("You lost" , totalplayerscore)
        
   
def ballingstart(request):

    #opp bat first
    bat = random.randint(0,6)
    form = ComputerScore(run_perball= bat,Total_run =0)
    form.save()
    if(bat!=0):
        currentscore = ComputerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        return render(request,'oppbatfirst.html',{'score':bat,'currentscore':currentscore})
    else:
        cricdb= ComputerScore.objects.aggregate(Sum('run_perball'))
        for i in cricdb.values():
            totalscore = int(i)
        scoreToWIn = totalscore+1
        #messages.success(request,('OUT!!!')) 
       #ball = battingstart(request,totalscore)
        return render(request,'CompInningBreak.html',{'result':scoreToWIn})

def ballingsecond(request):
    totalplayerscore=PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
   
    bat = random.randint(0,6)
    form = ComputerScore(run_perball= bat,Total_run =0)
    form.save()
    #totalplayerscore = PlayerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
    #if(totalplayerscore>totalcompscore):
      # return HttpResponse("You Won!!")
    if(bat!=0):
        currentscore = ComputerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        return render(request,'oppbatsecond.html',{'score':bat,'currentscore':currentscore})
    else:
        totalcompscore = ComputerScore.objects.aggregate(Sum('run_perball')).get('run_perball__sum')
        ComputerScore.objects.all().delete()
        PlayerScore.objects.all().delete()
        #messages.success(request,('OUT!!!')) 
        if(totalplayerscore>totalcompscore):
            rundifference = totalplayerscore - totalcompscore
            return render(request,'result.html',{'result':totalplayerscore,'statement':"Congratulations!! You Won by",'rundifference':rundifference,'statement2':"runs"})
            #return HttpResponse("You Won!!")
        else:
            rundifference = "1 wicket"
            return render(request,'result.html',{'result':totalcompscore,'statement':"Opponent won by ",'rundifference':rundifference})
            #return HttpResponse("Lost")
       

       
def RPS(request):
    if request.method=='POST':
        if 'rock' in request.POST:
            player1 = 1
        elif 'paper' in request.POST:
            player1=2
        elif 'scissor' in request.POST:
            player1=3
        player2 = random.randint(1,3)
        form = RPSModel(player1 = player1 , player2 = player2)
        form.save()
        if(player1==1):
            msg1 = "Player-1 Choose Rock"
        if(player1==2):
            msg1 = "Player-1 Choose Paper"
        if(player1==3):
            msg1 = "Player-1 Choose Scissor"
        if(player2==1):
            msg2 = "Opponent Choose Rock"
        if(player2==2):
            msg2 = "Opponent Choose Paper"
        if(player2==3):
            msg2 = "Opponent Choose Scissor"
        
        if(player1==player2):
            finalmsg = "Match Tied"
        if(player1==1 and player2==2):
            finalmsg = "Opponent won"
        if(player1==1 and player2==3):
            finalmsg = "Player-1 won"
        if(player1==2 and player2==1):
            finalmsg="Player-1 won"
        if(player1==2 and player2==3):
            finalmsg="Opponent won"
        if(player1==3 and player2==1):
            finalmsg="Opponent won"
        if(player1==3 and player2==2):
            finalmsg="Player-1 won"
        RPSModel.objects.all().delete()
        return render(request,'RPS.html',{'finalmsg':finalmsg , 'msg1':msg1,'msg2':msg2})
    else:
        
        return render(request,'RPS.html')


    

  