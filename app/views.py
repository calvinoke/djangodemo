from django.shortcuts import render, redirect
import datetime
# Create your views here.
#from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")


#def index(request):
    #now = datetime.datetime.now()
    #html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    #return HttpResponse(html)    # rendering the template in HttpResponse



# Create your views here.

def index(request):
    return render(request,'app/index.html')


from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')


from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request,'app/index.html')

from django.shortcuts import render
from app.form import EmpForm

def indexoo(request):
    stu = EmpForm()
    return render(request,"app/index.html",{'form':stu})


from django.shortcuts import render
from app.form import StudentForm, EmployeeForm

def indext(request):

    #instantiation of the form
    student = StudentForm()
    return render(request,"app/index.html",{'form':student})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'app/index.html',{'form':form})

from django.shortcuts import render
from django.http import HttpResponse
from app.functions.functions import handle_uploaded_file
from app.form import StudentForm
def indexs(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"app/index.html",{'form':student})

def methodinfo(request):
    return HttpResponse("Http request is: "+request.method)

from django.shortcuts import render
from django.http import HttpResponse

def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail);

from django.shortcuts import render
from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: "+  tutorial);

import csv

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])
    return response

from app.models import Employee
import csv
def getfiles(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = Employee.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.eid,employee.ename,employee.econtact])
    return response

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response