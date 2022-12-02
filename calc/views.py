


from django.shortcuts import render

def employeeform(request):
    data={}
    try:
        if request.method=="POST":
            name=request.POST.get("name")
            password=request.POST.get("password")
            address=request.POST.get("address")
            state=request.POST.get("state")
            gender=request.POST.get("gender")
            vehicle=request.POST.getlist("vehicle[]")
            salary=int(request.POST.get("salary"))
            dob=request.POST.get("dob")

            data={
                "name":name,  
                "password":password,
                "address":address,
                "state":state,
                "gender":gender,
                "vehicle":vehicle,
                "salary":salary,
                "dob":dob
            }
            print(data)
    except:
        pass
    return render(request, "index.html", data)