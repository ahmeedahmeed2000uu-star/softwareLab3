
# from django.shortcuts import render

# def home(request):
#     context ={
#         "course_name":"Software Engineering",
#     }
#     return render(request, "students/home.html",context)
    
#     # return render(request, "students/home.html")
# def about(request):
#     return render(request, "students/about.html")

from datetime import datetime
from django.shortcuts import render

def home(request):
    now = datetime.now()
    hour = now.hour

    # تفاصيل الشروط المأخوذة من الصور
    context = {
        'is_morning': hour < 12,
        'employee_can_enter': hour >= 8,
        'customer_can_enter': hour >= 9,
        'cafe_open': hour >= 9,
    }
def  home(request):
       return render(request, 'students/home.html')    
def about(request):
    return render(request, 'students/about.html')