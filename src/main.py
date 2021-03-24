from ui.wsfastapi import create_app
import uvicorn


def run():
    app = create_app()
    uvicorn.run(app=app, host='0.0.0.0', port=5000)


run()
