# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bot_action.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bot_base_pb2 as bot__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bot_action.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\021net.lz1998.botidl',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x62ot_action.proto\x1a\x0e\x62ot_base.proto\"\xdd\x01\n\x06\x41\x63tion\x12\r\n\x05\x62otId\x18\x01 \x01(\x03\x12\x1f\n\nactionType\x18\x02 \x01(\x0e\x32\x0b.ActionType\x12\x37\n\x15sendPrivateMessageReq\x18\x65 \x01(\x0b\x32\x16.SendPrivateMessageReqH\x00\x12\x33\n\x13sendGroupMessageReq\x18\x66 \x01(\x0b\x32\x14.SendGroupMessageReqH\x00\x12+\n\x0fgetGroupInfoReq\x18g \x01(\x0b\x32\x10.GetGroupInfoReqH\x00\x42\x08\n\x06\x61\x63tion\"G\n\x15SendPrivateMessageReq\x12\x0e\n\x06userId\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t\"\'\n\x16SendPrivateMessageResp\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t\"F\n\x13SendGroupMessageReq\x12\x0f\n\x07groupId\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t\"%\n\x14SendGroupMessageResp\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t\"1\n\x0fGetGroupInfoReq\x12\x0f\n\x07groupId\x18\x01 \x01(\x03\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t\"8\n\x10GetGroupInfoResp\x12\x15\n\x05group\x18\x01 \x01(\x0b\x32\x06.Group\x12\r\n\x04\x65\x63ho\x18\xff\x01 \x01(\t*R\n\nActionType\x12\x18\n\x14SEND_PRIVATE_MESSAGE\x10\x00\x12\x16\n\x12SEND_GROUP_MESSAGE\x10\x01\x12\x12\n\x0eGET_GROUP_INFO\x10\x02\x42\x13\n\x11net.lz1998.botidlb\x06proto3'
  ,
  dependencies=[bot__base__pb2.DESCRIPTOR,])

_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='ActionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEND_PRIVATE_MESSAGE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SEND_GROUP_MESSAGE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET_GROUP_INFO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=594,
  serialized_end=676,
)
_sym_db.RegisterEnumDescriptor(_ACTIONTYPE)

ActionType = enum_type_wrapper.EnumTypeWrapper(_ACTIONTYPE)
SEND_PRIVATE_MESSAGE = 0
SEND_GROUP_MESSAGE = 1
GET_GROUP_INFO = 2



_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='botId', full_name='Action.botId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actionType', full_name='Action.actionType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendPrivateMessageReq', full_name='Action.sendPrivateMessageReq', index=2,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sendGroupMessageReq', full_name='Action.sendGroupMessageReq', index=3,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='getGroupInfoReq', full_name='Action.getGroupInfoReq', index=4,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='action', full_name='Action.action',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=37,
  serialized_end=258,
)


_SENDPRIVATEMESSAGEREQ = _descriptor.Descriptor(
  name='SendPrivateMessageReq',
  full_name='SendPrivateMessageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='SendPrivateMessageReq.userId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='SendPrivateMessageReq.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='echo', full_name='SendPrivateMessageReq.echo', index=2,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=260,
  serialized_end=331,
)


_SENDPRIVATEMESSAGERESP = _descriptor.Descriptor(
  name='SendPrivateMessageResp',
  full_name='SendPrivateMessageResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='echo', full_name='SendPrivateMessageResp.echo', index=0,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=333,
  serialized_end=372,
)


_SENDGROUPMESSAGEREQ = _descriptor.Descriptor(
  name='SendGroupMessageReq',
  full_name='SendGroupMessageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='SendGroupMessageReq.groupId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='SendGroupMessageReq.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='echo', full_name='SendGroupMessageReq.echo', index=2,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=374,
  serialized_end=444,
)


_SENDGROUPMESSAGERESP = _descriptor.Descriptor(
  name='SendGroupMessageResp',
  full_name='SendGroupMessageResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='echo', full_name='SendGroupMessageResp.echo', index=0,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=446,
  serialized_end=483,
)


_GETGROUPINFOREQ = _descriptor.Descriptor(
  name='GetGroupInfoReq',
  full_name='GetGroupInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='groupId', full_name='GetGroupInfoReq.groupId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='echo', full_name='GetGroupInfoReq.echo', index=1,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=485,
  serialized_end=534,
)


