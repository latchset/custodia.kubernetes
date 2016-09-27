#!/usr/bin/python
#
# Copyright (C) 2015  Custodia project Contributors, for licensee see COPYING

from setuptools import setup

requirements = [
    'custodia >= 0.2.dev1',
    'docker-py',
]

# test requirements
test_requires = ['coverage', 'pytest']
test_pylint_requires = ['pylint'] + test_requires
test_pep8_requires = ['flake8', 'flake8-import-order', 'pep8-naming']
test_docs_requires = ['docutils', 'markdown']

with open('README') as f:
    long_description = f.read()


# Plugins
custodia_authenticators = [
    'K8sNodeAuth = custodia.kubernetes.node:NodeAuth',
]

custodia_authorizers = [
    'K8sAuthz = custodia.kubernetes.authz:KubeAuthz',
]


setup(
    name='custodia.kubernetes',
    description='Kubernetes and Docker plugins for Custodia',
    long_description=long_description,
    version='0.2.dev1',
    license='GPLv3+',
    maintainer='Custodia project Contributors',
    maintainer_email='cheimes@redhat.com',
    url='https://github.com/latchset/custodia.kubernetes',
    namespace_packages=['custodia'],
    packages=[
        'custodia.kubernetes',
    ],
    entry_points={
        'custodia.authenticators': custodia_authenticators,
        'custodia.authorizers': custodia_authorizers,
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=requirements,
    tests_require=test_requires,
    extras_require={
        'test': test_requires,
        'test_docs': test_docs_requires,
        'test_pep8': test_pep8_requires,
        'test_pylint': test_pylint_requires,
    },
)
