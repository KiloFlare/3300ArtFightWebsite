from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import *


# Page View Functions
def index(request):
    # Render the HTML template index.html with the data in the context variable.
   return render( request, 'artfight_app/index.html')

def recent(request):
   #Get all students
   art_list = IndividualArt.objects.all()

   print("Arts Query Set", art_list)
   return render(request, 'artFight_app/recent.html', {'art_list':art_list})

#Detail Page Functions
class individualArtView(generic.DetailView):
    model = IndividualArt

#Forms Functions
def uploadArtForm(request):
   if request.method == 'POST':
        form = UploadArt(request.POST, request.FILES)
        if form.is_valid():
            # create a new `Band` and save it to the db
            newArt = form.save()

            newArt.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return HttpResponseRedirect(reverse('individualArt-detail', args=(newArt.id,)))

   else:
      form = UploadArt()

   return render(request,
               'artFight_app/form_art_upload.html',
               {'form': form})