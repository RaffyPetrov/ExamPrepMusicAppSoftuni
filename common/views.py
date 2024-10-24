from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from ExamPreparation.utils import get_user_obj
from albums.models import Albums
from profiles.forms import ProfileCreateForm


class HomePage(ListView, BaseFormView):
    model = Albums
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_obj()
        return context

    def get_template_names(self):
        profile = get_user_obj()  # None or QuerySet

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
