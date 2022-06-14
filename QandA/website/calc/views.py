from audioop import reverse
import json
from pickle import APPEND
from urllib import request
from django.shortcuts import render
import mysql.connector
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')


def index_login(request):
    return render(request,'login.html')

def login(request): 
    if request.method=="POST":
        name=request.POST['fullName']
        username=request.POST['userName']
        email=request.POST['eMail']
        pwd=request.POST['passWord']

        conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
        cursor=conn.cursor()

        cursor.execute("insert into project.users(name,username,email,password) values(%s,%s,%s,%s)",(name,username,email,pwd))

        return render(request,'login.html')

    else:    
        return render(request,'signup.html')


def home_feed(request):
    global uname
    conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
    cursor1=conn.cursor()

    cursor1.execute("select questions from project.questions")
    data=cursor1.fetchall()

    if id is not None:
            conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
            cursor1=conn.cursor()

            cursor1.execute("select username,questions from project.questions")
            data=cursor1.fetchall()

            str(data)
            # list_questions = [lis[0] for lis in data]
            # list_questions.reverse()
            # list_questions=str(list_tuple_questions)

            data.reverse()

            cursor1.execute("select username,answers from project.answers")
            answers_data=cursor1.fetchall()

            str(answers_data)
            answers_data.reverse()

            return render(request,'feed.html',{'result':data,'answer':answers_data})


def feed(request):
    if request.method=="POST":
        global uname
        uname=request.POST['username']
        ps=request.POST['userpassword']

        conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
        cursor=conn.cursor()

        cursor.execute("select * from project.users where username=%s and password=%s",(uname,ps))
        id=cursor.fetchone()

        if id is not None:
            conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
            cursor1=conn.cursor()

            cursor1.execute("select username,questions from project.questions")
            data=cursor1.fetchall()

            str(data)
            # list_users= [li[0] for li in data]
            # list_questions = [lis[1] for lis in data]
            data.reverse()

            cursor1.execute("select username,answers from project.answers")
            answers_data=cursor1.fetchall()

            str(answers_data)
            answers_data.reverse()

            return render(request,'feed.html',{'result':data,'answer':answers_data})
            
        else:
            return render(request,"login.html")

def comment(request):
    if request.method=="POST":
        conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
        cursor1=conn.cursor()

        cursor1.execute("select username,questions from project.questions")
        data=cursor1.fetchall()
        data.reverse()

        answer=request.POST['answer']
        if answer is None:
            return render(request,'feed.html',{'result':data})
        else :
            # cursor1.execute("select user_id from project.users where username=%s",(uname,))
            # id=cursor1.fetchone()
            # u_id=int(''.join(map(str,id)))

            global uname
            cursor1.execute("insert into project.answers(username,answers) VALUES (%s,%s)",(uname,answer))

            cursor1.execute("select username,answers from project.answers")
            answers_data=cursor1.fetchall()

            str(answers_data)
            answers_data.reverse()

            return render(request,'feed.html',{'result':data,'answer':answers_data})


def profile(request):
    profile_name = 'John'
    return render(request,'profile.html',{'Profile_name':profile_name})

def notification(request):
    return render(request,'notification.html')

def settings(request):
    return render(request,'settings.html')

def add(request):
    if request.method=="POST":
        uname=request.POST['uname']
        ques=request.POST['question']

        conn= mysql.connector.connect(host='localhost',user='root',password='2307@darsh',database='project',autocommit=True)
        cursor=conn.cursor()

        cursor.execute("select user_id from project.users where username=%s",(uname,))
        id=cursor.fetchone()
        u_id=int(''.join(map(str,id)))

        cursor.execute("insert into project.questions(username,user_id,questions) VALUES (%s,%s,%s)",(uname,u_id,ques))

        return render(request,"add.html")
    else:
        return render(request,'add.html')

def search_q(request):
    return render(request,'search.html')

