from django import forms


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=4)
    confirm_password = forms.CharField(required=True, min_length=4)

    # nick_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True, min_length=1)
    last_name = forms.CharField(required=True, min_length=1)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    # gender = forms.ChoiceField(choices=gender, label="性别")


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=4)
    password = forms.CharField(required=True, min_length=4)
