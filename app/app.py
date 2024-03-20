from app.config.app import get_app
from app.middlewares.appMiddleware import init_middleware
from app.config.routes import init_routes

"""Inicializing app"""
app = get_app()

"""Inicializing middlewares"""
init_middleware(app)

"""Inicializing routes"""
init_routes(app)
