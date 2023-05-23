from __future__ import absolute_import

from django.db import models
from django.db.models import ImageField, FileField
from django import forms
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from .forms import FilesFormField, BaseFilesWidget, FilesWidget, ImagesWidget
from topnotchdev.files_widget import controllers
from .settings import *


def formfield_defaults(field, default_widget=None, widget=None, form_class=FilesFormField, required=True, **kwargs):
    if widget is None or not issubclass(widget, BaseFilesWidget):
        if default_widget is None:
            raise ImproperlyConfigured('Widget class is not set for field `{0}`'.format(field))
        else:
            widget = default_widget

    defaults = {
        'form_class': FilesFormField,
        'fields': (forms.CharField(required=required), forms.CharField(required=False), forms.CharField(required=False), ),
        'widget': widget(field.model._meta.app_label, field.model._meta.model_name),
    }
    defaults.update(kwargs)

    return defaults


def save_all_data(self, instance, data):
    # Save old data to know which images are deleted.
    # We don't know yet if the form will really be saved.
    old_data = getattr(instance, self.name)
    setattr(instance, OLD_VALUE_STR % self.name, old_data)
    setattr(instance, DELETED_VALUE_STR % self.name, data.deleted_files)
    setattr(instance, MOVED_VALUE_STR % self.name, data.moved_files)


class FilesField(models.TextField):
    description = _("Files")
    attr_class = controllers.FilePaths

    def __init__(self, verbose_name=None, name=None, upload_to='', *args, **kwargs):
        self.upload_to = upload_to
        super(FilesField, self).__init__(verbose_name, name, *args, **kwargs)

    def contribute_to_class(self, cls, name, virtual_only=False):
        super(FilesField, self).contribute_to_class(cls, name)
        setattr(cls, self.name, controllers.FilesDescriptor(self))

    def save_form_data(self, instance, data):
        save_all_data(self, instance, data)
        super(FilesField, self).save_form_data(instance, data)

    def formfield(self, default_widget=FilesWidget, **kwargs):
        defaults = formfield_defaults(self, default_widget, **kwargs)
        return super(FilesField, self).formfield(**defaults)


class ImagesField(FilesField):
    description = _("Images")
    attr_class = controllers.ImagePaths

    def formfield(self, default_widget=ImagesWidget, **kwargs):
        return super(ImagesField, self).formfield(default_widget=default_widget, **kwargs)
