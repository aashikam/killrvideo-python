# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from statistics import statistics_service_pb2 as statistics_dot_statistics__service__pb2


class StatisticsServiceStub(object):
  """Service that tracks playback statistics for videos
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RecordPlaybackStarted = channel.unary_unary(
        '/killrvideo.statistics.StatisticsService/RecordPlaybackStarted',
        request_serializer=statistics_dot_statistics__service__pb2.RecordPlaybackStartedRequest.SerializeToString,
        response_deserializer=statistics_dot_statistics__service__pb2.RecordPlaybackStartedResponse.FromString,
        )
    self.GetNumberOfPlays = channel.unary_unary(
        '/killrvideo.statistics.StatisticsService/GetNumberOfPlays',
        request_serializer=statistics_dot_statistics__service__pb2.GetNumberOfPlaysRequest.SerializeToString,
        response_deserializer=statistics_dot_statistics__service__pb2.GetNumberOfPlaysResponse.FromString,
        )


class StatisticsServiceServicer(object):
  """Service that tracks playback statistics for videos
  """

  def RecordPlaybackStarted(self, request, context):
    """Record that playback started for a given video
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNumberOfPlays(self, request, context):
    """Get the number of plays for a given video or set of videos
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StatisticsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RecordPlaybackStarted': grpc.unary_unary_rpc_method_handler(
          servicer.RecordPlaybackStarted,
          request_deserializer=statistics_dot_statistics__service__pb2.RecordPlaybackStartedRequest.FromString,
          response_serializer=statistics_dot_statistics__service__pb2.RecordPlaybackStartedResponse.SerializeToString,
      ),
      'GetNumberOfPlays': grpc.unary_unary_rpc_method_handler(
          servicer.GetNumberOfPlays,
          request_deserializer=statistics_dot_statistics__service__pb2.GetNumberOfPlaysRequest.FromString,
          response_serializer=statistics_dot_statistics__service__pb2.GetNumberOfPlaysResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'killrvideo.statistics.StatisticsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
