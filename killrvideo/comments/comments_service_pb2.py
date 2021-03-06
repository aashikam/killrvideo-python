# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comments/comments_service.proto

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
  name='comments/comments_service.proto',
  package='killrvideo.comments',
  syntax='proto3',
  serialized_options=_b('\252\002\023KillrVideo.Comments'),
  serialized_pb=_b('\n\x1f\x63omments/comments_service.proto\x12\x13killrvideo.comments\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19\x63ommon/common_types.proto\"\xae\x01\n\x15\x43ommentOnVideoRequest\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12(\n\x07user_id\x18\x02 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12/\n\ncomment_id\x18\x03 \x01(\x0b\x32\x1b.killrvideo.common.TimeUuid\x12\x0f\n\x07\x63omment\x18\x04 \x01(\t\"\x18\n\x16\x43ommentOnVideoResponse\"\xa5\x01\n\x16GetUserCommentsRequest\x12(\n\x07user_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x38\n\x13starting_comment_id\x18\x03 \x01(\x0b\x32\x1b.killrvideo.common.TimeUuid\x12\x14\n\x0cpaging_state\x18\x10 \x01(\t\"\x8d\x01\n\x17GetUserCommentsResponse\x12(\n\x07user_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x32\n\x08\x63omments\x18\x02 \x03(\x0b\x32 .killrvideo.comments.UserComment\x12\x14\n\x0cpaging_state\x18\x03 \x01(\t\"\xb1\x01\n\x0bUserComment\x12/\n\ncomment_id\x18\x01 \x01(\x0b\x32\x1b.killrvideo.common.TimeUuid\x12)\n\x08video_id\x18\x02 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x35\n\x11\x63omment_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa7\x01\n\x17GetVideoCommentsRequest\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x38\n\x13starting_comment_id\x18\x03 \x01(\x0b\x32\x1b.killrvideo.common.TimeUuid\x12\x14\n\x0cpaging_state\x18\x10 \x01(\t\"\x90\x01\n\x18GetVideoCommentsResponse\x12)\n\x08video_id\x18\x01 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x33\n\x08\x63omments\x18\x02 \x03(\x0b\x32!.killrvideo.comments.VideoComment\x12\x14\n\x0cpaging_state\x18\x03 \x01(\t\"\xb1\x01\n\x0cVideoComment\x12/\n\ncomment_id\x18\x01 \x01(\x0b\x32\x1b.killrvideo.common.TimeUuid\x12(\n\x07user_id\x18\x02 \x01(\x0b\x32\x17.killrvideo.common.Uuid\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\x12\x35\n\x11\x63omment_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xdb\x02\n\x0f\x43ommentsService\x12i\n\x0e\x43ommentOnVideo\x12*.killrvideo.comments.CommentOnVideoRequest\x1a+.killrvideo.comments.CommentOnVideoResponse\x12l\n\x0fGetUserComments\x12+.killrvideo.comments.GetUserCommentsRequest\x1a,.killrvideo.comments.GetUserCommentsResponse\x12o\n\x10GetVideoComments\x12,.killrvideo.comments.GetVideoCommentsRequest\x1a-.killrvideo.comments.GetVideoCommentsResponseB\x16\xaa\x02\x13KillrVideo.Commentsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,common_dot_common__types__pb2.DESCRIPTOR,])




_COMMENTONVIDEOREQUEST = _descriptor.Descriptor(
  name='CommentOnVideoRequest',
  full_name='killrvideo.comments.CommentOnVideoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.comments.CommentOnVideoRequest.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.comments.CommentOnVideoRequest.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_id', full_name='killrvideo.comments.CommentOnVideoRequest.comment_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='killrvideo.comments.CommentOnVideoRequest.comment', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=117,
  serialized_end=291,
)


_COMMENTONVIDEORESPONSE = _descriptor.Descriptor(
  name='CommentOnVideoResponse',
  full_name='killrvideo.comments.CommentOnVideoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=293,
  serialized_end=317,
)


_GETUSERCOMMENTSREQUEST = _descriptor.Descriptor(
  name='GetUserCommentsRequest',
  full_name='killrvideo.comments.GetUserCommentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.comments.GetUserCommentsRequest.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='killrvideo.comments.GetUserCommentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_comment_id', full_name='killrvideo.comments.GetUserCommentsRequest.starting_comment_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.comments.GetUserCommentsRequest.paging_state', index=3,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=320,
  serialized_end=485,
)


_GETUSERCOMMENTSRESPONSE = _descriptor.Descriptor(
  name='GetUserCommentsResponse',
  full_name='killrvideo.comments.GetUserCommentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.comments.GetUserCommentsResponse.user_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='killrvideo.comments.GetUserCommentsResponse.comments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.comments.GetUserCommentsResponse.paging_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=488,
  serialized_end=629,
)


_USERCOMMENT = _descriptor.Descriptor(
  name='UserComment',
  full_name='killrvideo.comments.UserComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment_id', full_name='killrvideo.comments.UserComment.comment_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.comments.UserComment.video_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='killrvideo.comments.UserComment.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_timestamp', full_name='killrvideo.comments.UserComment.comment_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=632,
  serialized_end=809,
)


_GETVIDEOCOMMENTSREQUEST = _descriptor.Descriptor(
  name='GetVideoCommentsRequest',
  full_name='killrvideo.comments.GetVideoCommentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.comments.GetVideoCommentsRequest.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='killrvideo.comments.GetVideoCommentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_comment_id', full_name='killrvideo.comments.GetVideoCommentsRequest.starting_comment_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.comments.GetVideoCommentsRequest.paging_state', index=3,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=812,
  serialized_end=979,
)


_GETVIDEOCOMMENTSRESPONSE = _descriptor.Descriptor(
  name='GetVideoCommentsResponse',
  full_name='killrvideo.comments.GetVideoCommentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_id', full_name='killrvideo.comments.GetVideoCommentsResponse.video_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='killrvideo.comments.GetVideoCommentsResponse.comments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paging_state', full_name='killrvideo.comments.GetVideoCommentsResponse.paging_state', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=982,
  serialized_end=1126,
)


_VIDEOCOMMENT = _descriptor.Descriptor(
  name='VideoComment',
  full_name='killrvideo.comments.VideoComment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='comment_id', full_name='killrvideo.comments.VideoComment.comment_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='killrvideo.comments.VideoComment.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment', full_name='killrvideo.comments.VideoComment.comment', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comment_timestamp', full_name='killrvideo.comments.VideoComment.comment_timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1129,
  serialized_end=1306,
)

_COMMENTONVIDEOREQUEST.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_COMMENTONVIDEOREQUEST.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_COMMENTONVIDEOREQUEST.fields_by_name['comment_id'].message_type = common_dot_common__types__pb2._TIMEUUID
_GETUSERCOMMENTSREQUEST.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_GETUSERCOMMENTSREQUEST.fields_by_name['starting_comment_id'].message_type = common_dot_common__types__pb2._TIMEUUID
_GETUSERCOMMENTSRESPONSE.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_GETUSERCOMMENTSRESPONSE.fields_by_name['comments'].message_type = _USERCOMMENT
_USERCOMMENT.fields_by_name['comment_id'].message_type = common_dot_common__types__pb2._TIMEUUID
_USERCOMMENT.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_USERCOMMENT.fields_by_name['comment_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETVIDEOCOMMENTSREQUEST.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_GETVIDEOCOMMENTSREQUEST.fields_by_name['starting_comment_id'].message_type = common_dot_common__types__pb2._TIMEUUID
_GETVIDEOCOMMENTSRESPONSE.fields_by_name['video_id'].message_type = common_dot_common__types__pb2._UUID
_GETVIDEOCOMMENTSRESPONSE.fields_by_name['comments'].message_type = _VIDEOCOMMENT
_VIDEOCOMMENT.fields_by_name['comment_id'].message_type = common_dot_common__types__pb2._TIMEUUID
_VIDEOCOMMENT.fields_by_name['user_id'].message_type = common_dot_common__types__pb2._UUID
_VIDEOCOMMENT.fields_by_name['comment_timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['CommentOnVideoRequest'] = _COMMENTONVIDEOREQUEST
DESCRIPTOR.message_types_by_name['CommentOnVideoResponse'] = _COMMENTONVIDEORESPONSE
DESCRIPTOR.message_types_by_name['GetUserCommentsRequest'] = _GETUSERCOMMENTSREQUEST
DESCRIPTOR.message_types_by_name['GetUserCommentsResponse'] = _GETUSERCOMMENTSRESPONSE
DESCRIPTOR.message_types_by_name['UserComment'] = _USERCOMMENT
DESCRIPTOR.message_types_by_name['GetVideoCommentsRequest'] = _GETVIDEOCOMMENTSREQUEST
DESCRIPTOR.message_types_by_name['GetVideoCommentsResponse'] = _GETVIDEOCOMMENTSRESPONSE
DESCRIPTOR.message_types_by_name['VideoComment'] = _VIDEOCOMMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommentOnVideoRequest = _reflection.GeneratedProtocolMessageType('CommentOnVideoRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMMENTONVIDEOREQUEST,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.CommentOnVideoRequest)
  ))
_sym_db.RegisterMessage(CommentOnVideoRequest)

CommentOnVideoResponse = _reflection.GeneratedProtocolMessageType('CommentOnVideoResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMENTONVIDEORESPONSE,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.CommentOnVideoResponse)
  ))
_sym_db.RegisterMessage(CommentOnVideoResponse)

GetUserCommentsRequest = _reflection.GeneratedProtocolMessageType('GetUserCommentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERCOMMENTSREQUEST,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.GetUserCommentsRequest)
  ))
