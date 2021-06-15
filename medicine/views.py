from django.shortcuts import render, redirect
from medicine.models import Medicine

# Create your views here.
# Create your views here.
def index(request):
    # Get으로 페이지 번호 획득  
    template_name = "medicine/medicine_index.html"
    dates = Medicine.objects.all().order_by("-medicine_dt")[:5]
    content = {'dates':dates}
    return render(request, template_name, content)

def take(request):
    obj = Medicine()
    obj.save()
    return redirect("medicine:index")