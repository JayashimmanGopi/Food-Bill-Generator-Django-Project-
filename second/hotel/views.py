from django.shortcuts import get_object_or_404, redirect, render,HttpResponse,Http404
from hotel.models import item
from hotel.forms import Itemform
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect to homepage if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect to homepage if already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Error in form submission")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# Create your views here.
def homepage(request):
    
    itemlist=item.objects.all()
    context={
      "ITEMLIST":itemlist
    }
    return render(request,'home.html',context)
def detailpage(request,id):
    try:
        detaillist=item.objects.get(id=id)
    except item.DoesNotExist:
        raise Http404("it is not found")
    context={
        "DETAILIST":detaillist
    }
    return render(request,'detail.html',context)

def CreateView(request): #create the function and get request
    if request.method=='POST': #use 'POST' for input store
        item_form=Itemform(request.POST) #create instance("item_form") and request the post
        if item_form.is_valid(): #here we use 'is_valid' for check to valid the data
            dish=item_form.cleaned_data['dish'] #here its clean data assign name dish for dish
            cost=item_form.cleaned_data['cost'] #here its clean data assign name cost for cost
            items=item.objects.create(
                dish=dish,
                cost=cost
            )
            items.save()
            return redirect("homepage")
        else:
            return redirect("Createview")
    else:
        item_form=Itemform()
        context = {
            "form": item_form  
        }
        return render(request, 'create.html', context)
    
def UpdateView(request,id):
    obj=get_object_or_404(item,id=id)
    form=Itemform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    
    context={"form":form}
    return render(request,'update.html',context)

def deleteview(request ,id):
    obj=get_object_or_404(item,id=id)
    obj.delete()
    return redirect("homepage")


        
        

    

