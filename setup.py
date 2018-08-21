from setuptools import setup, find_packages

setup(name='poimap',
      version='2.4.3',
      description='Manage POI on a map',
      url='https://github.com/atiberghien/poimap',
      author='Alban Tiberghien',
      author_email='alban.tiberghien@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
           'psycopg2-binary',
           'Django<2.0',
           "django-compressor",
           "django-sekizai",
           'django-autoslug',
           'django-countries',
           'djangorestframework',
           'djangorestframework-gis',
           'django-treebeard',
           'django-polymorphic',
           'django-polymorphic-tree',
           'easy-thumbnails',
           'django-leaflet',
           'django-fontawesome',
           'shapely',
           'django-ckeditor',
           'django-ckeditor-filer',
           'django-filter==1.1.0',
           'django-bootstrap4',
           'django-admin-sortable2',
           'pyowm',
           'django-easy-select2',
           'django-recurrence',
           'googlemaps',
           'pandas==0.22.0',
           'xhtml2pdf',
           'reportlab',
           'networkx',
      ],
      zip_safe=False)
