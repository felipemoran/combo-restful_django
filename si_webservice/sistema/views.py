# -*- coding: utf-8 -*-

from django.shortcuts import render
import json
from forms import *
from models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


def cadastrar(request):
    print '*** Cadastrar ***'
    resposta = {}
    resposta['texto'] = 'Entrou em cadastrar'

    return HttpResponse(json.dumps(resposta), content_type="application/json")

@api_view(['POST','GET','PUT','DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly, ))
def teste(request):
    print '*** teste ***'
    resposta = {}
    # resposta['texto'] = 'Entrou em teste'
    # resposta['username'] = request.user.username

    if request.method == 'GET':
        if request.GET.get('chave') == 'valor':
            resposta['texto'] = 'Entrou no if GET e chave = valor'
        else:
            resposta['texto'] = 'Entrou no if GET e chave != valor'

    elif request.method == 'POST':
        if request.POST.get('chave') == 'valor':
            resposta['texto'] = 'Entrou no if POST e chave = valor'
        else:
            resposta['texto'] = 'Entroi no if POST e chave != valor'

    else:
        resposta['texto'] = 'Entrou no else'


    return Response(resposta)
