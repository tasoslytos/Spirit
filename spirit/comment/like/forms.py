# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import CommentLike


class LikeForm(forms.ModelForm):

    class Meta:
        model = CommentLike
        fields = []

    def __init__(self, user=None, comment=None, five_stars=None, *args, **kwargs):
        super(LikeForm, self).__init__(*args, **kwargs)
        self.user = user
        self.comment = comment
        self.five_stars = five_stars

    def clean(self):
        cleaned_data = super(LikeForm, self).clean()

        like = CommentLike.objects.filter(user=self.user,
                                          comment=self.comment,five_stars=self.five_stars)

        if like.exists():
            # Do this since some of the unique_together fields are excluded.
            raise forms.ValidationError(_("This like already exists"))

        return cleaned_data

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.user = self.user
            self.instance.comment = self.comment
            self.instance.five_stars = self.five_stars

        return super(LikeForm, self).save(commit)
