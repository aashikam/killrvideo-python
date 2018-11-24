# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user-management/user_management_events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from common import common_types_pb2 as common_dot_common__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='user-management/user_management_events.proto',
  package='killrvideo.user_management.events',
  syntax='proto3',
  serialized_options=_b('\252\002 KillrVideo.UserManagement.Events'),
  serialized_pb=_b('\n,user-management/user_management_events.proto\x12!killrvideo.user_management.events\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63ommon/common_types.proto\"\x9c\x01\n\x0bUserCreated\x12(\n\x07user_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB#\xaa\x02 KillrVideo.UserManagement.Eventsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common_dot_common__types__pb2.DESCRIPTOR,])




_USERCREATED = _descriptor.Descriptor(
  name='UserCreated',
  full_name='killrvideo.user_management.events.UserCreated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.user_management.events.UserCreated.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='killrvideo.user_management.events.UserCreated.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='killrvideo.user_management.events.UserCreated.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='killrvideo.user_management.events.UserCreated.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='killrvideo.user_management.events.UserCreated.timestamp', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=144,
  serialized_end=300,
)

_USERCREATED.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_USERCREATED.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['UserCreated'] = _USERCREATED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserCreated = _reflection.GeneratedProtocolMessageType('UserCreated', (_message.Message,), dict(
  DESCRIPTOR = _USERCREATED,
  __module__ = 'user_management.user_management_events_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.user_management.events.UserCreated)
  ))
_sym_db.RegisterMessage(UserCreated)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
