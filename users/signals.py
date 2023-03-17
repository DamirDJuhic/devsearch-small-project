from django.db.models.signals import post_save,post_delete
from email.mime.image import MIMEImage
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from .models import Profile 
from django.template.loader import render_to_string


#@receiver(post_save,sender=Profile) moze ovako   
def createProfile(sender, instance, created, **kwargs):
   if created:
      user = instance
      profile = Profile.objects.create(
         user=user,
         username=user.username,
         email=user.email,
         name=user.first_name
      )
      #nacin 1
      #subject = 'Welcome to DevSearch'
      #html_message= render_to_string("users/welcome_mail.html", html_message=text/html)
      #send_mail(
         #subject,
         #html_message,
         #settings.EMAIL_HOST_USER,
         #[profile.email],
         #fail_silently=False
      #)
      #nacin 2 
      #ovo za pamtiveka 
      subject, from_email, to = 'hello', settings.EMAIL_HOST_USER , profile.email
      text_content = 'Welcome to DevSearch'
      html_content = render_to_string('users/welcome_mail.html')
      msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.content_subtype = "html"
      msg.send()
      

def updateUser(sender,instance,created,**kwargs):
   profile= instance
   user=profile.user
   
   if created == False:
      user.first_name = profile.name
      user.username= profile.username
      user.email = profile.email
      user.save()
   
def deleteUser(sender, instance, **kwargs):
   user = instance.user
   user.delete()
   print('Delete user...')

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)


