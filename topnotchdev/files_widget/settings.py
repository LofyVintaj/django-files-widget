from django.conf import settings

#FILES_DIR = getattr(settings, 'FILES_WIDGET_FILES_DIR', 'uploads/files_widget/')
OLD_VALUE_STR = getattr(settings, 'FILES_WIDGET_OLD_VALUE_STR', 'old_%s_value')
DELETED_VALUE_STR = getattr(settings, 'FILES_WIDGET_DELETED_VALUE_STR', 'deleted_%s_value')
MOVED_VALUE_STR = getattr(settings, 'FILES_WIDGET_MOVED_VALUE_STR', 'moved_%s_value')
JQUERY_PATH = getattr(settings, 'FILES_WIDGET_JQUERY_PATH', '//ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js')
JQUERY_UI_PATH = getattr(settings, 'FILES_WIDGET_JQUERY_UI_PATH', '//ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js')
ADD_IMAGE_BY_URL = getattr(settings, 'FILES_WIDGET_ADD_IMAGE_BY_URL', True)
MAX_FILESIZE = getattr(settings, 'FILES_WIDGET_MAX_FILESIZE', 0)
FILE_TYPES = getattr(settings, 'FILES_WIDGET_FILE_TYPES', None)
USE_TRASH = getattr(settings, 'FILES_WIDGET_USE_TRASH', False)
TRASH_DIR = getattr(settings, 'FILES_WIDGET_TRASH_DIR', 'uploads/trash/files_widget/')
IMAGE_QUALITY = getattr(settings, 'FILES_WIDGET_IMAGE_QUALITY', 50)
PROJECT_DIR = getattr(settings, 'MEDIA_ROOT', '')

