from django.shortcuts import render

# Create your views here.

def home(request):
    import datetime
    data=dict()
    time = datetime.datetime.now()
    data["time_of_day"] = time
    print(time)
    return render(request,"home.html", context=data)


