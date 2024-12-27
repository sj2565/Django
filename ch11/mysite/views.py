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

from django.contrib.auth.mixins import AccessMixin

class OwnerOnlyMixin(AccessMixin):
    # True이면 403 예외에 대한 응답 객체를 돌려준다.
    # False이면 로그인 페이지로 이동시킨다.
    raise_exception = True
    
    # 403 예외 발생 시 보여 주고자 하는 메세지
    permission_denied_message = '해당 소유자만 수정/업데이트가 가능합니다.'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:   # 사용자와 소유자가 동일하지 않으면
            return self.handle_no_permission()  # 403 예외를 클라이언트에게 전송한다.
        return super().dispatch(request, *args, **kwargs)