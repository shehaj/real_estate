from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


    # def save_and_login(self, request):
    #     user = self.save(commit=True)
    #     username = form.cleaned_data.get('username')
    #     raw_password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=raw_password)
    #     login(request, user)

