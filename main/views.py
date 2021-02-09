from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EntradaTeste, UploadImage
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.core.files.storage import FileSystemStorage


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def nova_entrada(request):
    if request.method == "POST":
        form = EntradaTeste(request.POST)
        if form.is_valid():
            messages.info(request, "Entrada Registrada com Sucesso!")
            return redirect("/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request,
                          template_name="main/entrada.html",
                          context={"form": form})

    form = EntradaTeste()
    return render(request=request,
                  template_name="main/entrada.html",
                  context={"form": form})


def upload_photo(request):
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs.FileSystemStorage()
        fs.save(upload_file.name, upload_file)
    return render(request, 'main/upload.html')


@login_required
def cad_home(request):
    return render(request=request,
                  template_name="caddecampo/home.html",
                  context={})  #


def photo_page(request):
    return render(request=request,
                  template_name="main/photo_page.html",
                  context={
                      "foto": Photo.objects.first(),
                  }
                  )  #
