"""
Django settings for Xiao_bai project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#把apps作为app搜索目录
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

#把xadmin作为后台的搜索目录
sys.path.insert(1, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'un$s8)4*gp2s7@^dfx1m5(n7ivu67ws*2c3e2pdf=-cf9&rhye'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',#用户apps
    'xadmin',#xadmin后台apps
    'apps.novel', #小说的封面章节信息apps
    'crispy_forms',#xadmin后台apps
    'captcha', #验证码
    'apps.author', #作者app
    'apps.homes', #主页app
    'pure_pagination', #实现分页功能app
    'taggit', #实现便签功能
]

AUTH_USER_MODEL = 'users.UserProfile' #重载自定义的用户表

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Xiao_bai.urls' 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Xiao_bai.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xiaobaidu',
        'USER': 'root',
        'PASSWORD': '654321',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'zh-hans' #语言改为中文

# TIME_ZONE = 'UTC'

TIME_ZONE = 'Asia/Shanghai' #时间改为中国上海

USE_I18N = True 

USE_L10N = True

# USE_TZ = True
USE_TZ = False #改为False,让django使用本地时间

#格式化后台内容的显示时间
USE_L10N = False
DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    (os.path.join(BASE_DIR, 'static')),
]

MEDIA_ROOT = os.path.join(BASE_DIR,'Banner')
MEDIA_URL = '/Banner/'

#定义邮箱账号密码
EMAIL_HOST = "mail.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "12345678@sina.com"
EMAIL_HOST_PASSWORD = "12345678"
EMAIL_USE_TLS= False
EMAIL_FROM = "12345678@sina.com"

