from django.shortcuts import render
from .forms import uploadfileform

# Create your views here.
def upload_file(request):
    if request.method == "POST":
       form = uploadfileform(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return render(request, 'upload.html')  
    else:
        form = uploadfileform()
    return render(request, 'upload.html', {'form': form})    
        