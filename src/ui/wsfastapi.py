from domain import (
    entities,
    valueobjects,
    exceptions,
    services
)

from fastapi import (
    Request,
    FastAPI,
    status
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


def configure_routers(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body})
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: exceptions.DomainBaseException):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=jsonable_encoder({"detail": str(exc)})
        )

    @app.post("/employer", response_model=entities.Employer)
    async def create_employer(employer: entities.Employer) -> entities.Employer:
        return services.create_new_employer(employer)

    @app.get("/employer", response_model=entities.Employer)
    async def get_employer(point: valueobjects.Point) -> entities.Employer:
        return services.get_employer_most_nearest(point)


def create_app():
    app = FastAPI()
    configure_routers(app)
    return app
