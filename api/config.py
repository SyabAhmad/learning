class Config:
    """Flask configuration"""
    DEBUG = True
    SECRET_KEY = 'your-secret-key-here'
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development specific configuration"""
    ENV = 'development'
    DEBUG = True

class ProductionConfig(Config):
    """Production specific configuration"""
    ENV = 'production'
    DEBUG = False