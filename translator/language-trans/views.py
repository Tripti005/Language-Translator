from django.shortcuts import render,HttpResponse,redirect
from PIL import Image
from PIL import Image
import pytesseract
from googletrans import Translator
import os
from translate import Translator
import textblob
from langdetect import detect
from .forms import *

def image_view(request):
 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract' #change path 
            name = request.FILES['image'].name
            image_folder_path = "/Users/bijnis/Documents/translator/images" #change this path 
            path_to_images = image_folder_path+"/"+name
            img = Image.open(path_to_images)
            
            text = pytesseract.image_to_string(img)
            lan=detect(text)
            words=textblob.TextBlob(text)
            
            words=words.translate(from_lang=lan,to=request.POST.get('to_language'))
            return HttpResponse(f"<h1>{words}</h1>")
    else:
        form = ImageForm()
    return render(request, 'image.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')