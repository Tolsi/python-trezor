# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class WavesMessageSignature(p.MessageType):
    FIELDS = {
        1: ('address', p.BytesType, 0),
        2: ('signature', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 119