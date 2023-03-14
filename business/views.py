# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Business
from .forms import BusinessForm
from django.contrib import messages

def business_list(request):
    businesses = Business.objects.all()
    print(businesses)
    return render(request, 'list.html', {'businesses': businesses})

def business_detail(request, pk):
    business = get_object_or_404(Business, pk=pk)
    return render(request, 'details.html', {'business': business})

def business_create(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name','')
            messages.info(request, f"Business ({name}) created successfully!")
            return redirect('business_list')
    else:
        form = BusinessForm()
    return render(request, 'form.html', {'form': form})

def business_update(request, pk):
    business = get_object_or_404(Business, pk=pk)
    if request.method == 'POST':
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            form.save()
            messages.info(request, "Business updated successfully!")
            return redirect('business_list')
    else:
        form = BusinessForm(instance=business)
    return render(request, 'form.html', {'form': form})

def business_delete(request, pk):
    business = get_object_or_404(Business, pk=pk)
    name = business.name
    business.delete()
    messages.info(request, f"Business ({name}) deleted successfully!")
    return redirect('business_list')
