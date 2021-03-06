import os
from distutils.core import setup

setup(name='_',
    author='Thomas Levine',
    author_email='_@thomaslevine.com',
    description='Microblogging',
   #url='https://github.com/tlevine/_.thomaslevine.com.git',
    url='https://git.thomaslevine.com/_.thomaslevine.com',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['microblog_email','microblog_web'],
    scripts=[os.path.join('bin','_')],
    install_requires = ['bottle'],
    tests_require = ['nose'],
    version='0.0.1',
    license='AGPL'
)
