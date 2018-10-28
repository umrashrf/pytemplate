from setuptools import setup, find_packages


setup(
    name='bot',
    version='1.0.0',
    description='Template python cli project with use of tkinter and subprocess',
    author='Umair Ashraf',
    author_email='umrashrf@gmail.com',
    url='https://github.com/umrashrf/pytemplate',
    packages=find_packages(),
    install_requires=[
        'Click>=7.0',
        'django-environ>=0.4.5',
    ],
    data_files=[
        ('config', ['config/logging.ini'])
    ]
)
