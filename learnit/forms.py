from django import forms


class LearnForm(forms.Form):
    text = forms.CharField(label="What do you want to learn?", max_length=100, widget=forms.TextInput(attrs={'class': 'input-text'}))
    MY_CHOICES = (
        ('1', '1 question'),
        ('2', '2 question'),
        ('3', '3 question'),
        ('4', '4 question'),
        ('5', '5 question'),
    )
    no_of_question_for_quiz = forms.ChoiceField(choices=MY_CHOICES, widget=forms.Select(attrs={'class': 'input-quiz'}))
