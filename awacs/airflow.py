# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Managed Workflows for Apache Airflow'
prefix = 'airflow'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CreateCliToken = Action('CreateCliToken')
CreateEnvironment = Action('CreateEnvironment')
CreateWebLoginToken = Action('CreateWebLoginToken')
DeleteEnvironment = Action('DeleteEnvironment')
GetEnvironment = Action('GetEnvironment')
ListEnvironments = Action('ListEnvironments')
ListTagsForResource = Action('ListTagsForResource')
PublishMetrics = Action('PublishMetrics')
TagResource = Action('TagResource')
UntagResource = Action('UntagResource')
UpdateEnvironment = Action('UpdateEnvironment')
