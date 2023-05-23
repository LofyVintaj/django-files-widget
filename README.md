django-files-widget
===================

Django AJAX form widgets and model fields for multiple files/images upload with progress bar

__This is currently an alpha release. Not all functionality is there, only `ImagesField` have been implemented and there is not yet enough error handling.__

Features
--------

- Drag &amp; drop file uploading via AJAX
- Plus 2 other ways to add files: upload button or by URL
- Uploading multiple files at once
- Upload progress bar
- 2 model fields with corresponding form fields and widgets: `ImagesField` and `FilesField`
- Image gallery widget with drag &amp; drop reordering
- Integrates with Django Admin, [Grappelli](https://github.com/sehmaschine/django-grappelli) 

Screenshots
-----------

<table>
  <tr>
    <td>
      <img alt="File drag & drop to ImagesWidget in Django Admin" src="/topnotchdev/files_widget/static/docs/img/admin-images-widget-drop.jpg" width="350" />
    </td>
    <td>
      <img alt="Ajax upload progress bar in ImagesWidget in Django Admin" src="/topnotchdev/files_widget/static/docs/img/admin-images-widget-progress.jpg" width="350" />
    </td>
  </tr>
  <tr>
    <td>File drag & drop to ImagesWidget in Django Admin</td>
    <td>Ajax upload progress bar in ImagesWidget in Django Admin</td>
  </tr>
</table>

Quick Start
-----------

### Requirements ###

- Django 1.5 or later
- [sorl-thumbnail](https://github.com/sorl/sorl-thumbnail)
- [Pillow](https://github.com/python-imaging/Pillow) (or PIL)
- jQuery 1.7 or later
- jQuery UI (included)
- [jQuery File Upload](https://github.com/blueimp/jQuery-File-Upload) (included)

### Install ###

    pip install git+git://github.com/dellax/django-files-widget

### In `settings.py` ###

    INSTALLED_APPS = (
        ...,
        'sorl.thumbnail',
        'topnotchdev.files_widget',
        ...,
    )
    
    MEDIA_URL = ...
    MEDIA_ROOT = ...
    THUMBNAIL_DEBUG = False
    
(Optional) basic settings with their defaults:

    FILES_WIDGET_JQUERY_PATH         # (jQuery 2.2.4 from Google)
    FILES_WIDGET_JQUERY_UI_PATH      # (jQuery UI 1.11.4 from Google)
    FILES_WIDGET_IMAGE_QUALITY       # 50

### In `urls.py` ###

    url(r'^files-widget/', include('topnotchdev.files_widget.urls')),

### In `models.py` ###

    from topnotchdev import files_widget
  
    class MyModel(models.Model):
        images = files_widget.ImagesField()

### Django Auth User Permissions (optional) ###

    files_widget.can_upload_files

### Template Usage Examples ###

No extra steps are required to use the widget in your Admin site. Here are some examples of displaying files and (thumbnail) images on your site:

A list of linked thumbnails:

    {% for img in my_instance.images.all %}
        <a src="{{ img.url }}">
            {{ img.thumbnail_tag_100x100 }}
            <span class="caption">{{ img.filename }}</span>
        </a>
    {% endfor %}

Only the next image:

    {{ my_instance.images.next.img_tag }}

The filename without extension and underscores of the next 3 (or n) images:

    {% for img in my_instance.images.next_3 %}
        {{ img.display_name }}
    {% endfor %}

Or other attributes:

    {{ my_instance.image.url }}
    {{ my_instance.image.filename }}
    {{ my_instance.image.local_path }} (just as an example)
    {{ my_instance.image.exists }}
    {{ my_instance.image.get_size }}
    {{ my_instance.image.thumbnail_64x64.url }}
    ...

License
-------

MIT

Credits
-------

- [jQuery File Upload](https://github.com/blueimp/jQuery-File-Upload/wiki/Options)
- [Tutorial on jQuery Filedrop](http://tutorialzine.com/2011/09/html5-file-upload-jquery-php/) by Martin Angelov
- [Tutorial on Django AJAX file upload](http://kuhlit.blogspot.nl/2011/04/ajax-file-uploads-and-csrf-in-django-13.html) by Alex Kuhl
- [Answer on non-Model user permissions](http://stackoverflow.com/questions/13932774/how-can-i-use-django-permissions-without-defining-a-content-type-or-model) on Stackoverflow


API Documentation
=================

(Under construction)

Navigation
----------

### Settings

- [`FILES_WIDGET_FILES_DIR`](#FILES_WIDGET_FILES_DIR)
- [`FILES_WIDGET_JQUERY_PATH`](#FILES_WIDGET_JQUERY_PATH)
- [`FILES_WIDGET_JQUERY_UI_PATH`](#FILES_WIDGET_JQUERY_UI_PATH)

### Model Fields

- [`files_widget.FilesField()`](#FilesField)
- [`files_widget.ImagesField()`](#ImagesField)

### Model Field Options

- [`upload_to`](#upload_to) (only string values supported now)
- [`max_length`](#max_length)

### FilesField and ImagesField Instance Attributes

- [`splitlines()`](#splitlines)
- [`all()`](#all)
- [`count()`](#count)
- [`first()`](#first)
- [`last()`](#last)
- [`next()`](#next)
- [`next_n()`](#next_n)
- [`has_next()`](#has_next)
- [`as_list()`](#as_list) (not yet implemented)
- [`as_gallery()`](#as_gallery) (not yet implemented)
- [`as_carousel()`](#as_carousel) (not yet implemented)

### FilesField, ImagesField Instance Attributes

- [(unicode)](#unicode)
- [`settings`](#settings-attr)
- [`escaped`](#escaped)
- [`url`](#url)
- [`local_path`](#local_path)
- [`filename`](#filename)
- [`display_name`](#display_name)
- [`ext`](#ext)
- [`img_tag()`](#img_tag)
- [`thumbnail()`](#thumbnail)
- [`thumbnail_mxn()`](#thumbnail_mxn)
- [`thumbnail_tag()`](#thumbnail_tag)
- [`thumbnail_tag_mxn()`](#thumbnail_tag_mxn)
- [`exists()`](#exists)
- [`get_size()`](#get_size)
- [`get_accessed_time()`](#get_accessed_time)
- [`get_created_time()`](#get_created_time)
- [`get_modified_time()`](#get_modified_time)

### Static Files Inclusion

- [`form.media`](#form.media)
- [`files_widget/media.html`](#media.html) (not yet implemented)
- [Manual](#manual-inclusion)

### Signal Handlers

- [`post_save`](#django.post_save)
