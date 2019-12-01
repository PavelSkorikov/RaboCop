# загрузка базовых настроек для локального окружения
try:
    from RaboCop.settings.base_settings import *
except ImportError:
    raise Exception('Please create base_settings.py file')

# загрузка настроек rest_framework
try:
    from RaboCop.settings.rest_settings import *
except ImportError:
    raise Exception('Please create rest_settings.py file')

# загрузка настроек для разрешения всех кросдоменных запросов
try:
    from RaboCop.settings.corsheaders_settings import *
except ImportError:
    raise Exception('Please create corsheaders_settings.py file')