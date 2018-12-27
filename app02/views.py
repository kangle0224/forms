from django.shortcuts import render, HttpResponse, redirect
from django.forms import Form
from django.forms import fields
from django.forms import widgets
from app01 import models

class TestForm(Form):
    user = fields.CharField(
        required=True,
        max_length=12,
        min_length=3,
        error_messages={},  # 错误提示
        widget=widgets.TextInput(attrs={'name':123}),    #定制生成html插件
        label='用户名',    # 前端的label {{obj.user.label}}
        initial='alex',     #初始值
        help_text='提示信息',    # 提示信息
        show_hidden_initial='True',   # 再生成一个框
        # validators=[],      # 自定义验证
        localize=True,     # 本地化
        disabled=False,     # 是否可编辑
        label_suffix='aaa', # label后缀

    )
    age = fields.IntegerField(
        label='年龄',
        max_value=12,
        min_value=5,
        error_messages={
            "max_value": '太大了',
            "min_value": '太小了',

        }
    )
    email = fields.EmailField(
        label='邮箱',
    )
    img = fields.FileField(
        label='文件'
    )
    city = fields.ChoiceField(
        label='城市',
        choices=[
            (1, "北京"),
            (2, "上海"),
            (3, "广州"),
        ],  # 后台拿到的是字符串1,2,3
        initial=2,   # 默认值也可以在函数中传字典
    )
    # 字符串转换为数字
    # city = fields.TypedChoiceField(
    #     coerce=lambda x: int(x),    # 这个做字符串转换的
    #     label='城市',
    #     choices=[
    #         (1, "北京"),
    #         (2, "上海"),
    #         (3, "广州"),
    #     ],  # 后台拿到的是字符串1,2,3
    #     initial=2,  # 默认值也可以在函数中传字典
    # )
    hobby = fields.MultipleChoiceField(
        choices=[
            (1, '篮球'),
            (2, '足球'),
            (3, '乒乓球'),
        ],  # 后台拿到的是字符串1,2,3，如果需要使用数字，需使用TypedChoiceField
        initial=[1,2],
    )

    xdb = fields.ChoiceField(
        widget=widgets.Select(choices=([
            (1, '篮球'),
            (2, '足球'),
            (3, '乒乓球'),
        ])),
    )

    # 多选
    xdb1 = fields.MultipleChoiceField(
        widget=widgets.SelectMultiple(attrs={'class': 'c1'}),
        choices=[
            (1, '篮球'),
            (2, '足球'),
            (3, '乒乓球'),
        ],
    )

    # checkbox 单选
    xbd2 = fields.CharField(
        widget=widgets.CheckboxInput()
    )

    # checkbox 多选
    xbd3 = fields.MultipleChoiceField(
        initial=[2,],
        choices=((1,'北京'),(2,'上海'),(3,'深圳')),
        widget=widgets.CheckboxSelectMultiple()
    )

    # radio
    xdb4 = fields.ChoiceField(
        initial=2,
        choices=((1, '北京'), (2, '上海'), (3, '深圳')),
        widget=widgets.RadioSelect(),

    )

def test(request):
    if request.method == 'GET':
        obj = TestForm()
        return render(request, 'test.html', {"obj": obj})
    else:
        obj = TestForm(request.POST, request.FILES)
        obj.is_valid()
        return render(request, 'test.html', {"obj": obj})
from django.forms.models import ModelChoiceField
class XqForm(Form):
    price = fields.IntegerField()
    user_id = fields.IntegerField(
        widget=widgets.Select(
            # values_list返回的是元组
            # choices=models.UserInfo.objects.values_list('id', 'username'),
        )
    )

    # 不推荐
    user_id2 = ModelChoiceField(
        queryset=models.UserInfo.objects.all(),
        to_field_name='username'
    )

    def __init__(self, *args, **kwargs):
        # 实时更新，super会拷贝所有字段来赋值
        super(XqForm, self).__init__(*args, **kwargs)
        # 下面这行必须写在super下面
        self.fields["user_id"].widget.choices = models.UserInfo.objects.values_list('id', 'username')


def xq(request):
    obj = XqForm()
    return render(request, 'xq.html', {'obj':obj})

from django.core.exceptions import ValidationError
class AjaxForm(Form):
    username = fields.CharField()
    user_id = fields.IntegerField(
        widget=widgets.Select(choices=[(0,'alex'),(1,'root'),(2,'qwer')])
    )

    # 自定义方法 clean_字段名
    # 必须有返回值 self.cleaned_data['username']
    # 如果出错，raise ValidationError('fieldname')
    def clean_username(self):
        v = self.cleaned_data['username']
        if models.UserInfo.objects.filter(username=v).count():
            # 这里是看源码得到的
            raise ValidationError('用户名已存在')

        # return self.cleaned_data['price']
        return v

import json
def ajax(request):
    if request.method == 'GET':
        obj = AjaxForm()
        return render(request, 'ajax.html', {'obj':obj})
    else:
        ret = {'status': '没钱','msg':None}
        obj = AjaxForm(request.POST)
        if obj.is_valid():
            data = obj.cleaned_data
            ret["status"] = '钱'
            return HttpResponse(json.dumps(ret))
        else:
            ret['msg'] = obj.errors
            # from django.forms.utils import ErrorDict
            # print(obj.errors.as_json())
            # print(obj.errors.as_ul())
            # print(obj.errors.as_data())
            return HttpResponse(json.dumps(ret))






