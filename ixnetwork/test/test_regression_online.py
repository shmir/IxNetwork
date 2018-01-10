"""
IxNetwork package regression tests (all in offline mode).

@author yoram@ignissoft.com
"""

from trafficgenerator.tgn_utils import ApiType

from ixnetwork.test.test_online import IxnTestOnline


class IxnTestRegressionTcl(IxnTestOnline):

    def setUp(self):
        tcl = ApiType.tcl
        self.config.set('IXN', 'api', tcl.name)
        self.config.set('IXN', 'api_port', str(8009))
        super(self.__class__, self).setUp()


class IxnTestRegressionRest(IxnTestOnline):

    def setUp(self):
        rest = ApiType.rest
        self.config.set('IXN', 'api', rest.name)
        self.config.set('IXN', 'api_port', str(11009))
        super(self.__class__, self).setUp()