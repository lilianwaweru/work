from django.template.loader import render_to_string
from django.core.mail import EmailMessage as EmailMultiAlternatives


def send_welcome_email(receipient,sender,subject,body):
    print("called ")
    # Creating message subject and sender
    #receipient = ""
    #sender = 'lilowesh.lw@gmail.com'
    #subject = ""
    #body = ""

    #passing in the context vairables
    # text_content = render_to_string('email/newsemail.txt',{"name": name})
    # html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,body,to=[receipient])
    # msg.attach_alternative(html_content,'text/html')
    a=msg.send()
    if a:
        print(a)
    else:
        print("#### subject")
        print (subject)
        print("#### recept")
        print (receipient)
        print("#### body")
        print (body)
