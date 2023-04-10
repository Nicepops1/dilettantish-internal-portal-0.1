import pathlib

class DevConfig:
    SECRET_KEY='dev'
    PASSWORD_SALT = 'dev'
    DATABASE_PATH=pathlib.Path('instance', 'devel.db')
    SQLALCHEMY_DATABASE_URI='sqlite:///' + str(DATABASE_PATH.resolve())

    PATHS = {
        'user_md_files': pathlib.Path('user_md_files'),
        'user_documents': pathlib.Path('user_documents'),
        'user_images': pathlib.Path('user_images'),
    }

    ADMIN = {
        'username': 'admin',
        'password': 'admin',
        'email': 'admin@admin.com'
    }
    
    ROLES = [
        'admin',
        'user'
    ]