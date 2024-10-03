from django import forms

class MovieForm(forms.Form):
    title=forms.CharField()

    genre=forms.Select()
    
    language=forms.CharField()


    year=forms.CharField()

    run_time=forms.IntegerField()
    
    director=forms.CharField()

    def clean(self):

        cleaned_data=super().clean()

        year= cleaned_data.get("year")

        run_time=cleaned_data.get("run_time")

        if int(year)< 1990:

            error_message="year should be > 1990"

            self.add_error("year",error_message)

        if run_time>210 or run_time<60:

           error_message ="Run time should be greater than 210 and less than 60"

           self.add_error("run_time",error_message) 
            
         