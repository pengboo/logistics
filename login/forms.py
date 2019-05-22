from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'name_input', 'placeholder': "用户名", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'pass_input', 'placeholder': "密码"}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput())
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput())
    phone = forms.CharField(label="手机号码", max_length=11, widget=forms.TextInput())
    department= forms.CharField(label="部门", max_length=20, widget=forms.TextInput())
    sex = forms.ChoiceField(label='性别', choices=gender)