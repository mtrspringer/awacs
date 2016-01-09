# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon CloudWatch Logs'
prefix = 'logs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateLogGroup = Action('CreateLogGroup')
CreateLogStream = Action('CreateLogStream')
DeleteLogGroup = Action('DeleteLogGroup')
DeleteLogStream = Action('DeleteLogStream')
DeleteMetricFilter = Action('DeleteMetricFilter')
DeleteRetentionPolicy = Action('DeleteRetentionPolicy')
DescribeLogGroups = Action('DescribeLogGroups')
DescribeLogStreams = Action('DescribeLogStreams')
DescribeMetricFilters = Action('DescribeMetricFilters')
FilterLogEvents = Action('FilterLogEvents')
GetLogEvents = Action('GetLogEvents')
PutLogEvents = Action('PutLogEvents')
PutMetricFilter = Action('PutMetricFilter')
PutRetentionPolicy = Action('PutRetentionPolicy')
TestMetricFilter = Action('TestMetricFilter')