_sym_db.RegisterMessage(GetUserCommentsRequest)

GetUserCommentsResponse = _reflection.GeneratedProtocolMessageType('GetUserCommentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERCOMMENTSRESPONSE,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.GetUserCommentsResponse)
  ))
_sym_db.RegisterMessage(GetUserCommentsResponse)

UserComment = _reflection.GeneratedProtocolMessageType('UserComment', (_message.Message,), dict(
  DESCRIPTOR = _USERCOMMENT,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.UserComment)
  ))
_sym_db.RegisterMessage(UserComment)

GetVideoCommentsRequest = _reflection.GeneratedProtocolMessageType('GetVideoCommentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVIDEOCOMMENTSREQUEST,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.GetVideoCommentsRequest)
  ))
_sym_db.RegisterMessage(GetVideoCommentsRequest)

GetVideoCommentsResponse = _reflection.GeneratedProtocolMessageType('GetVideoCommentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETVIDEOCOMMENTSRESPONSE,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.GetVideoCommentsResponse)
  ))
_sym_db.RegisterMessage(GetVideoCommentsResponse)

VideoComment = _reflection.GeneratedProtocolMessageType('VideoComment', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOCOMMENT,
  __module__ = 'comments.comments_service_pb2'
  # @@protoc_insertion_point(class_scope:killrvideo.comments.VideoComment)
  ))
_sym_db.RegisterMessage(VideoComment)


DESCRIPTOR._options = None

_COMMENTSSERVICE = _descriptor.ServiceDescriptor(
  name='CommentsService',
  full_name='killrvideo.comments.CommentsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1309,
  serialized_end=1656,
  methods=[
  _descriptor.MethodDescriptor(
    name='CommentOnVideo',
    full_name='killrvideo.comments.CommentsService.CommentOnVideo',
    index=0,
    containing_service=None,
    input_type=_COMMENTONVIDEOREQUEST,
    output_type=_COMMENTONVIDEORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserComments',
    full_name='killrvideo.comments.CommentsService.GetUserComments',
    index=1,
    containing_service=None,
    input_type=_GETUSERCOMMENTSREQUEST,
    output_type=_GETUSERCOMMENTSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetVideoComments',
    full_name='killrvideo.comments.CommentsService.GetVideoComments',
    index=2,
    containing_service=None,
    input_type=_GETVIDEOCOMMENTSREQUEST,
    output_type=_GETVIDEOCOMMENTSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMENTSSERVICE)

DESCRIPTOR.services_by_name['CommentsService'] = _COMMENTSSERVICE

# @@protoc_insertion_point(module_scope)
