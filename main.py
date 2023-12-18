from fastapi.middleware.cors import CORSMiddleware
import fastapi
import uvicorn
from config.config import RELOAD, SERVER_HOST, SERVER_PORT, SERVER_WORKERS, UVICORN_LOG_LEVEL, ALLOWED_ORIGINS
from utils.startup import init
from api.user import userrouter
from api.reportendpoint import reportrouter


def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI()  # type: ignore
    app.include_router(userrouter)
    app.include_router(reportrouter)
    app.add_middleware(CORSMiddleware,
                       allow_origins=ALLOWED_ORIGINS,
                       # allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
                       # allow_methods=settings.ALLOWED_METHODS,
                       # allow_headers=settings.ALLOWED_HEADERS,
                       )

    # app.add_event_handler(
    #     "startup",
    #     execute_backend_server_event_handler(backend_app=app),
    # )
    # app.add_event_handler(
    #     "shutdown",
    #     terminate_backend_server_event_handler(backend_app=app),
    # )

    # app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)
    return app


app: fastapi.FastAPI = initialize_backend_application()

if __name__ == "__main__":
    init()
    uvicorn.run(app="main:app",
                host=SERVER_HOST,
                port=SERVER_PORT,
                reload=RELOAD,
                workers=SERVER_WORKERS,
                log_level=UVICORN_LOG_LEVEL.lower(),
                )
