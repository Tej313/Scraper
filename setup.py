from setuptools import setup, find_packages

setup(
    name='Scraper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'scraper=Scraper.beautiful_soup:main',
        ],
    },
)
