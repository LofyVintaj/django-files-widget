from django import forms
from django.utils import six
from django.template.loader import render_to_string

from topnotchdev.files_widget.settings import *


class VisibleHiddenInput(forms.HiddenInput):
    is_hidden = False


class BaseFilesWidget(forms.MultiWidget):
    def __init__(self,
                 app_name,
                 model_name,
                 multiple=False,
                 preview_size=150,
                 template="files_widget/files_widget.html",
                 widgets=tuple([VisibleHiddenInput]*3),
                 **kwargs):
        super(BaseFilesWidget, self).__init__(widgets, **kwargs)
        self.app_name = app_name
        self.model_name = model_name
        self.multiple = multiple
        self.preview_size = preview_size
        self.template = template

    class Media:
        js = [
            JQUERY_PATH,
            JQUERY_UI_PATH,
            'files_widget/js/jquery.iframe-transport.js',
            'files_widget/js/jquery.fileupload.js',
            'files_widget/js/widgets.js',
        ]

        css = {
            'all': (
                'files_widget/css/widgets.css',
            ),
        }

    def decompress(self, value):
        if value:
            return [value, '', '', ]
        return ['', '', '', ]

    def render(self, name, value, attrs=None, renderer=None):
        if not isinstance(value, list):
            value = self.decompress(value)
        files, deleted_files, moved_files = value

        context = {
            'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL,
            'add_image_by_url': ADD_IMAGE_BY_URL,
            'input_string': super(BaseFilesWidget, self).render(name, value, attrs, renderer),
            'name': name,
            'files': files,
            'deleted_files': deleted_files,
            'multiple': self.multiple and 1 or 0,
            'preview_size': six.text_type(self.preview_size),
            'app_name': self.app_name,
            'model_name': self.model_name,
        }
        return render_to_string(self.template, context)


class FilesWidget(BaseFilesWidget):
    def __init__(self, app_name, model_name,  multiple=True, preview_size=64, **kwargs):
        super(FilesWidget, self).__init__(app_name, model_name, multiple, preview_size, **kwargs)


class ImagesWidget(BaseFilesWidget):
    def __init__(self, app_name, model_name,  multiple=True, preview_size=150, **kwargs):
        super(ImagesWidget, self).__init__(app_name, model_name, multiple, preview_size, **kwargs)
