from conf import settings
from ui import create_app

create_app(settings['ws'])
