# coding=utf-8
from __future__ import absolute_import, unicode_literals
from urllib import urlencode
from urlparse import urlparse
from zope.formlib import form
from Products.CustomUserFolder.interfaces import IGSUserInfo
from Products.Five.browser.pagetemplatefile import \
    ZopeTwoPageTemplateFile
from Products.GSProfile.profileaudit import ProfileAuditer
from gs.profile.signup.base.changeprofile import ChangeProfileForm  \
    as RegisterEditProfileForm
from .utils import fn_to_nickname

import logging
log = logging.getLogger('EDemEditProfileForm')


class EDemRegisterEditProfileForm(RegisterEditProfileForm):
    label = 'Change Profile'
    pageTemplateFileName = 'browser/templates/changeprofile.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    @form.action(label='Submit', failure='handle_set_action_failure')
    def handle_set(self, action, data):
        self.auditer = ProfileAuditer(self.context)
        self.actual_handle_set(action, data)

        # Actual E-Dem Custom code. We like to set the nickname during reg
        if self.userInfo.nickname == self.userInfo.id:
            m = 'Adding nickname to %s (%s)' % (self.userInfo.name, 
                self.userInfo.id)
            log.info(m)
            nickname = fn_to_nickname(self.context, self.userInfo.name)
            self.context.add_nickname(nickname)
        else:
            nickname = userInfo.nickname  # --=mpj17=-- See below
        
        # / Actual E-Dem Custom code.

        cf = str(data.pop('came_from'))
        cf = cf if cf != 'None' else ''
        if self.user_has_verified_email:
            parsedCameFrom = urlparse(cf)
            p = parsedCameFrom.path if cf else '/'
            uri = '{0}?welcome=1'.format(p)
        else:
            email = self.emailUser.get_addresses()[0]
            u = '{0}/verify_wait.html?{1}'
            d = {'form.email': email,
                 'form.came_from': cf}
            queryString = urlencode(d)
            uri = u.format('/p/%s' % nickname, queryString)

        assert uri
        return self.request.RESPONSE.redirect(uri)

    def filteredOptionalProfileWidgets(self, omit):
        widgets = self.optionalProfileWidgets
        filtered_widgets = []
        for widget in widgets:
            print widget.name, omit
            if widget.name not in omit:
                filtered_widgets.append(widget)

        return filtered_widgets
