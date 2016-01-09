# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon SES'
prefix = 'ses'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DeleteIdentity = Action('DeleteIdentity')
DeleteVerifiedEmailAddress = Action('DeleteVerifiedEmailAddress')
GetIdentityDkimAttributes = Action('GetIdentityDkimAttributes')
GetIdentityNotificationAttributes = \
    Action('GetIdentityNotificationAttributes')
GetIdentityVerificationAttributes = \
    Action('GetIdentityVerificationAttributes')
GetSendQuota = Action('GetSendQuota')
GetSendStatistics = Action('GetSendStatistics')
ListIdentities = Action('ListIdentities')
ListVerifiedEmailAddresses = Action('ListVerifiedEmailAddresses')
SendEmail = Action('SendEmail')
SendRawEmail = Action('SendRawEmail')
SetIdentityDkimEnabled = Action('SetIdentityDkimEnabled')
SetIdentityNotificationTopic = Action('SetIdentityNotificationTopic')
SetIdentityFeedbackForwardingEnabled = \
    Action('SetIdentityFeedbackForwardingEnabled')
VerifyDomainDkim = Action('VerifyDomainDkim')
VerifyDomainIdentity = Action('VerifyDomainIdentity')
VerifyEmailAddress = Action('VerifyEmailAddress')
VerifyEmailIdentity = Action('VerifyEmailIdentity')
