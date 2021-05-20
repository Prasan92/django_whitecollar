from django.shortcuts import render
from appone.forms import FormName
from appone.models import User

# Create your views here.
def index(request):
    return render(request,'appone/index.html')


def form_name_view(request):
    form = FormName()

    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("invalid values")
    else:
        print("Error")
    return render(request,'appone/join.html',{'form':form})


def members(request):
    mem_list = User.objects.order_by('name')
    mem_dict = {'members':mem_list}
    return render(request,'appone/members.html',mem_dict)
