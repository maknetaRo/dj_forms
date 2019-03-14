from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from .forms import NewsUserSignUpForm
from .models import NewsUsers

def subscribe_form(request):
    form = NewsUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsUsers.objects.filter(email=instance.email).exists():
            messages.add_message(request, messages.SUCCESS,
                            "Twój email jest już w naszej bazie danych.")

        else:
            instance.save()

            subject = "Dziękujemy za zapisanie się na nasz newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletter/templates/newsletter/subscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/subscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            messages.add_message(request, messages.SUCCESS,
                            "Dziękujemy za zapisanie się na nasz newsletter.")


    return {'subscribe_form' : form}
