class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "home/contact_form.html"
    success_url = '/thank_you/'


    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        content = "{name} / {from_email} wysłał/a Ci następującą wiadomość: ".format(
                    name = form.cleaned_data['name'],
                    from_email = form.cleaned_data['from_email'])
        content += "\n\n{0}".format(form.cleaned_data['content'])
        from_email = form.cleaned_data['from_email']
        cc_myself = form.cleaned_data['cc_myself']
        recipients = ['romagda321@gmail.com']
        if cc_myself:
            recipients.append(from_email)
        try:
            send_mail(subject, content, from_email, recipients,
                    fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return super(ContactFormView, self).form_valid(form)



def thank_you(request):
    return render(request, 'home/thank_you.html', {'page':'thankyou'})

def clear(request):
    form = ContactForm()
    return render(request, 'home/contact_form.html', {'form':form})
