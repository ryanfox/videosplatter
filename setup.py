from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='videosplatter',
    version='0.2',
    description='Splat videos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/ryanfox/videosplatter',
    author='Ryan Fox',
    author_email='ryan@foxrow.com',
    license='ACSL',
    packages=['videosplatter'],
    install_requires=[
        'imageio-ffmpeg==0.4.5',
        'cx-freeze==6.10',
        'gooey==1.0.8.1',
    ],
    entry_points= {
        'console_scripts': ['videosplatter=videosplatter.splat:main'],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
