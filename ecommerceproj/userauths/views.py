from django.shortcuts import render
from userauths.forms import UserRegisterForm
# Create your views here.

def register_view(request):
    if request.method == "POST":
        print("User Registerd Successfully")
    else:
        print("User Cannot Resiter")


    form = UserRegisterForm()
    context = {'form':form}
    return render(request,"userauths/signup.html",context)