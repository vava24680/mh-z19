import itertools

from mh_z19 import utils


VERSION = (0, 6, 1)

DEFAULT_SERIAL_FILE_PATH = utils.get_default_serial_device()

BAUD_RATE = 9600

NONE_BYTE = b'\x00'
RESERVED_BYTE = b'\x01'
START_BYTE = b'\xFF'

SELF_CALIBRATION_COMMAND_BYTE = b'\x79'
ENABLE_SELF_CALIBRATION_COMMAND_BYTE = b'\xA0'
DISABLE_SELF_CALIBRATION_COMMAND_BYTE = b'\x00'
ENABLE_SELF_CALIBRATION_COMMAND_CHECKSUM_BYTE = b'\xE6'
DISABLE_SELF_CALIBRATION_COMMAND_CHECKSUM_BYTE = b'\x86'

READ_COMMAND_BYTE = b'\x86'
READ_COMMAND_CHECKSUM_BYTE = b'\x79'

CALIBRATE_ZERO_POINT_COMMAND_BYTE = b'\x87'
CALIBRATE_ZERO_POINT_COMMAND_CHECKSUM_BYTE = b'\x78'

CALIBRATE_SPAN_POINT_COMMAND_BYTE = b'\x88'

SET_DETECTION_RANGE_COMMAND_BYTE = b'\x99'
SET_DETECTION_RANGE_2000_COMMAND_CHECKSUM_BYTE = b'\x8F'
SET_DETECTION_RANGE_5000_COMMAND_CHECKSUM_BYTE = b'\xCB'
SET_DETECTION_RANGE_10000_COMMAND_CHECKSUM_BYTE = b'\x2F'

READ_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        READ_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        READ_COMMAND_CHECKSUM_BYTE
    ))

ENABLE_SELF_CALIBRATION_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        SELF_CALIBRATION_COMMAND_BYTE,
        ENABLE_SELF_CALIBRATION_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        ENABLE_SELF_CALIBRATION_COMMAND_CHECKSUM_BYTE
    ))

DISABLE_SELF_CALIBRATION_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        SELF_CALIBRATION_COMMAND_BYTE,
        DISABLE_SELF_CALIBRATION_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        DISABLE_SELF_CALIBRATION_COMMAND_CHECKSUM_BYTE
    ))

SET_DETECTION_RANGE_2000_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        SET_DETECTION_RANGE_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        (2000 >> 8).to_bytes(1, 'big'),
        (2000 & 0xFF).to_bytes(1, 'big'),
        SET_DETECTION_RANGE_2000_COMMAND_CHECKSUM_BYTE
    ))

SET_DETECTION_RANGE_5000_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        SET_DETECTION_RANGE_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        (5000 >> 8).to_bytes(1, 'big'),
        (5000 & 0xFF).to_bytes(1, 'big'),
        SET_DETECTION_RANGE_5000_COMMAND_CHECKSUM_BYTE
    ))

SET_DETECTION_RANGE_10000_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        SET_DETECTION_RANGE_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        (10000 >> 8).to_bytes(1, 'big'),
        (10000 & 0xFF).to_bytes(1, 'big'),
        SET_DETECTION_RANGE_10000_COMMAND_CHECKSUM_BYTE
    ))

CALIBRATE_ZERO_POINT_COMMAND_BYTE_SEQUENCE = \
    bytes(itertools.chain(
        START_BYTE,
        RESERVED_BYTE,
        CALIBRATE_ZERO_POINT_COMMAND_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        NONE_BYTE,
        CALIBRATE_ZERO_POINT_COMMAND_CHECKSUM_BYTE
    ))
