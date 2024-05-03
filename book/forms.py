from django import forms

from book.models import Book, Tag


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Поиск',
                'class': 'form-control'
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    orderings = (
        ('title', 'По заголовку'),
        ('-title', 'По заголовку (обратно)'),
        ('rate', 'По оценке'),
        ('-rate', 'По оценке (обратно)'),
        ('created_at', 'По дате создания'),
        ('-created_at', 'По дате создания (обратно)')
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=5)
    text = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    rate = forms.FloatField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'python' in title.lower():
            raise forms.ValidationError('Слово "python" недопустимо в заголовке')
        return title

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate


class BookForm2(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'text', 'image', 'rate', 'tags']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Введите текст',
                    'rows': 5,
                    'cols': 30,
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите заголовок',
                    'class': 'form-control'
                }
            ),
            'rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Введите оценку',
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title and text and title.lower() == text.lower():
            raise forms.ValidationError('Заголовок и текст не должны совпадать')
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'python' in title.lower():
            raise forms.ValidationError('Слово "python" недопустимо в заголовке')
        return title

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        if rate < 0:
            raise forms.ValidationError('Оценка не может быть отрицательной')
        return rate
