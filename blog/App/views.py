import os
from random import randint

from django.contrib import auth
from django.contrib.auth import login,authenticate
from django.core.paginator import Paginator
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime,time
# Create your views here.
from django.urls import reverse

from App.forms import RegisterForm
from App.models import Category, User, Article
#路由保护
from Django_Projects import settings




# def safety(func):
#     def inner(*args, **kwargs):
#         if args[0].session.get('username'):
#             return func(*args, **kwargs)
#         else:
#             return redirect('/user/loginb/')
#     return inner




def index(request):
    # username = request.session.get('username')
    # # print(index)
    # if username:
    return render(request, 'index.html', locals())
    # else:
    #     return redirect('/user/loginb/')



def loginb(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            request.session['username'] = user.username
            return redirect('/user/index')

        else:
            return render(request, '飞机.html', {'msg': '用户名或密码错误!'})
    else:
        return render(request, '飞机.html')


def header(request):
    username = request.session.get('username')
    return render(request, 'public_header.html', locals())


def left(request):
    return render(request, 'public_left.html')

#文章管理
def xinwen(request, cid=-1, page=1):
    categories = Category.objects.all()
    #检索分类
    if cid < 0:
        f_categories = categories.first()
        cid = f_categories.cid
    articles = Article.objects.filter(cid=cid)
    #得到POST提交的值
    if(request.method == 'POST'):
        cid = request.POST['cid']
        search = request.POST['search']
        #搜索
        articles = Article.objects.filter(cid=cid, title__contains=search)
    else:
        if cid < 0:
            first_category = categories.first()
            cid = first_category.cid
            articles = Article.objects.filter(cid=cid)
    #分页
    paginator = Paginator(articles, 4)
    #page表示当前页
    pager = paginator.page(page)
    #总的文章个数
    pa_count = paginator.count
    #总的页码
    pa_all = paginator.num_pages
    pa = range(1, pa_all + 1)

    return render(request,'wenzhang_xinwen.html', locals())


def art_del(request,aid, cid=-1, page=1):
    article = Article.objects.get(pk=aid)
    if article:
        article.delete()

    return redirect(reverse("App:xinwen" , kwargs = {'cid': cid, 'page':page}))


# def send_em(request):
#     from App.SMS import sms
#     para = "{'number':%d}"%(randint(1000,100000))
#     print(para)
#     res = sms.send('17753659553',para)
#     print(res.decode("utf-8"))
#     return HttpResponse("ok")

#删除cookie/session
def logout(request):
    res = redirect('/user/loginb/')
    #session 清楚所有键值对
    request.session.clear()
    return res


def content(request, aid):
    articles = Article.objects.filter(aid=aid)
    for article in articles:
        print(article)

    return render(request, 'wenzhangneiirong.html', locals())


def changepaswd(request):
    if request.method == "POST":
        old_upswd = request.POST.get('password1')
        new_upswd = request.POST.get('password2')
        username = request.session.get('username')
        user = auth.authenticate(username=username, password=old_upswd)

        if user:
            user.set_password(new_upswd)
            user.save()

        return redirect(reverse('App:loginb'))

    return render(request,'change_psw.html')



#注册
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop('confirm')
            u = User.objects.filter(username=data['username'])
            if u:
                return render(request,'register.html',{'msg':'用户名已存在'})

            user = User.objects.create_user(**data)
            if user:
                return render(request,'飞机2.html')
        else:
            return render(request,'register.html',{'form':form})

    return render(request,'register.html')

#文本编辑器
def wenbenbianji(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('content'))
    return render(request,'wenbenbianji.html')

#文章修改
def art_pub(request,aid):
    article = Article.objects.filter(aid=aid).first()
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.filter(aid=aid).first()
        article.title = title
        article.content = content
        article.save()
        return redirect('/user/xinwen')

    return render(request,'wenzhnagfabu2.html',locals())


#文章发布
def art_publick(request,cid):

    if request.method == 'POST':
        try:
                f = request.FILES.get('files')
                path = os.path.join(settings.STATICFILES_DIRS[0],'filesss')
                path = os.path.join(path,f.name)
                if f:
                    with open(path,'wb') as target:
                        if f.multiple_chunks():
                            for data in f.chunks():
                                target.write(data)

                        else:
                              target.write(f.read())
                pic = '/static/filesss/' + f.name
                tit = request.POST.get('title')
                con = request.POST.get('content')
                cursor = connection.cursor()
                cursor.execute("insert into article (cid,title,content,picture,create_time) values ('{}','{}','{}','{}',now()) ".format(cid,tit,con,pic))
                return redirect('/user/xinwen/')

        except:
                tit = request.POST.get('title')
                con = request.POST.get('content')
                cursor = connection.cursor()
                cursor.execute("insert into article (cid,title,content,create_time) values ('{}','{}','{}',now()) ".format(cid,tit,con))
                return redirect('/user/xinwen/')
    return render(request,'wenzhang_xinwen_fabu.html', locals())


def charu(request):
    if request.method == 'POST':
        name = request.POST.get('add_name')

        if name:
            try:
                add_car(request, name)
                return redirect('/user/xinwen/')
            except:
                return render(request,'category.html',{'msg1':'分类名重复'})

        name = request.POST.get('del_name')

        if name:
            try:
                del_car(request, name)
                return redirect('/user/xinwen/')
            except:
                return render(request,'category.html',{'msg2':'没有这个分类'})

    return render(request,'category.html')

#增加类别
def add_car(request,name):
        Category.objects.create(name=name)

        return redirect('/user/index')


#删除类别
def del_car(request,name):
        category = Category.objects.get(name=name)
        category.delete()

        return redirect('/user/index')






