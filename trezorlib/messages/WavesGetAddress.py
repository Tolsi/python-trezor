# Automatically generated by pb2py
from __future__ import absolute_import
from .. import protobuf as p


class WavesGetAddress(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('show_display', p.BoolType, 0),
    }
    MESSAGE_WIRE_TYPE = 120
