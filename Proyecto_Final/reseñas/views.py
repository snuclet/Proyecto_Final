from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.shortcuts import render

from reseñas.forms import ReseñaForm
from reseñas.models import Reseña

def get_reseña(request):
    courses = Reseña.objects.all()
    paginator = Paginator(courses, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

def reseña(request):
    return render(
        request=request,
        context={"reseña_list": get_reseña(request)},
        template_name="reseña/reseña_list.html",
    )

