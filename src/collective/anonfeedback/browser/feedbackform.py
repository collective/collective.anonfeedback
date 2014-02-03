from Products.Five import BrowserView

from plone.app.layout.viewlets.common import TitleViewlet 

class FeedbackForm(BrowserView):
    
    def handleform(self):
        form = self.request.form
        submit = form.get('submit')
        if submit:
            self.subject = form.get('subject')
            self.feedback = form.get('feedback')
        else:
            self.subject = ''
            self.feedback = ''
            self.message = ''
        
        
        