# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video-catalog/video_catalog_events.proto

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
  name='video-catalog/video_catalog_events.proto',
  package='killrvideo.video_catalog.events',
  syntax='proto3',
  serialized_options=_b('\252\002\036KillrVideo.VideoCatalog.Events'),
  serialized_pb=_b('\n(video-catalog/video_catalog_events.proto\x12\x1fkillrvideo.video_catalog.events\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63ommon/common_types.proto\"\x85\x01\n\x15UploadedVideoAccepted\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x12\n\nupload_url\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xab\x02\n\x12UploadedVideoAdded\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12(\n\x07user_id\x18\x02 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x1e\n\x16preview_image_location\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12.\n\nadded_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaa\x02\n\x11YouTubeVideoAdded\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12(\n\x07user_id\x18\x02 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x1e\n\x16preview_image_location\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\x12.\n\nadded_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\ttimestamp\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB!\xaa\x02\x1eKillrVideo.VideoCatalog.Eventsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common_dot_common__types__pb2.DESCRIPTOR,])




_UPLOADEDVIDEOACCEPTED = _descriptor.Descriptor(
  name='UploadedVideoAccepted',
  full_name='killrvideo.video_catalog.events.UploadedVideoAccepted',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.video_catalog.events.UploadedVideoAccepted.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_url', full_name='killrvideo.video_catalog.events.UploadedVideoAccepted.upload_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='killrvideo.video_catalog.events.UploadedVideoAccepted.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=138,
  serialized_end=271,
)


_UPLOADEDVIDEOADDED = _descriptor.Descriptor(
  name='UploadedVideoAdded',
  full_name='killrvideo.video_catalog.events.UploadedVideoAdded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_image_location', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.preview_image_location', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_date', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.added_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='killrvideo.video_catalog.events.UploadedVideoAdded.timestamp', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=274,
  serialized_end=573,
)


_YOUTUBEVIDEOADDED = _descriptor.Descriptor(
  name='YouTubeVideoAdded',
  full_name='killrvideo.video_catalog.events.YouTubeVideoAdded',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.location', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview_image_location', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.preview_image_location', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.tags', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_date', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.added_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='killrvideo.video_catalog.events.YouTubeVideoAdded.timestamp', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=576,
  serialized_end=874,
)

_UPLOADEDVIDEOACCEPTED.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_UPLOADEDVIDEOACCEPTED.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPLOADEDVIDEOADDED.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_UPLOADEDVIDEOADDED.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_UPLOADEDVIDEOADDED.fields_by_name['added_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPLOADEDVIDEOADDED.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_YOUTUBEVIDEOADDED.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_YOUTUBEVIDEOADDED.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_YOUTUBEVIDEOADDED.fields_by_name['added_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_YOUTUBEVIDEOADDED.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['UploadedVideoAccepted'] = _UPLOADEDVIDEOACCEPTED
DESCRIPTOR.message_types_by_name['UploadedVideoAdded'] = _UPLOADEDVIDEOADDED
DESCRIPTOR.message_types_by_name['YouTubeVideoAdded'] = _YOUTUBEVIDEOADDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UploadedVideoAccepted = _reflection.GeneratedProtocolMessageType('UploadedVideoAccepted', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADEDVIDEOACCEPTED,
  __module__ = 'video_catalog.video_catalog_events_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.video_catalog.events.UploadedVideoAccepted)
  ))
_sym_db.RegisterMessage(UploadedVideoAccepted)

UploadedVideoAdded = _reflection.GeneratedProtocolMessageType('UploadedVideoAdded', (_message.Message,), dict(
  DESCRIPTOR = _UPLOADEDVIDEOADDED,
  __module__ = 'video_catalog.video_catalog_events_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.video_catalog.events.UploadedVideoAdded)
  ))
_sym_db.RegisterMessage(UploadedVideoAdded)

YouTubeVideoAdded = _reflection.GeneratedProtocolMessageType('YouTubeVideoAdded', (_message.Message,), dict(
  DESCRIPTOR = _YOUTUBEVIDEOADDED,
  __module__ = 'video_catalog.video_catalog_events_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.video_catalog.events.YouTubeVideoAdded)
  ))
_sym_db.RegisterMessage(YouTubeVideoAdded)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