_GETGROUPINFORESP = _descriptor.Descriptor(
  name='GetGroupInfoResp',
  full_name='GetGroupInfoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group', full_name='GetGroupInfoResp.group', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='echo', full_name='GetGroupInfoResp.echo', index=1,
      number=255, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=536,
  serialized_end=592,
)

_ACTION.fields_by_name['actionType'].enum_type = _ACTIONTYPE
_ACTION.fields_by_name['sendPrivateMessageReq'].message_type = _SENDPRIVATEMESSAGEREQ
_ACTION.fields_by_name['sendGroupMessageReq'].message_type = _SENDGROUPMESSAGEREQ
_ACTION.fields_by_name['getGroupInfoReq'].message_type = _GETGROUPINFOREQ
_ACTION.oneofs_by_name['action'].fields.append(
  _ACTION.fields_by_name['sendPrivateMessageReq'])
_ACTION.fields_by_name['sendPrivateMessageReq'].containing_oneof = _ACTION.oneofs_by_name['action']
_ACTION.oneofs_by_name['action'].fields.append(
  _ACTION.fields_by_name['sendGroupMessageReq'])
_ACTION.fields_by_name['sendGroupMessageReq'].containing_oneof = _ACTION.oneofs_by_name['action']
_ACTION.oneofs_by_name['action'].fields.append(
  _ACTION.fields_by_name['getGroupInfoReq'])
_ACTION.fields_by_name['getGroupInfoReq'].containing_oneof = _ACTION.oneofs_by_name['action']
_GETGROUPINFORESP.fields_by_name['group'].message_type = bot__base__pb2._GROUP
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['SendPrivateMessageReq'] = _SENDPRIVATEMESSAGEREQ
DESCRIPTOR.message_types_by_name['SendPrivateMessageResp'] = _SENDPRIVATEMESSAGERESP
DESCRIPTOR.message_types_by_name['SendGroupMessageReq'] = _SENDGROUPMESSAGEREQ
DESCRIPTOR.message_types_by_name['SendGroupMessageResp'] = _SENDGROUPMESSAGERESP
DESCRIPTOR.message_types_by_name['GetGroupInfoReq'] = _GETGROUPINFOREQ
DESCRIPTOR.message_types_by_name['GetGroupInfoResp'] = _GETGROUPINFORESP
DESCRIPTOR.enum_types_by_name['ActionType'] = _ACTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:Action)
  })
_sym_db.RegisterMessage(Action)

SendPrivateMessageReq = _reflection.GeneratedProtocolMessageType('SendPrivateMessageReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDPRIVATEMESSAGEREQ,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:SendPrivateMessageReq)
  })
_sym_db.RegisterMessage(SendPrivateMessageReq)

SendPrivateMessageResp = _reflection.GeneratedProtocolMessageType('SendPrivateMessageResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDPRIVATEMESSAGERESP,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:SendPrivateMessageResp)
  })
_sym_db.RegisterMessage(SendPrivateMessageResp)

SendGroupMessageReq = _reflection.GeneratedProtocolMessageType('SendGroupMessageReq', (_message.Message,), {
  'DESCRIPTOR' : _SENDGROUPMESSAGEREQ,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:SendGroupMessageReq)
  })
_sym_db.RegisterMessage(SendGroupMessageReq)

SendGroupMessageResp = _reflection.GeneratedProtocolMessageType('SendGroupMessageResp', (_message.Message,), {
  'DESCRIPTOR' : _SENDGROUPMESSAGERESP,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:SendGroupMessageResp)
  })
_sym_db.RegisterMessage(SendGroupMessageResp)

GetGroupInfoReq = _reflection.GeneratedProtocolMessageType('GetGroupInfoReq', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPINFOREQ,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:GetGroupInfoReq)
  })
_sym_db.RegisterMessage(GetGroupInfoReq)

GetGroupInfoResp = _reflection.GeneratedProtocolMessageType('GetGroupInfoResp', (_message.Message,), {
  'DESCRIPTOR' : _GETGROUPINFORESP,
  '__module__' : 'bot_action_pb2'
  # @@protoc_insertion_point(class_scope:GetGroupInfoResp)
  })
_sym_db.RegisterMessage(GetGroupInfoResp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)