from django.shortcuts import render
import cv2 
import numpy as np
from .extract_color import extract_colors
from .models import StripFile
from .forms import UploadStripForm
# Create your views here.

def upload_image(request):
    '''
    User uploads image and gets back 
    '''
    if request.method == 'POST':
        form = UploadStripForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['file']
            img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_UNCHANGED)

            analyzed_colors = extract_colors(img)
            urine_strip = StripFile(file=image, color_values=analyzed_colors)
            urine_strip.save()
            return render(request, 'home.html', {'analyzed_colors': analyzed_colors})
        
    else:
        form = UploadStripForm()
    
    return render(request, 'color_extract/home.html',{"form":form})

