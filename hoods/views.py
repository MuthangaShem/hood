from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from hoods.models import Hood

# Create your views here.


class CreateHood(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'location')
    model = Hood


class SingleHood(generic.DetailView):
    model = Hood


class ListHoods(generic.ListView):
    model = Hood