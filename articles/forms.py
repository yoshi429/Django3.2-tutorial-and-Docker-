from django import forms



class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     title = cleaned_data.get('title')
    #     if title.lower() == 'the office':
    #         raise forms.ValidationError('this title is taken.')
    #     return title 

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)

        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        
        if title.lower() == 'the office':
            raise forms.ValidationError('this title is taken.')
        
        if 'office'in content or 'office' in title.lower():
            self.add_error('content', 'Office cannot be in content')
            raise forms.ValidationError('Office is not allowed')
            
        return cleaned_data