from django import forms


class PdfExtractForm(forms.Form):
    file = forms.FileField(label="Upload PDF Document")
    # page = forms.CharField(max_length=20, label="Page Number")
    
    # def clean_file(self):
    #     file = self.cleaned_data.get('file')
    #     if not file.name.lower().endswith('.pdf'):
    #         raise forms.ValidationError("Only pdf documents are allowed. ")
    #     return file