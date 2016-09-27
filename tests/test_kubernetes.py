# Copyright (C) 2016  Custodia Project Contributors - see LICENSE file

import unittest

import pkg_resources

from custodia.plugin import HTTPAuthenticator, HTTPAuthorizer


class TestKubernetesPlugins(unittest.TestCase):
    def test_nodeauth(self):
        eps = list(pkg_resources.iter_entry_points(
            'custodia.authenticators', 'K8sNodeAuth'))
        self.assertEqual(len(eps), 1)
        cls = eps[0].resolve()
        self.assertEqual(issubclass(cls, HTTPAuthenticator))

    def test_authz(self):
        eps = list(pkg_resources.iter_entry_points(
            'custodia.authenticators', 'K8sAuthz'))
        self.assertEqual(len(eps), 1)
        cls = eps[0].resolve()
        self.assertEqual(issubclass(cls, HTTPAuthorizer))
