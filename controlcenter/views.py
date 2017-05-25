# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import JsonResponse
from controlcenter.models import User
from controlcenter.forms import UserLoginForm, UserStatusForm


def controlcenter_view(request):

    if not request.current_user:
        return redirect('login')

    form = UserStatusForm(instance=request.current_user)
    users = User.objects.all()

    payload = {
        'users': users,
        'current_user': request.current_user,
        'current_user_status': request.current_user.get_status_display(),
        'form': form
    }

    return render(request, 'controlcenter.html', payload)

def login(request):

    if request.current_user:
        return redirect('control_view')

    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        user, status = User.objects.get_or_create(username=cleaned_data['username'])

        response = redirect('control_view')
        response.set_cookie('session_id', user.id)

        return response

    payload = {
        'form': form
    }

    return render(request, 'login.html', payload)

def logout(request):
    response = redirect('login')
    response.delete_cookie('session_id')
    return render(request, 'login.html')


def change_status(request):

    form = UserStatusForm(request.POST, instance=request.current_user)

    if form.is_valid():
        user = form.save()
        return JsonResponse({'status_code': 200, 'status': user.get_status_display()})

    return JsonResponse({'status_code': 400})

def users(request):

    filter = {}
    if request.GET.get('username'):
        filter['username__contains'] = request.GET.get('username')
    if request.GET.get('status'):
        filter['status'] = request.GET.get('status')

    users_list = User.objects.filter(**filter)

    data = []

    for user in users_list:
        data.append({
            'username': user.username,
            'status': user.get_status_display()
        })

    return JsonResponse({'status_code': 200, 'data': data})



def status_change_api(request):
    status = request.GET.get('CurrentStatus')
    session_id = request.GET.get('UniqueID')

    if status and session_id:
        try:
            user = User.objects.get(pk=session_id)
        except User.DoesNotExist:
            return JsonResponse({'status': False})
        else:
            user.status = status
            user.save()
            return JsonResponse({'status': True})
    return JsonResponse({'status': False})

