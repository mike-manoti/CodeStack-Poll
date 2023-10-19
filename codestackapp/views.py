from django.shortcuts import render

# Create your views here.
def index(resource):
    context ={}
    render(resource, 'index.html', context)

def detail(resource):
    context ={}
    render(resource, 'detail.html', context)

def result(resource):
    context ={}
    render(resource, 'result.html', context)

def signin(resource):
    context ={}
    render(resource, 'signin.html', context)

def signup(resource):
    context ={}
    render(resource, 'signup.html', context)
