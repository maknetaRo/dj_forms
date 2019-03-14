class ContactForm(forms.Form):
    name = forms.CharField(label="", max_length=200)
    subject = forms.CharField(label="", max_length=200, required=False)
    from_email = forms.EmailField(label="", max_length=254)
    content = forms.CharField(label="", max_length=2000, widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label="Wyślij kopię do mnie")
    #captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    def post(self, request, *args, **kwargs):
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response' : recaptcha_response,
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        status = result.get("success", False)
        if not status:
            raise forms.ValidationError("Weryfikacja się nie powiodła. Proszę spróbować jeszcze raz.")


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class':'form-control',
        'placeholder':'Imię (i Nazwisko)'}
        self.fields['from_email'].widget.attrs = {'class':'form-control',
         'placeholder': 'Adres Email'}
        self.fields['subject'].widget.attrs = {'class':'form-control',
        'placeholder': 'Temat'}
        self.fields['content'].widget.attrs = {'class':'form-control',
         'placeholder':'Tu Wpisz Swoją Wiadomość'}
