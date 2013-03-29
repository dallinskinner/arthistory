from study_helper.models import Artwork, Artist, Category
from django.shortcuts import render

def art(r):
	artworks = Artwork.objects.all().order_by('?')

	return render(r, 'art.html', locals())

def artist(r):
	artists = Artist.objects.all().order_by('?')

	return render(r, 'artist.html', locals())

def category(r):
	categories = Category.objects.all()

	return render(r, 'category.html', locals())

def timeline(r):
	artworks = Artwork.objects.all().order_by('year')

	return render(r, 'timeline.html', locals())

def unit(r, unit):
	artworks = Artwork.objects.filter(unit=unit)

	return render(r, 'art.html', locals())