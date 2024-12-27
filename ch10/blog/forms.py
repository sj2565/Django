from django import forms

class PostSearchForm(forms.Form):   # django에 기본적으로 Form이 있음
    # html 형식 : <input type = "text" name = "Search_Word">
    search_word = forms.CharField(label="Search Word ")