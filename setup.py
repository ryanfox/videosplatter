from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='videosplatter',
    version='0.3',
    description='Splat videos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ryanfox/videosplatter',
    author='Ryan Fox',
    author_email='ryan@foxrow.com',
    license='ACSL',
    packages=['videosplatter'],
    install_requires=[
        'moviepy==1.0.3',
        'opencv-python==4.5.5.62',
    ],
    entry_points={
        'console_scripts': ['videosplatter=videosplatter.splat:main'],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
