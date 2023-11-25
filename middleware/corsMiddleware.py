from fastapi.middleware.cors import CORSMiddleware
origins=[
    "http://localhos:4200",
    "http://localhos"
]
cors_config = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}