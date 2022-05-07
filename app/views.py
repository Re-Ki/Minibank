from django.shortcuts import render
from django.http import HttpResponse
import pymongo
from random import randint

connection = pymongo.MongoClient("localhost",27017)
database = connection["Mydatabase"]
collection = database["Mycollection"]

def home(request):
    try:
        return render(request,'home.html',{"data":"Welcome to MiniBank"})
    except Exception as error:
        print(error)
        return render(request,'home.html',{'error':error})

def about(request):
    return render(request,'about.html',{})

def add(request):
    try:
        username = request.POST['name']
        password = request.POST['password']
        query = {'name':username,'password':password}
        data = collection.find_one(query)
        userid , username , userpassword , useramount = data.get('_id'),data.get('name'),data.get('password'),data.get('amount')
        return render(request,'result2.html',{
            "userid": userid,
            "name": username,
            "password":userpassword,
            "amount": useramount
        })
    except Exception as err:
        return render(request,'result2.html',{'error':err})

def login(request):
    return render(request,'login.html',{})

def register(request):
    return render(request,'register.html',{})

def add2(request):
    try:
        username = request.POST['name']
        password = request.POST['password']
        amount = request.POST['amount']
        randomID = randint(000,1000)
        userid = randomID

        insert_data ={'_id':userid,'name':username,'password':password,'amount':amount}
        collection.insert_one(insert_data)
        print("insert Success !")
        return render(request,'result3.html',{'userid':userid,'username':username,'password':password,'amount':amount})
    except Exception as err:
        render(request,'result3.html',{'error':err})

def registerToLogin(request):
    try:
        username = request.POST['name']
        password = request.POST['password']
        query = {'name': username, 'password': password}
        data = collection.find_one(query)
        userid, username, userpassword , useramount = data.get('_id'), data.get('name'),data.get('password'), data.get('amount')
        return render(request, 'result2.html', {
            "userid": userid,
            "name": username,
            "password": userpassword,
            "amount": useramount
        })
    except Exception as err:
        return render(request, 'result2.html', {'error': err})