
from setuptools import setup

setup(
    name='exptrk',
    version='0.1',
    py_modules=['exptrk'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        exptrk=exptrk:cli
    ''',
)

