# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import graph_pb2 as graph__pb2


class GraphOperationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGraph = channel.unary_unary(
                '/data.GraphOperations/CreateGraph',
                request_serializer=graph__pb2.Graph.SerializeToString,
                response_deserializer=graph__pb2.CreateResponse.FromString,
                )
        self.GetDistance = channel.unary_unary(
                '/data.GraphOperations/GetDistance',
                request_serializer=graph__pb2.SourceTarget.SerializeToString,
                response_deserializer=graph__pb2.DistResponse.FromString,
                )
        self.DeleteGraph = channel.unary_unary(
                '/data.GraphOperations/DeleteGraph',
                request_serializer=graph__pb2.GraphId.SerializeToString,
                response_deserializer=graph__pb2.DeleteResponse.FromString,
                )


class GraphOperationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGraph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDistance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGraph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GraphOperationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGraph': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGraph,
                    request_deserializer=graph__pb2.Graph.FromString,
                    response_serializer=graph__pb2.CreateResponse.SerializeToString,
            ),
            'GetDistance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDistance,
                    request_deserializer=graph__pb2.SourceTarget.FromString,
                    response_serializer=graph__pb2.DistResponse.SerializeToString,
            ),
            'DeleteGraph': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGraph,
                    request_deserializer=graph__pb2.GraphId.FromString,
                    response_serializer=graph__pb2.DeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data.GraphOperations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GraphOperations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGraph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.GraphOperations/CreateGraph',
            graph__pb2.Graph.SerializeToString,
            graph__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDistance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.GraphOperations/GetDistance',
            graph__pb2.SourceTarget.SerializeToString,
            graph__pb2.DistResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGraph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data.GraphOperations/DeleteGraph',
            graph__pb2.GraphId.SerializeToString,
            graph__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
