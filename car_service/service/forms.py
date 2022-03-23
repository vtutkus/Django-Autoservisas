from django import forms
from .models import Order, OrderMessages, CarInstance


class OrderMessageForm(forms.ModelForm):
    class Meta:
        model = OrderMessages
        fields = ('order', 'author', 'message',)
        widgets = {
            'order': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            'message': forms.Textarea(attrs={"cols": "50", "rows": "3", "style": "width:100%;"},),
        }


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('car_instance', 'due_back')
        widgets = {
            'car_instance': forms.Select(),
            'due_back': forms.DateInput(),
        }

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['car_instance'].queryset = CarInstance.objects.filter(
            owner=self.request.user)
