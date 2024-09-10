from django import forms
from .models import User

class UserModelForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', max_length=80, widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호확인', max_length=80, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['userID','email','birth','team']

    def cleaned(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password2 != password1:
            raise forms.ValidationError('비밀번호가 일치 하지 않습니다.')
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        
        if commit:
            user.save()
        
        return user
    
