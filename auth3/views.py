from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'login.html')



def register(request):
    return render(request, 'register.html')



def home(request):
    return render(request, 'home.html')


def home(request):
    amal = request.GET.get('amal', '+')
    print(amal)
    son1 = int(request.GET.get('son1', 0))
    son2 = int(request.GET.get('son2', 0))

    if amal == '+':
        natija = son1 + son2
    elif amal == '-':
        natija = son1 - son2
    elif amal == '/':
        natija = son1 / son2
    elif amal == '*':
        natija = son1 * son2
    else:
        natija = 0
    

    context = {
        'user': request.user,
        'course': 'Fintechhub',
        'age': '16',
        'amal': amal,
        'son1': son1,
        'son2': son2,
        'natija': natija
    }


    return render(request, 'home.html', context=context)