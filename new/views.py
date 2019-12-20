from django.http  import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Work
from .forms import WorkForm
from .email import send_welcome_email

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        form = WorkForm(request.POST)
        print("Successful")
        subject= request.POST.get("subject")
        print (subject)
        receipient = request.POST.get("receipient")
        print (receipient)
        body = request.POST.get("body")
        print (body)
        send_welcome_email(receipient,"",subject,body)
        if form.is_valid():
            create=form.save(commit=False)
            create.save()
        return redirect('report')
    else:
        form =  WorkForm()  
    return render(request,'welcome.html',{"form":form})




        # """
        # if form.is_valid():
        #     create = form.save(commit=False)
        #     receipient = form.cleaned_data['receipient']
        #     sender = form.cleaned_data['sender']
        #     subject= form.cleaned_data['subject']
        #     body = form.cleaned_data['body']
        #     send_welcome_email(receipient,sender,subject,body)
        #     create.save()
            
        #     return redirect('welcome')"""

    
def report(request):
    works = Work.objects.all()
    
    return render(request,'report.html',{"works":works})





