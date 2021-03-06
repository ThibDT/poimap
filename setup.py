from setuptools import setup, find_packages

setup(name='poimap',
      version='3.2.1',
      description='Manage POI on a map',
      url='https://github.com/atiberghien/poimap',
      author='Alban Tiberghien',
      author_email='alban.tiberghien@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
           'Django<3', ## for django-cms 3.6
           'psycopg2-binary<2.8', #due to https://github.com/divio/django-cms/issues/6666
           "django-compressor",
           "django-sekizai",
           "django-fontawesome-5",
           'django-autoslug',
           'django-countries',
           'djangorestframework',
           'djangorestframework-gis',
           'django-treebeard',
           'django-polymorphic<2.1', #for django-filer 1.5
           'django-polymorphic-tree',
           'easy-thumbnails',
           'django-leaflet',
           'shapely',
           'django-ckeditor',
           'django-ckeditor-filer',
           'django-filter',
           'django-bootstrap4',
           'django-admin-sortable2',
           'pyowm',
           'django-easy-select2',
           'django-recurrence',
           'googlemaps',
           'pandas',
           'xhtml2pdf',
           'reportlab',
           'networkx',
      ],
      zip_safe=False)
