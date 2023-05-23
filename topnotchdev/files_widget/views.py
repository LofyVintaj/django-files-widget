from __future__ import absolute_import

from django.http import Http404, HttpResponse
from django.conf import settings
from django.template.loader import render_to_string
from django.core.exceptions import FieldDoesNotExist
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
try:
    from django.db.models.loading import get_model
except ImportError:
    from django.apps import apps
    get_model = apps.get_model

from PIL import Image

import json

from .settings import PROJECT_DIR, IMAGE_QUALITY
from .controllers import ImagePath


def get_file_field(app_label, model_name, field_name):
    real_field_name = field_name.split('-')[-1]
    model = get_model(app_label, model_name)
    try:
        try:
            return model._meta.get_field_by_name(real_field_name)
        except AttributeError:
            return model._meta.get_field(real_field_name)
    except FieldDoesNotExist:
        raise


def upload(request):
    if not request.method == 'POST':
        raise Http404

    response_data = {}
    if request.is_ajax():
        if request.FILES:
            fields = get_file_field(
                request.POST.get('app', None),
                request.POST.get('model', None),
                request.POST.get('field', None)
            )
            try:
                field = fields[0]
            except (TypeError, IndexError):
                field = fields

            files = list(request.FILES.values())[0]
            path = default_storage.save('{}{}/{}'.format(field.upload_to,
                                                         request.user.pk,
                                                         files.name), ContentFile(files.read()))
            try:
                full_path = PROJECT_DIR+'/'+path
                img = Image.open(full_path)
                img.save(full_path, quality=IMAGE_QUALITY)
            except:
                pass
                
            try:
                preview_size = request.POST['preview_size']
            except KeyError:
                preview_size = '64'
            response_data['status'] = True
            response_data['imagePath'] = path
            response_data['thumbnail'] = render_to_string('files_widget/includes/thumbnail.html',
                                                          {'MEDIA_URL': settings.MEDIA_URL,
                                                           'STATIC_URL': settings.STATIC_URL,
                                                           'preview_size': preview_size})

        else:
            response_data['status'] = False
            response_data['message'] = "We're sorry, but something went wrong."

        return HttpResponse(json.dumps(response_data), content_type='application/json')


def thumbnail_url(request):
    if 'img' not in request.GET or 'preview_size' not in request.GET:
        raise Http404
    
    url = ImagePath(request.GET['img']).thumbnail(request.GET['preview_size']).url
    return HttpResponse(url)
