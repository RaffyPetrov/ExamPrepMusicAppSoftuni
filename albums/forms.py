from django import forms

from ExamPreparation.mixins import PlaceholderMixin, ReadOnlyMixin
from albums.models import Albums


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Albums
        exclude = ('owner', )


class AlbumCreateForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumEditForm(PlaceholderMixin, AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'genre', 'price', 'description']
