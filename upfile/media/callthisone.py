from django.shortcuts import redirect, render

# SMA code will go here!!!

def callthisfunc(request):
    dict = {'hello': 'hellofellas'}
    print("finalllyyyyy")
    print(dict)
    return render(request, 'upfile/show.html', dict)