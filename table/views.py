from django.shortcuts import render
import json
import requests
from .forms import UrlForm
# Create your views here.
def show_table(request):
    web_dta = requests.get('https://www.w3schools.com/angular/customers.php')
    json_dict = web_dta.json()
    key = tuple(json_dict.keys())[0]
    #print(json_dict,type(json_dict),key)
    json_dict1=json_dict[key]
    print(json_dict,json_dict1,type(json_dict1))
    return render(request,'disp_tables.html',{'json_dict1':json_dict1, 'key':key})

def home(request):
    chk=False
    if request.method =='POST':
        form=UrlForm(request.POST)
        if form.is_valid():
            chk=True
            cd=form.cleaned_data
            web_dta = requests.get(cd['url'])
            json_dict = web_dta.json()
            key = tuple(json_dict.keys())[0]
            #print(json_dict,type(json_dict),key)
            json_dict1=json_dict[key]
            print(json_dict,json_dict1,type(json_dict1))
            return render(request,'disp_tables.html',{'json_dict1':json_dict1, 'key':key})
    else:
        form=UrlForm()
        return render(request,'forms.html',{'form':form,'chk':chk})
