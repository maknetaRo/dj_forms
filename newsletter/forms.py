class NewsUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsUsers

        fields = ['email', 'name']
        widgets = {
                'email': forms.TextInput(attrs={'placeholder':'Adres E-mail'}),
                'name': forms.TextInput(attrs={'placeholder':'Imię'}),
        }

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
        super(NewsUserSignUpForm, self).__init__(*args, **kwargs)

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

        def clean_name(self):
            name = self.cleaned_data.get('name')
            return name
