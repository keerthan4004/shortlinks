import qrcode
import io
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save()
            short_url = request.build_absolute_uri(f'/{url.short_code}/')
            return render(request, 'shortener/home.html', {
                'form': URLForm(),
                'short_url': short_url,
                'original_url': url.original_url,
                'short_code': url.short_code,
            })
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)

def generate_qr(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    short_url = request.build_absolute_uri(f'/{url.short_code}/')

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(short_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return HttpResponse(buffer, content_type='image/png')