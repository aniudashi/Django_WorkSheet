
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import json
import datetime
from django.core import serializers
from workSheet import models


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.__str__()
        elif isinstance(obj,datetime.date):
            return obj.__str__()
        else:
            return json.JSONEncoder.default(self, obj)

def index(request):
    return render(request, 'index.html')

def data(request):
    allrecords = models.workSheetTable.objects.all()
    dataCount = allrecords.count()
    list =[]
    for data in allrecords:
        dict = {}  # 存放数据的字典
        dict["priority"] = data.priority
        dict["order_id"] = data.order_id
        dict["order_time"] = data.order_time
        dict["topic_desc"] = data.topic_desc
        dict["topic_type"] = data.get_topic_type_display()
        dict["topic_desc"] = data.topic_desc
        dict["dev_person"] = data.dev_person
        dict["dev_state"] = data.get_dev_state_display()
        dict["plan_dev_finish_time"] = data.plan_dev_finish_time
        dict["dev_finish_time"] = data.dev_finish_time
        dict["test_person"] = data.test_person
        dict["test_state"] = data.get_test_state_display()
        dict["plan_test_finish_time"] = data.plan_test_finish_time
        dict["test_finish_time"] = data.test_finish_time
        dict["plan_online_time"] = data.plan_online_time
        list.append(dict)
    Result = {"code": 0, "msg": "OK", "count":dataCount,"data":list}
    print(Result)
    return HttpResponse(json.dumps(Result,cls=CJsonEncoder),content_type="application/json")