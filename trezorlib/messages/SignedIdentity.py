# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class SignedIdentity(p.MessageType):
    FIELDS = {
        1: ('address', p.UnicodeType, 0),
        2: ('public_key', p.BytesType, 0),
        3: ('signature', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 54
