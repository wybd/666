

from django.http import HttpResponse
import time

def index(request):
    return HttpResponse('hello,world')

def giao(request):
    return HttpResponse('你给我的一giaogiao')

def zhengze(request,year,where):
    return HttpResponse("我在%s年去%s" %(where,year))

def demo(request,id):
    print(id)
    return HttpResponse("demo")

def demo02(request,year,where):
    return HttpResponse("我在%s年去%s" %(where,year))

def datys(request,year,mouth,day):
    ret1=time.mktime(time.strptime('{0}-{1}-{2}'.format(year,mouth,day),'%Y-%m-%d'))
    ret2=time.mktime(time.strptime("2019-01-01","%Y-%m-%d"))
    ret3=ret1-ret2
    n=int(ret3/60/60/24)
    return HttpResponse(n)