#!/usr/bin/env python
from setuptools import setup

from lib import __version__

tests_require = [
    'pytest',
    'flake8'
]

setup(
    name='Sitescanner',
    #version=__version__,
    packages=[  'lib',
                'lib.utils',
                'lib.config',
                'lib.modules',
                'lib.modules.crawler',
                'lib.modules.attacks',
                'lib.modules.attacks.bruteforce',
                'lib.modules.attacks.injection',
                'lib.modules.attacks.vulns',
                'lib.modules.attacks.other',
                'lib.modules.fingerprints',
                'lib.modules.fingerprints.cdn',
                'lib.modules.fingerprints.cms',
                'lib.modules.fingerprints.framework',
                'lib.modules.fingerprints.frontend',
                'lib.modules.fingerprints.header',
                'lib.modules.fingerprints.lang',
                'lib.modules.fingerprints.server',
                'lib.modules.fingerprints.system',
                'lib.modules.fingerprints.waf',
                'lib.request'],
    scripts=['sitescanner.py'],
    include_package_data=True,
    author='Rapidsafeguard',
    author_email='rapidsafeguard@gmail.com',
    description='Sitescanner web scanner',
    version='1.0',
    python_requires=">=3.5",
    install_requires=[
        "requests",
        "urllib3",
        "pyyaml",
        "colorama",
        "scrapy"
    ],
    extras_require={
        'tests': tests_require,
    },
)
