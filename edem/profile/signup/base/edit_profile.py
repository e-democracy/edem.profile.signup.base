# coding=utf-8
from __future__ import absolute_import, unicode_literals
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
        user = self.context
        self.auditer = ProfileAuditer(user)
        self.actual_handle_set(action, data)

        userInfo = IGSUserInfo(self.ctx)
        if userInfo.nickname == userInfo.id:
            m = 'Adding nickname to %s (%s)' % (userInfo.name, userInfo.id)
            log.info(m)
            nickname = fn_to_nickname(user, userInfo.name)
            user.add_nickname(nickname)
        else:
            nickname = userInfo.nickname  # --=mpj17=-- See below

        cf = str(data.pop('came_from'))
        if cf == 'None':
            cf = ''
        if self.user_has_verified_email:
            uri = str(data.get('came_from'))
            if uri == 'None':
                uri = '/'
            uri = '%s?welcome=1' % uri
        else:
            # --=mpj17=-- I construct the URI manually because there
            # is a race condition between setting the nickname in the
            # relational database, and getting it out to form the URI.
            email = self.context.get_emailAddresses()[0]
            uri = '/p/%s/verify_wait.html?form.email=%s&form.came_from=%s' %\
                (nickname, email, cf)
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
