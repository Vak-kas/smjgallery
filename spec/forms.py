from django import forms;
from spec.models import Activity

class ActivityForm(forms.ModelForm):
    class Meta:
        model =  Activity;
        field = ['check', 'subject', 'start_date', 'end_date', 'award', 'content']
        labels = {
            'check' : "메인화면 출력 여부",
            'subject' : '활동명',
            'start_date' : "시작일",
            "end_date" : "종료일",
            "award" : "수상 내역",
            "content" : "활동 내용",
        }
