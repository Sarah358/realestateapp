from django.core.mail import send_mail

from real_estate.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response

from .models import Enquiry

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject,message,from_email,recipient_list,fail_silently=True)
        enquiry = Enquiry(name=name,email=email,subject=subject,message=message)
        enquiry.save()

        return Response({"success":"Your enquiry was successfully submitted"})
    except:
        return Response({"failed":"Enquiry not sent.Please try again"})



