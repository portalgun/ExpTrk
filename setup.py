

from setuptools import setup

setup(
    name='metatrack',
    version='0.1.0',
    py_modules=['metatrack'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'metatrack = metatrack:tracker',
        ],
    },
)
