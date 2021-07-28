from setuptools import setup

setup(
    name='termUI',
    version='0.1',
    py_modules=['termUI'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        termUI=termUI:cli
    ''',
)

