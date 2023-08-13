from django.shortcuts import render,redirect
from .models import produit,demande
# Create your views here.
def produits (request):
    
    return render(request,'produits.html',{'pro':produit.objects.filter(active=True,pack=False)})

def promotions (request):
    return render(request,'promotions.html',{'promo':produit.objects.filter(active=True,promo=True)})

def packs (request):
    return render(request,'packs.html',{'pack':produit.objects.filter(active=True,pack=True)})

def form (request,id):
    if request.method=='POST':
        demande(nomprenom=request.POST.get('nom'),num=request.POST.get('num'),pro=request.POST.get('pro'),adress=request.POST.get('add')).save()
        return redirect('produit')
    return render(request,'formulaire.html',{'remp':produit.objects.get(id=id)})

def details (request,id):

    return render(request,'detail.html',{'det':produit.objects.get(id=id)})

def achat (request):

    return render(request,'achat.html',)

