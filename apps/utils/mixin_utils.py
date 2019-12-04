from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 定义只有登录才能访问的class
class LoginRequiredMixin(object):
    '''这个函数没看懂。。。'''
    '''现在看懂了'''
    # @login_required(login_url='/users/login')
    @method_decorator(login_required(login_url='/users/login'))  # method_decorator的作用是向装饰器中补充self参数，使之能适配类方法
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)  # 妙啊！！！