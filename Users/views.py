from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from Users.forms import RegisterForm, LoginForm
from Users.models import UserProfile


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # 判断用户已经登录重定向到index
            return HttpResponseRedirect(reverse("index"))
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # mobile = login_form.cleaned_data["mobile"]
            # email = login_form.cleaned_data["email"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        # if request.session.get('is_login', None):
        #     # 登录状态不允许注册。你可以修改这条原则！
        #     return render(request, "index.html")
        register_form = RegisterForm(request.POST)
        msg = "请检查填写内容"
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            confirm_password = register_form.cleaned_data['confirm_password']

            email = register_form.cleaned_data['email']
            # gender = register_form.cleaned_data['gender']
            mobile = register_form.cleaned_data["mobile"]
            first_name = register_form.cleaned_data["first_name"]
            last_name = register_form.cleaned_data["last_name"]
            if password != confirm_password:  # 判断两次密码是否相同
                msg = "两次输入的密码不同！"
                return render(request, 'register.html', {"msg": msg})
            else:
                same_name_user = UserProfile.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    msg = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', {"msg": msg})
                same_email_user = UserProfile.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    msg = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', {"msg": msg})
                same_email_user = UserProfile.objects.filter(mobile=mobile)
                if same_email_user:  # 手機號碼唯一
                    msg = '该手機號已被注册，请使用别的手機號！'
                    return render(request, 'register.html', {"msg": msg})
                # 当一切都OK的情况下，创建新用户
                new_user = UserProfile.objects.create()
                new_user.username = username
                new_user.password = make_password(password)
                new_user.email = email
                # new_user.gender = gender
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                return HttpResponseRedirect(reverse('login'))  # 自动跳转到登录页面

        return render(request, 'register.html', {"msg": register_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))
