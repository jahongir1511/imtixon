from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import AddReviewForm, ReviewUpdateForm
from .models import Dorilar, Review, CategoryDorilar

class DoriListView(View):
    def get(self, request):
        dorilar = Dorilar.objects.all().order_by('-id')
        return render(request, 'dori/dori_list.html', {'dori': dorilar})

class DoriDetailView(View):
    def get(self, request, pk):
        dori = Dorilar.objects.get(pk=pk)
        reviews = Review.objects.filter(dori=pk)
        category_dorilar = Dorilar.objects.filter(category=dori.category.pk)
        context = {
            'dori': dori,
            'reviews': reviews,
            'category_dorilar': category_dorilar
        }
        return render(request, 'dori/dori_detail.html', context=context)

class DoriCreateView(CreateView):
    model = Dorilar
    template_name = 'dori/dori_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:dori-list')

class DoriDeleteView(DeleteView):
    model = Dorilar
    template_name = 'dori/dori_delete.html'
    success_url = reverse_lazy('products:dori-list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        dori = Dorilar.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'dori': dori,
            'add_review_form': add_review_form
        }
        return render(request, 'dori/add_review.html', context=context)

    def post(self, request, pk):
        dori = Dorilar.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                dori=dori,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )
            review.save()
            messages.success(request, "Review added successfully.")
            return redirect('products:dori-detail', pk=pk)
        else:
            messages.error(request, "Failed to add review. Please check the form.")
            return render(request, 'dori/add_review.html', {'dori': dori, 'add_review_form': add_review_form})

class ReviewUpdateView(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(instance=review)
        context = {
            'update_review_form': update_review_form
        }
        return render(request, 'dori/review_update.html', context=context)

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(request.POST, instance=review)
        if update_review_form.is_valid():
            update_review = update_review_form.save(commit=False)
            update_review.dori_id = review.dori_id
            update_review.save()
            return redirect('products:dori-detail', pk=review.dori_id)
        else:
            return render(request, 'dori/review_update.html', {'update_review_form': update_review_form})

class CategoriesListView(View):
    def get(self, request):
        categories = CategoryDorilar.objects.all()
        return render(request, 'dori/products.html', {'categories': categories})
