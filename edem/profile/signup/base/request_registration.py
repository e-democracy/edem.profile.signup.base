# coding=utf-8
from __future__ import absolute_import, unicode_literals
from Products.Five.browser.pagetemplatefile import \
    ZopeTwoPageTemplateFile
from gs.profile.signup.base.request_registration import \
    RequestRegistrationForm

import logging
log = logging.getLogger('EDemRequestRegistrationForm')


class EDemRequestRegistrationForm(RequestRegistrationForm):
    label = 'Sign Up'
    pageTemplateFileName = 'browser/templates/signup.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
