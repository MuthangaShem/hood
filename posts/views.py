from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic
from braces.views import SelectRelatedMixin
from . import models
from . import forms
from django.contrib.auth import get_user_model

class CreateBusiness(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('business_name', 'business_email', 'hood')
    model = models.Business

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class BusinessDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Business
    select_related = ('user', 'hood')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user___username__iexact=self.kwargs.get('username'))

