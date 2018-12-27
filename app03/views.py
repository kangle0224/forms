from django.shortcuts import render,HttpResponse
from app01 import models
import json

# 序列化
def xuliehua(request):
    # user_list =
    return render(request, 'xuliehua.html')

from django.core import serializers

def get_data(request):
    ret = {'status': True, 'data': None}
    try:
        # 1. queryset
        # user_list = models.UserInfo.objects.all()
        # serializers.serialize只能对queryset进行序列化
        # ret['data'] = serializers.serialize('json', user_list)
        # 2. values value_list
        user_list = models.UserInfo.objects.all().values('id', 'username')
        # serializers.serialize只能对queryset进行序列化
        ret['data'] = list(user_list)
    except Exception as e:
        ret['status'] = False
    result = json.dumps(ret)
    return HttpResponse(result)
