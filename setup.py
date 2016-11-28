from setuptools import setup

setup(name='ujson_drf',
      version='0.1',
      description='JSON Renderer and Parser for Django Rest Framework using the ultra fast json (in C).',
      url='https://github.com/akshaysharma096/ujson_drf',
      author='Akshay Sharma',
      author_email='mailbag.akshay@gmail.com',
      license='MIT',
      packages=['ujson_drf'],
      install_requires=[
          'ujson',
          'django',
          'djangorestframework'
      ],
      classifiers=['Framework :: Django', 'Programming Language :: Python',
                   'Intended Audience :: Developers', 'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='django djangorestframework restframework djangorest parser renderer',
      zip_safe=False)
