from django import forms

from .models import Server, ServerType


# 定义资产表单验证
class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        #定义表单所需要的字段
        fields = ['zctype', 'ipaddress', 'description', 'brand', 'zcmodel', 'zcnumber', 'zcpz',  'guartime',
                  'comment']


# 定义资产类型表单验证
class ServerTypeForm(forms.ModelForm):
    class Meta:
        model = ServerType
        fields = ['zctype']

