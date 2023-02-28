from django import forms


class PasswordForms(forms.Form):
    length = forms.ChoiceField(label='Длина пароля',
                                        choices=(('6', '6'),
                                                 ('7', '7'),
                                                 ('8', '8'),
                                                 ('9', '9'),
                                                 ('10', '10'),
                                                 ('11', '11'),
                                                 ('12', '12'),
                                                 ),
                                        initial='8')
    uppercase = forms.BooleanField(label='Верхний регистр', required=False)
    numbers = forms.BooleanField(label='Цифры', required=False)
    special_symbols = forms.BooleanField(label='Специальные символы', required=False)
