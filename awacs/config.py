# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'AWS Config'
prefix = 'config'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


DeleteDeliveryChannel = Action('DeleteDeliveryChannel')
DeliverConfigSnapshot = Action('DeliverConfigSnapshot')
DescribeConfigurationRecorderStatus = \
    Action('DescribeConfigurationRecorderStatus')
DescribeConfigurationRecorders = Action('DescribeConfigurationRecorders')
DescribeDeliveryChannelStatus = Action('DescribeDeliveryChannelStatus')
DescribeDeliveryChannels = Action('DescribeDeliveryChannels')
GetResourceConfigHistory = Action('GetResourceConfigHistory')
GetResources = Action('GetResources')
GetTagKeys = Action('GetTagKeys')
PutConfigurationRecorder = Action('PutConfigurationRecorder')
PutDeliveryChannel = Action('PutDeliveryChannel')
StartConfigurationRecorder = Action('StartConfigurationRecorder')
StopConfigurationRecorder = Action('StopConfigurationRecorder')
