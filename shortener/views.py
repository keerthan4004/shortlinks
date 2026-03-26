from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from .forms import URLForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            short_url = request.build_absolute_url(f'/{url.short_code}/')
            return render(request, 'shortener/home.html', {
                'form' : URLForm(),
                'short_url' : short_url,
                'original_url' : url.original_url,
            })
    else:
        form = URLForm()
        return render(request, 'shortener/home.html', {'form':form})

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)