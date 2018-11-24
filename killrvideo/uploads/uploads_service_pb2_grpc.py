# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from uploads import uploads_service_pb2 as uploads_dot_uploads__service__pb2


class UploadsServiceStub(object):
  """Service that handles processing/re-encoding of uploaded videos
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUploadDestination = channel.unary_unary(
        '/killrvideo.uploads.UploadsService/GetUploadDestination',
        request_serializer=uploads_dot_uploads__service__pb2.GetUploadDestinationRequest.SerializeToString,
        response_deserializer=uploads_dot_uploads__service__pb2.GetUploadDestinationResponse.FromString,
        )
    self.MarkUploadComplete = channel.unary_unary(
        '/killrvideo.uploads.UploadsService/MarkUploadComplete',
        request_serializer=uploads_dot_uploads__service__pb2.MarkUploadCompleteRequest.SerializeToString,
        response_deserializer=uploads_dot_uploads__service__pb2.MarkUploadCompleteResponse.FromString,
        )
    self.GetStatusOfVideo = channel.unary_unary(
        '/killrvideo.uploads.UploadsService/GetStatusOfVideo',
        request_serializer=uploads_dot_uploads__service__pb2.GetStatusOfVideoRequest.SerializeToString,
        response_deserializer=uploads_dot_uploads__service__pb2.GetStatusOfVideoResponse.FromString,
        )


class UploadsServiceServicer(object):
  """Service that handles processing/re-encoding of uploaded videos
  """

  def GetUploadDestination(self, request, context):
    """Gets an upload destination for a user to upload a video
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MarkUploadComplete(self, request, context):
    """Marks an upload as complete
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatusOfVideo(self, request, context):
    """Gets the status of an uploaded video
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UploadsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUploadDestination': grpc.unary_unary_rpc_method_handler(
          servicer.GetUploadDestination,
          request_deserializer=uploads_dot_uploads__service__pb2.GetUploadDestinationRequest.FromString,
          response_serializer=uploads_dot_uploads__service__pb2.GetUploadDestinationResponse.SerializeToString,
      ),
      'MarkUploadComplete': grpc.unary_unary_rpc_method_handler(
          servicer.MarkUploadComplete,
          request_deserializer=uploads_dot_uploads__service__pb2.MarkUploadCompleteRequest.FromString,
          response_serializer=uploads_dot_uploads__service__pb2.MarkUploadCompleteResponse.SerializeToString,
      ),
      'GetStatusOfVideo': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatusOfVideo,
          request_deserializer=uploads_dot_uploads__service__pb2.GetStatusOfVideoRequest.FromString,
          response_serializer=uploads_dot_uploads__service__pb2.GetStatusOfVideoResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'killrvideo.uploads.UploadsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
