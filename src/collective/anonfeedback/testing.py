from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveAnonfeedback(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.anonfeedback
        xmlconfig.file('configure.zcml',
                       collective.anonfeedback,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.anonfeedback:default')

COLLECTIVE_ANONFEEDBACK_FIXTURE = CollectiveAnonfeedback()
COLLECTIVE_ANONFEEDBACK_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_ANONFEEDBACK_FIXTURE, ),
                       name="CollectiveAnonfeedback:Integration")

COLLECTIVE_ANONFEEDBACK_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(COLLECTIVE_ANONFEEDBACK_FIXTURE,),
                      name="CollectiveAnonfeedback:Functional"
                      )
