from django.shortcuts import render
from .extract_color import extract_colors
from .models import StripFile
from .forms import UploadStripForm
# Create your views here.

def upload_image(request):
    '''
    User uploads image and gets back dictionary of rgb values
    '''
    if request.method == 'POST':
        form = UploadStripForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES['file']
            extracted_colors = extract_colors(img)
            urine_strip = StripFile(image=img, color_values=extracted_colors)
            urine_strip.save()

            return render(request, 'color_extract/upload.html', {'extracted_colors': extracted_colors})
        
    else:
        form = UploadStripForm()
    
    return render(request, 'color_extract/upload.html',{"form":form})

