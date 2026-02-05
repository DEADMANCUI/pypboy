from setuptools import setup

setup(
    name='PipBoy',
    version='0.1',
    packages=['game', 'pypboy', 'pypboy.modules', 'pypboy.modules.map', 'pypboy.modules.boot', 'pypboy.modules.data',
              'pypboy.modules.items', 'pypboy.modules.radio', 'pypboy.modules.stats', 'pypboy.modules.passcode',
              'objloader'],
    url='www.zapwizard.com',
    license='MIT',
    author='ZapWizard',
    author_email='zapwizard@gmail.com',
    description='Pypboy 3000 MK IV',
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'License :: OSI Approved :: MIT License',
    ]
)
