from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_steever2019dravidian',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_steever2019dravidian'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'steever2019dravidian=cldfbench_steever2019dravidian:Dataset',
        ]
    },
    install_requires=[
        'pyglottography',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
