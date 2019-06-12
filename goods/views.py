from django.shortcuts import render
from django.core.paginator import Paginator, Page
from . import models
from .models import TypeInfo, GoodsInfo
# Create your views here.

def index(request):
    #查询各分类的最新４条、最热４条数据
    typelist = TypeInfo.objects.all()

    typeinfo = models.TypeInfo.objects.all()
    news = models.GoodsInfo.objects.all()

    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-click')[0:4]

    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-click')[0:4]

    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-click')[0:4]

    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-click')[0:4]

    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-click')[0:4]

    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-click')[0:4]

    context = {'title': '首页', 'guest_cart': 1,
               'type0': type0, 'type01': type01,
               'type1': type1, 'type11': type11,
               'type2': type2, 'type21': type21,
               'type3': type3, 'type31': type31,
               'type4': type4, 'type41': type41,
               'type5': type5, 'type51': type01,
               'typeinfo': typeinfo,  # 类型信息
               'news': news,
               }
    return render(request, 'goods/index.html', context)

#列表页
def list(request):    #分别为类型的id，第几页，按什么排序
    typeinfo = models.TypeInfo.objects.all()
    news = models.GoodsInfo.objects.all()
    #news = typeinfo.goodsinfo_set.order_by('-id')[0:2]  #取该类型最新的两个物品

    #goods = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')


    context = {
        #'title':,  #类型名称  给base传递title
        #'page': page,             #排序后的每页元素列表
        'typeinfo': typeinfo,     #类型信息
        'news': news,             #新品推荐列表
        #'sort': sort,             #传递排序数字
        #'paginator': paginator,   #分页

    }

    return render(request, 'goods/index.html', context)