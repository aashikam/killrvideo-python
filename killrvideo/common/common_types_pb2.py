# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/common_types.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/common_types.proto',
  package='killrvideo.common',
  syntax='proto3',
  serialized_options=_b('\252\002\023KillrVideo.Protobuf'),
  serialized_pb=_b('\n\x19\x63ommon/common_types.proto\x12\x11killrvideo.common\"\x15\n\x04Uuid\x12\r\n\x05value\x18\x01 \x01(\t\"\x19\n\x08TimeUuid\x12\r\n\x05value\x18\x01 \x01(\tB\x16\xaa\x02\x13KillrVideo.Protobufb\x06proto3')
)




_UUID = _descriptor.Descriptor(
  name='Uuid',
  full_name='killrvideo.common.Uuid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='killrvideo.common.Uuid.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=69,
)


_TIMEUUID = _descriptor.Descriptor(
  name='TimeUuid',
  full_name='killrvideo.common.TimeUuid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='killrvideo.common.TimeUuid.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['Uuid'] = _UUID
DESCRIPTOR.message_types_by_name['TimeUuid'] = _TIMEUUID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Uuid = _reflection.GeneratedProtocolMessageType('Uuid', (_message.Message,), dict(
  DESCRIPTOR = _UUID,
  __module__ = 'common.common_types_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.common.Uuid)
  ))
_sym_db.RegisterMessage(Uuid)

TimeUuid = _reflection.GeneratedProtocolMessageType('TimeUuid', (_message.Message,), dict(
  DESCRIPTOR = _TIMEUUID,
  __module__ = 'common.common_types_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.common.TimeUuid)
  ))
_sym_db.RegisterMessage(TimeUuid)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
