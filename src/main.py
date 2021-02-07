from conf import settings
from ui import create_app

app = create_app(settings['application']['ui_mode'])

import uvicorn
uvicorn.run(app)
