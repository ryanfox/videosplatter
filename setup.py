from setuptools import setup

setup(
    name='videosplatter',
    version='0.1',
    description='Splat videos',
    url='http://github.com/ryanfox/videosplatter',
    author='Ryan Fox',
    author_email='ryan@foxrow.com',
    license='ACSL',
    packages=['videosplatter'],
    install_requires=[
        'imageio-ffmpeg==0.4.5',
    ],
    zip_safe=False
)
