from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'in9f56=59m!zlqriz%gzava(=-5pi3idprx7f=hd&x8$5ok@sm'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', 'joelw.org', 'localhost']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
