from django import forms
from .models import Book

# ========================
# ExampleForm
# ========================
class ExampleForm(forms.ModelForm):
    """
    نموذج مثال للتدريب أو للاختبار.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

# ========================
# BookForm
# ========================
class BookForm(forms.ModelForm):
    """
    نموذج لإضافة أو تعديل الكتب مع التحقق الكامل من البيانات.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # مثال على التحقق الإضافي من البيانات
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title
