# bitcoder
A python package for describing packed bits and exporting that information to other languages.

Given a simple description of a packed field such as

    class Example16Bytes(Encoded):
        bits = 16
        gps_enabled = Bool(start=2)
        latitude = Field(start=3, len=4)
        sbas_enabled = Bool(start=10)

Produces formatted descriptions such as:

    0:	Reserved
    1:	Reserved
    2:	gps_enabled
    3:	latitude
    4:	latitude
    5:	latitude
    6:	latitude
    7:	Reserved
    8:	Reserved
    9:	Reserved
    10:	sbas_enabled
    11:	Reserved
    12:	Reserved
    13:	Reserved
    14:	Reserved
    15:	Reserved
