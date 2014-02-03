from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from plone.app.layout.viewlets.common import TitleViewlet 

class FeedbackForm(BrowserView):
    
    def handleform(self):
        form = self.request.form
        submit = form.get('submit', '')
        self.subject = form.get('subject', '').strip()
        self.feedback = form.get('feedback', '').strip()
        if submit:
            messages = IStatusMessage(self.request)
            if not self.subject or not self.feedback:
                messages.add(u'You must enter a subject and some feedback text.', type=u'error')
                return
            
            # Store feedback
            # Clear fields:
            self.subject = ''
            self.feedback = ''
            messages.add(u'Your feedback has been submitted.', type=u'info')
            