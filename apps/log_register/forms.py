from .models import User
from django import forms
import bcrypt
import re

# Register form


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(
        max_length=255, label='Confirme contraseña')
    password_confirm.widget = forms.TextInput(attrs={'type': 'password'})

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'password_confirm',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'password': 'Contraseña',
        }
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'})
        }

# Register form validations

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not valid_names(first_name):
            raise forms.ValidationError('Ingrese un nombre válido.')
        if len(first_name) < 4:
            raise forms.ValidationError(
                'El nombre no puede tener menos de 4 caracteres.'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not valid_names(last_name):
            raise forms.ValidationError(
                'Ingrese un apellido válido.'
                )
        if len(last_name) < 3:
            raise forms.ValidationError(
                'El apellido no puede tener menos de 3 caracteres.'
            )
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email = email)
        if not valid_email(email):
            raise forms.ValidationError(
                'Ingrese un email válido.'
                )
        if user:
            raise forms.ValidationError(
                'El email ya está en uso.'
                )
        if len(email) < 10:
            raise forms.ValidationError(
                'El email debe tener como mínimo 10 caracteres.'
                )
        return email

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(
                {
                    'password': 'Las contraseñas deben ser iguales'
                    }
                )
        if len(password) < 10:
            raise forms.ValidationError(
                {
                    'password':'La contraseña debe tener como mínimo 10 caracteres'
                    }
                )
        if len(password_confirm) < 10:
            raise forms.ValidationError(
                {
                    'password':'La contraseña debe tener como mínimo 10 caracteres'
                    }
                )
        
                


# Login form

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

        labels = {
            'email': 'Email',
            'password': 'Contraseña'
        }
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'})
        }

# Login form validations

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = User.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                {
                    'email':'Email no registrado'
                    }
                )
        if len(email) < 10:
            raise forms.ValidationError(
                {
                    'email':'El email debe tener como mínimo 10 caracteres'
                    }
                )
        user = user[0]
        if not bcrypt.checkpw(password.encode(), user.password.encode()):
            raise forms.ValidationError(
                {
                    'password':'Contraseña errónea'
                    }
            )
        return cleaned_data


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

# Register form validations

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not valid_names(first_name):
            raise forms.ValidationError('Ingrese un nombre válido.')
        if len(first_name) < 4:
            raise forms.ValidationError(
                'El nombre no puede tener menos de 4 caracteres.'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not valid_names(last_name):
            raise forms.ValidationError(
                'Ingrese un apellido válido.'
                )
        if len(last_name) < 3:
            raise forms.ValidationError(
                'El apellido no puede tener menos de 3 caracteres.'
            )
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email = email)
        if not valid_email(email):
            raise forms.ValidationError(
                'Ingrese un email válido.'
                )
        if len(email) < 10:
            raise forms.ValidationError(
                'El email debe tener como mínimo 10 caracteres.'
                )
        return email

#REGEX functions

class EditPasswordForm(forms.ModelForm):
    password_confirm = forms.CharField(
        max_length=255, label='Confirme contraseña')
    password_confirm.widget = forms.TextInput(attrs={'type': 'password'})

    class Meta:
        model = User
        fields = [
            'password',
            'password_confirm',
        ]
        labels = {
            'password': 'Contraseña',
        }
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'})
        }


    def clean(self):
        cleaned_data = super(EditPasswordForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(
                {
                    'password': 'Las contraseñas deben ser iguales'
                    }
                )
        if len(password) < 10:
            raise forms.ValidationError(
                {
                    'password':'La contraseña debe tener como mínimo 10 caracteres'
                    }
                )
        if len(password_confirm) < 10:
            raise forms.ValidationError(
                {
                    'password':'La contraseña debe tener como mínimo 10 caracteres'
                    }
                )



def valid_names(name):
    REGEX_NAME = re.compile(r'^[A-Za-z]+$')
    return REGEX_NAME.match(name)


def valid_email(email):
    REGEX_EMAIL = re.compile(
        r'^[a-zA-Z0-9\._-]+@[a-zA-Z0-9\.]+\.[a-zA-Z]{2,3}$'
    )
    return REGEX_EMAIL.match(email)
