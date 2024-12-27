from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

from django.views.generic import CreateView

# UserCreationForm 클래스는 신규 사용자를 위하여 장고에서 제공해주는 폼 클래스
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserCreateView(CreateView):   # 계정 생성
    template_name = 'registration/register.html'
    
    # 계정 생성을 위하여 사용할 폼을 지정해 줌
    form_class = UserCreationForm
    
    # success_url 속성은 데이터 처리가 성공했을 때 이동할 url을 지정해 주는 역할
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):   # 계정 생성 완료
    template_name = 'registration/register_done.html'