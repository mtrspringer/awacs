# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Elastic Block Store'
prefix = 'ebs'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


CompleteSnapshot = Action('CompleteSnapshot')
GetSnapshotBlock = Action('GetSnapshotBlock')
ListChangedBlocks = Action('ListChangedBlocks')
ListSnapshotBlocks = Action('ListSnapshotBlocks')
PutSnapshotBlock = Action('PutSnapshotBlock')
StartSnapshot = Action('StartSnapshot')
