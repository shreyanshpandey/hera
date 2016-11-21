from setuptools import find_packages, setup
setup(
    name='heraspy2',
    version='0.0',
    description='Callback for streaming realtime metrics in keras',
    author='Jake Bian',
    author_email='jake@keplr.io',
    platforms=['any'],
    license='mit',
    packages=find_packages(),
    install_requires=[
        'requests',
        'socketIO-client',
        'keras'
    ],
)
