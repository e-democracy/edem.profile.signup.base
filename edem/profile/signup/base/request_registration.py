# coding=utf-8
from Products.Five.browser.pagetemplatefile import \
    ZopeTwoPageTemplateFile
from gs.profile.signup.base.request_registration import \
    RequestRegistrationForm
import logging
log = logging.getLogger('EDemRequestRegistrationForm')

class EDemRequestRegistrationForm(RequestRegistrationForm):
    label = u'Sign Up'
    pageTemplateFileName = 'browser/templates/request_register.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

