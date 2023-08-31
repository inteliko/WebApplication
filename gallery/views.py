from django.shortcuts import render, redirect 
from .models import Photo, Category

import random

# Create your views here.


def Base(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base.html', context)


def Portfolio(request):
    categories = Category.objects.all()
    photos_by_category = {}

    for category in categories:
        category_photos = Photo.objects.filter(category=category)
        if category_photos.exists():
            random_photo = random.choice(category_photos)
            if random_photo.image:  # Check if the random_photo has an associated image
                photos_by_category[category] = random_photo

    context = {'photos_by_category': photos_by_category}
    return render(request, 'portfolio.html', context)



# views.py

def CategoryPhotos(request, category_id):
    category = Category.objects.get(id=category_id)
    photos = Photo.objects.filter(category=category)
    context = {'category': category, 'photos': photos}
    return render(request, 'gallery.html', context)




def About(request):
    return render(request, 'about.html')

def Testimonials(request):
    return render(request, 'testimonials.html')

def Service(request):
    return render(request, 'service.html')

def Upload(request):
    return render(request, 'upload.html')


def Contact(request):
    return render(request, 'contact.html')





def Catagories(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    photos = Photo.objects.filter(category=category)
    
    context = {'category': category, 'photos': photos}
    return render(request, 'potrait.html', context)




def Bridal(request, category_name):

    category = get_object_or_404(Category, name=category_name)
    photos = Photo.objects.filter(category=category)
    
    context = {'category': category, 'photos': photos}
    return render(request, 'bridal.html', context)


def Kids(request, category_name):

    category = get_object_or_404(Category, name=category_name)
    photos = Photo.objects.filter(category=category)
    photos = Photo.objects.order_by('-upload_date')[:10]

    
    context = {'category': category, 'photos': photos}
    return render(request, 'kids.html', context)

def Couples(request, category_name):

    category = get_object_or_404(Category, name=category_name)
    photos = Photo.objects.filter(category=category)
    photos = Photo.objects.order_by('-upload_date')[:10]

    
    context = {'category': category, 'photos': photos}
    return render(request, 'kids.html', context)

def Upload(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        # Check if 'category' or 'category_new' is provided
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        # Create a new Photo instance
        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('/')

    context = {'categories': categories}
    return render(request, 'upload.html', context)
