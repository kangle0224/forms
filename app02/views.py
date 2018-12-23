from django.shortcuts import render
from django.forms import Form
from django.forms import fields
from django.forms import widgets


class TestForm(Form):
    user = fields.CharField(
        required=True,
        max_length=12,
        min_length=3,
        error_messages={},  # 错误提示
        # widget=widgets.Select(),    #定制生成html插件
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







def test(request):
    if request.method == 'GET':
        obj = TestForm()
        return render(request, 'test.html', {"obj": obj})
    else:
        obj = TestForm(request.POST, request.FILES)
        obj.is_valid()
        return render(request, 'test.html', {"obj": obj})

