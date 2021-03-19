from django import forms
from .models import Result



class AnswerForm(forms.Form):
    Answer_choice = ((1,'매우아니다'), (2,'아니다'), (3,'보통'), (4,'그렇다'), (5,'매우그렇다'))
    age_choice=((1,'10대'),(2,'20대'),(3,'30대'),(4,'40대'),(5,'50대'),(6,'60대'))
    edu_choice=((1,'고졸미만'),(2,'고졸'),(3,'대졸'),(4,'석사'))
    engant_choice=((1,'네'),(2,'아니오'))
    family_choice=((1,'1명'),(2,'2명'),(3,'3명 이상'))
    gender_choice=((1,'남자'),(2,'여자'))
    hand_choice=((1,'오른손'),(2,'왼손'),(3,'양손'))
    married_choice=((1,'미혼'),(2,'최근 결혼'),(3,'결혼 10년차 이상'),(4,'돌싱'))
    race_choice=((1,'아시아인'),(2,'아랍'),(3,'흑인'),(4,'백인'),(5,'그 외'))
    religion_choice=((2,'무교'),(3,'불교'),(4,'크리스찬'),(5,'무슬림'),(6,'그 외'))
    tp_choice=((0,'매우 강한 부정'),(1,'강한 부정'),(2,'약한 부정'),(3,'매우 약한 부정'),(4,'매우 약한 긍정'),(5,'약한 긍정'),(6,'강한 긍정'),(7,'매우 강한 긍정'))
    urban_choice=((1,'시골'),(2,'교외 지역'),(3,'도시'))
    Name = forms.CharField(label='이름',required=False)
    Question1 = forms.IntegerField(label='질문1',required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question2 = forms.IntegerField(label='질문2', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question3 = forms.IntegerField(label='질문3', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question4 = forms.IntegerField(label='질문4', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question5 = forms.IntegerField(label='질문5', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question6 = forms.IntegerField(label='질문6', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question7 = forms.IntegerField(label='질문7', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question8 = forms.IntegerField(label='질문8', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question9 = forms.IntegerField(label='질문9', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question10 = forms.IntegerField(label='질문10', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question11 = forms.IntegerField(label='질문11', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question12 = forms.IntegerField(label='질문12', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question13 = forms.IntegerField(label='질문13', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question14 = forms.IntegerField(label='질문14', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question15 = forms.IntegerField(label='질문15', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question16 = forms.IntegerField(label='질문16', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question17 = forms.IntegerField(label='질문17', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question18 = forms.IntegerField(label='질문18', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question19 = forms.IntegerField(label='질문19', required=False, widget=forms.RadioSelect(choices=Answer_choice))
    Question20 = forms.IntegerField(label='질문20', required=False, widget=forms.RadioSelect(choices=age_choice))
    Question21 = forms.IntegerField(label='질문21', required=False, widget=forms.RadioSelect(choices=edu_choice))
    Question22 = forms.IntegerField(label='질문22', required=False, widget=forms.RadioSelect(choices=engant_choice))
    Question23 = forms.IntegerField(label='질문23', required=False, widget=forms.RadioSelect(choices=family_choice))
    Question24 = forms.IntegerField(label='질문24', required=False, widget=forms.RadioSelect(choices=gender_choice))
    Question25 = forms.IntegerField(label='질문25', required=False, widget=forms.RadioSelect(choices=hand_choice))
    Question26 = forms.IntegerField(label='질문26', required=False, widget=forms.RadioSelect(choices=married_choice))
    Question27 = forms.IntegerField(label='질문27', required=False, widget=forms.RadioSelect(choices=race_choice))
    Question28 = forms.IntegerField(label='질문28', required=False, widget=forms.RadioSelect(choices=religion_choice))
    Question29 = forms.IntegerField(label='질문29', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question30 = forms.IntegerField(label='질문30', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question31 = forms.IntegerField(label='질문31', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question32 = forms.IntegerField(label='질문32', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question33 = forms.IntegerField(label='질문33', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question34 = forms.IntegerField(label='질문34', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question35 = forms.IntegerField(label='질문35', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question36 = forms.IntegerField(label='질문36', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question37 = forms.IntegerField(label='질문37', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question38 = forms.IntegerField(label='질문38', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question39 = forms.IntegerField(label='질문39', required=False, widget=forms.RadioSelect(choices=tp_choice))
    Question40 = forms.IntegerField(label='질문40', required=False, widget=forms.RadioSelect(choices=urban_choice))



class AnswerForm(forms.ModelForm):
    class Meta:
        Answer_choice = ((1, '매우아니다'), (2, '아니다'), (3, '보통'), (4, '그렇다'), (5, '매우그렇다'))
        age_choice = ((1, '10대'), (2, '20대'), (3, '30대'), (4, '40대'), (5, '50대'), (6, '60대'))
        edu_choice = ((1, '고졸미만'), (2, '고졸'), (3, '대졸'), (4, '석사'))
        engant_choice = ((1, '네'), (2, '아니오'))
        family_choice = ((1, '1명'), (2, '2명'), (3, '3명 이상'))
        gender_choice = ((1, '남자'), (2, '여자'))
        hand_choice = ((1, '오른손'), (2, '왼손'), (3, '양손'))
        married_choice = ((1, '미혼'), (2, '최근 결혼'), (3, '결혼 10년차 이상'), (4, '돌싱'))
        race_choice = ((1, '아시아인'), (2, '아랍'), (3, '흑인'), (4, '백인'), (5, '그 외'))
        religion_choice = ((2, '무교'), (3, '불교'), (4, '크리스찬'), (5, '무슬림'), (6, '그 외'))
        tp_choice = ((1, '예'), (2, '아니오'))
        urban_choice = ((1, '시골'), (2, '교외 지역'), (3, '도시'))
        model=Result
        fields=['Name','Question1','Question2','Question3','Question4','Question5','Question6','Question7','Question8','Question9','Question10',
                'Question11','Question12','Question13','Question14','Question15','Question16','Question17','Question18','Question19','Question20',
                'Question21','Question22','Question23','Question24','Question25','Question26','Question27','Question28','Question29','Question30',
                'Question31','Question32','Question33','Question34','Question35','Question36','Question37','Question38','Question39','Question40']
        widgets={
            'Name':forms.TextInput
        }
        labels={
            'Name':'이름',
            'Question1':'다른 사람을 완전히 신뢰하는 사람은 문제를 일으킨다고 생각하시나요?',
            'Question2':'세상에서 앞서가는 사람들의 대부분은 도덕적으로 깨끗한 삶을 산다고 생각하시나요?',
            'Question3':'모든 사람들은 악한 마음을 가지고있고 문제가 생기면 그 악한 마음이 나올거라고 생각하시나요?',
            'Question4':'도덕적으로 옳다고 확신이 섰을때만 행동하시나요?',
            'Question5':'일반적으로 사람들은 강요받지 않으면 일을 열심히 하지 않는다고 생각하시나요?',
            'Question6':'중요한 사람에게 아부하는것이 중요하다고 생각하시나요?',
            'Question7':'성공하기 위해서는 다른것들을 포기해야한다고 생각하시나요?',
            'Question8':'불치병을 앓고 있는 사람들은 고통없이 죽을 수 있는 선택권을 줘야한다고 생각하시나요?',
            'Question9':'대부분의 사람들은 용감하다고 생각하시나요?',
            'Question10':'사람을 다루기 가장 쉬운 방법은 그들이 듣고 싶어하는 말을 해주는것이라고 생각하시나요?',
            'Question11':'대부분의 사람들과 범죄자들의 가장 큰 차이점은 경찰에게 잡힐만큼 멍청하지 않다고 생각하시나요?',
            'Question12':'정직함은 어떤 경우에도 최선의 방법이라고 생각하시나요?',
            'Question13':'매 분마다 멍청이가 태어난다고 말한 사람이 틀렸다고 생각하시나요?',
            'Question14':'대부분의 사람들은 기본적으로 좋고 친절하다고 생각하시나요?',
            'Question15':'어떤 사람에게 당신이 원하는 무언가를 부탁할때 그 일을 더 열심히 할수있게 하는것 보다 그것을 원하는 진짜 이유를 말해주는것이 좋다',
            'Question16':'모든 방면에 뛰어나다는것이 가능하다고 생각하시나요?',
            'Question17':'대부분의 사람들은 재산을 잃는것보다 부모님의 죽음을 잊는다고 생각하시나요?',
            'Question18':'당신이 어떤 일을한 진짜 이유를 말하면 안된다고 생각하시나요?',
            'Question19':'누군가에게 거짓말을 하는것은 변명의 여지가없다',
            'Question20':'대부분의 경우 권위있고 정직하지 못한것보다 겸손하고 정직한게 낫다',
            'Question21':'당신의 연령대',
            'Question22':'당신의 최종학력',
            'Question23':'모국어가 영어이신가요?',
            'Question24':'형제자매의 수는?',
            'Question25':'당신의 성별은?',
            'Question26':'당신이 필기할때 쓰는 손은?',
            'Question27':'혼인여부',
            'Question28':'인종',
            'Question29':'종교',
            'Question30':'당신은 외향적이고 열정적입니까?',
            'Question31':'당신은 비판적이고 타툼이 있습니까?',
            'Question32':'당신은 믿을만하고 자제력이 있습니까?',
            'Question33':'당신은 불안하고 쉽게 화를 냅니까?',
            'Question34':'당신은 새로운 경험에 개방적이며 복잡한 사람입니까?',
            'Question35':'당신은 조용한 편입니까?',
            'Question36':'당신은 공감을 잘하고 따뜻합니까?',
            'Question37':'당신은 무질서하고 부주의 합니까?',
            'Question38':'당신은 침착하고 정서적으로 안정되있습니까?',
            'Question39':'당신은 창의적이지 않습니까?',
            'Question40':'당신이 어릴적 살던 동네는?',


        }
        def save(self, commit=True):
            post=Result(**self.cleaned_data)
            if commit:
                post.save()
            return post
