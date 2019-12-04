from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 定义只有登录才能访问的class
class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/users/login')) #method_decorator的作用是将函数装饰器转化为一个方法装饰器（自动添加self参数）
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs) #这是什么用法？？没找到dispatch方法，实际上起作用的也就是装饰器啊
