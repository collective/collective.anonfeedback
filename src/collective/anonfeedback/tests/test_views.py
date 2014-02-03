import unittest2 as unittest
from plone.testing.z2 import Browser

from Products.CMFCore.utils import getToolByName

from collective.anonfeedback.testing import\
    COLLECTIVE_ANONFEEDBACK_FUNCTIONAL_TESTING


class TestInstalled(unittest.TestCase):

    layer = COLLECTIVE_ANONFEEDBACK_FUNCTIONAL_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi_tool = getToolByName(self.portal, 'portal_quickinstaller')
    
    def test_views(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        browser = Browser(self.app)
        portalURL = self.portal.absolute_url()
        browser.open(portalURL)
        browser.getLink('Give Feedback').click()
        
        form = browser.getForm(name='feedback')
        form.getControl('Subject').value = 'Test subject'
        form.getControl('Feedback').value = 'Test\nmessage.'
        form.getControl('Submit').click()
        
        self.assertIn('Your feedback has been submitted.', browser.contents)
        
        browser.open(portalURL)
        self.assertNotIn('Give Feedback', browser.contents)
        