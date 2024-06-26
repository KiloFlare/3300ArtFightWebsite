from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .decorators import has_permission

#Permissions Testing


# Page View Functions
def index(request):
    # Render the HTML template index.html with the data in the context variable.
   return render( request, 'artfight_app/index.html')

def recent(request):
   #Get all art
   art_list = IndividualArt.objects.all()

   print("Arts Query Set", art_list)
   return render(request, 'artFight_app/recent.html', {'art_list':art_list})

def duelsPage(request):
   #Get all duels
   duel_list = Duel.objects.all()

   print("Duels Query Set", duel_list)
   return render(request, 'artFight_app/duels.html', {'duel_list':duel_list})

#Detail Page Functions
class individualArtView(generic.DetailView):
   model = IndividualArt

class DuelView(generic.DetailView):
   model = Duel

#Forms Functions
@has_permission('create_individualArt')
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

def updateIndividualArtForm(request, id):
    art=get_object_or_404(IndividualArt, pk=id)
    print("Art Get: ", art)

    if request.method == 'POST':
         form = UpdateArt(request.POST, instance=art)

         if form.is_valid():
            #save changes to db
            art.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return HttpResponseRedirect(reverse('individualArt-detail', args=(art.id,)))

    else:
      form = UpdateArt(initial={'title': art.title, 'description':art.description, 'artPiece':art.artPiece, 'user':art.user})
    
    context = {'form': form,'art': art,}
    return render(request,
               'artFight_app/form_art_update.html',
               context)


def deleteIndividualArtForm(request, id):
   art = IndividualArt.objects.get(pk=id)

   if request.method == 'POST':
        # delete the band from the database
        art.delete()
        # redirect to the bands list
        return HttpResponseRedirect(reverse('index'))

    # no need for an `else` here. If it's a GET request, just continue

   return render(request,
                'artFight_app/form_art_delete.html',
                {'art': art})

def uploadDuelForm(request, id):
   #getting individual art instance of the art being attacked
   try:
      defenderArt = IndividualArt.objects.get(pk=id)
   except:
      return HttpResponseRedirect(reverse(''))
       

   if request.method == 'POST':
        form = UploadArt(request.POST, request.FILES)
        if form.is_valid():
            # create a new `IndivdualArt` and save it to the db
            newArt = form.save()

            newArt.save()

            #make new Duel and save to db
            newDuel = Duel(artOne = newArt, artTwo = defenderArt, title = newArt.title + " VS " + defenderArt.title)

            newDuel.save()

            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return HttpResponseRedirect(reverse('duel-detail', args=(newDuel.id,)))

   else:
      form = UploadArt()

   return render(request,
               'artFight_app/form_art_upload.html',
               {'form': form})