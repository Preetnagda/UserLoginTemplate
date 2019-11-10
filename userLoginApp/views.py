from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect(userLoggedIn)

    if request.method == "POST":
        user = authenticate(username=request.POST.get("username",""),password=request.POST.get("password",""))
        if user is not None :
            login(request,user)
            return redirect(userLoggedIn)
        else:
            context = {"auth" : 1}
            return render(request,"loginPage.html",context)
    return render(request,"loginPage.html")

def logout_user(request):
    logout(request)
    return redirect(login_user)

def userLoggedIn(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request,"indexAdmin.html")
        else:
            return render(request,"indexStaff.html")
    else:
        return redirect(login_user)
