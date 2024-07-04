"""
Django settings for sislid project.

Generated by 'django-admin startproject' using Django 3.2.24.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k^y$-a_%iz-54t(#d0-(@+-!^e!94%7az(ehzdw)%u1jk-0xz&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://*.serveo.net',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'cadastro',
    'gabineteOnline',
    'blogZito',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sislid.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'static/templates')],
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

WSGI_APPLICATION = 'sislid.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'pt-br'  # Define o idioma padrão para português brasileiro

TIME_ZONE = 'America/Sao_Paulo'  # Define o fuso horário para América/São_Paulo

USE_I18N = True  # Habilita a internacionalização

USE_L10N = True  # Habilita a localização

USE_TZ = True  # Habilita o suporte a fuso horário

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # título da janela (padrão: current_admin_site.site_title se ausente ou None)
    "site_title": "SISLID",

    # Título na tela de login (máx. 19 caracteres) (padrão: current_admin_site.site_header se ausente ou None)
    "site_header": "SISLID",

    # Título da marca (máx. 19 caracteres) (padrão: current_admin_site.site_header se ausente ou None)
    "site_brand": "SISLID",

    # Logotipo para usar no seu site, deve estar presente em arquivos estáticos, usado para a marca no canto superior esquerdo
    "site_logo": "img/logo.png",

    # Logotipo para usar no formulário de login (padrão: site_logo)
    "login_logo": "img/logo2.png",

    # Logotipo para usar no formulário de login em temas escuros (padrão: login_logo)
    "login_logo_dark": "img/logo2.png",

    # Classes CSS que são aplicadas ao logotipo acima
    "site_logo_classes": "img-circle",

    # Caminho relativo para um favicon para seu site, padrão: site_logo se ausente (idealmente 32x32 px)
    "site_icon": "img/logo.png",

    # Texto de boas-vindas na tela de login
    "welcome_sign": "Bem-vindo ao SISLID",

    # Direitos autorais no rodapé
    "copyright": "Desenvolvido por Beatriz Machado",

    # Lista de administrações de modelos para pesquisar na barra de pesquisa, barra de pesquisa omitida se excluída
    # Se você deseja usar um único campo de pesquisa, não precisa usar uma lista, pode usar uma string simples
    # "search_model": ["lideranca"],

    # Nome do campo no modelo de usuário que contém avatar ImageField/URLField/Charfield ou um chamável que recebe o usuário
    "user_avatar": None,

    #############
    # Menu do Usuário #
    #############

    # Links adicionais para incluir no menu do usuário no canto superior direito (tipo de url "app" não é permitido)
    "usermenu_links": [
        {"name": "Suporte", "url": "https://api.whatsapp.com/send?phone=5521991986769&text=", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Menu Lateral #
    #############

    # Se deve exibir o menu lateral
    "show_sidebar": True,

    # Se deve expandir automaticamente o menu
    "navigation_expanded": True,

    # Ocultar esses aplicativos ao gerar o menu lateral (por exemplo, auth)
    "hide_apps": [],

    # Ocultar esses modelos ao gerar o menu lateral (por exemplo, auth.user)
    "hide_models": [],

    # Lista de aplicativos (e/ou modelos) para basear a ordem do menu lateral (não precisa conter todos os aplicativos/modelos)
    "order_with_respect_to": ["cadastro","blogZito", "gabineteOnline"],


    # Ícones personalizados para aplicativos/modelos do menu lateral Veja https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # para a lista completa de classes de ícones gratuitas 5.13.0
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Ícones usados quando um não é especificado manualmente
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "topmenu_links": [
        {"name": "Início", 
         "url": "admin:index", 
         "permissions": ["auth.view_user"]},
        {
            "name": "Análises",
            "url": "https://metabase.sislid.net",
            "new_window": True,
            "permissions": ["auth.view_user"],  
        },
        {
            "name": "Site",
            "url": "/blog/home",
            "new_window": True,
            "permissions": ["auth.view_user"],  
        },
    ],

    #################
    # Modal Relacionado #
    #################
    # Usar modais em vez de pop-ups
    "related_modal_active": False,

    #############
    # Ajustes de UI #
    #############
    # Caminhos relativos para scripts CSS/JS personalizados (devem estar presentes em arquivos estáticos)
    "custom_css": None,
    "custom_js": None,
    # Se deve vincular fonte de fonts.googleapis.com (use custom_css para fornecer fonte caso contrário)
    "use_google_fonts_cdn": True,
    # Se deve mostrar o personalizador de IU na barra lateral
    "show_ui_builder": False,

    ###############
    # Formato de Visualização #
    ###############
    # Renderizar a visualização de alteração como um único formulário ou em guias, as opções atuais são
    # - single
    # - horizontal_tabs (padrão)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "single",

    
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-teal",
    "accent": "accent-teal",
    "navbar": "navbar-teal navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-olive",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "flatly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-outline-danger",
        "success": "btn-success"
    }
}