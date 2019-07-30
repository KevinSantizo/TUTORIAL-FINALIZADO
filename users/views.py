from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
# Create your views here.


def register_user(request):
    template = 'users/form_user.html'
    return render(request, template)


