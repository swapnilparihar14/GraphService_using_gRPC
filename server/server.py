import grpc
import graph_pb2
import graph_pb2_grpc
from graph_library import GraphLib
from concurrent import futures
from server_variables import SERVER_STARTED, PORT_ADDRESS

GRAPH_ARR = GraphLib()


class GraphOperationsServicer(graph_pb2_grpc.GraphOperationsServicer):

    def CreateGraph(self, request, context):
        edge_list = [(edge.start, edge.end) for edge in request.graph]
        return graph_pb2.CreateResponse(response=GRAPH_ARR.create_graph(edge_list=edge_list))

    def GetDistance(self, request, context):
        return graph_pb2.DistResponse(response=GRAPH_ARR.distance_between_nodes(int(request.graphid), request.source,
                                                                                request.target))

    def DeleteGraph(self, request, context):
        return graph_pb2.DeleteResponse(response=GRAPH_ARR.delete_graph(int(request.graphid)))


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    graph_pb2_grpc.add_GraphOperationsServicer_to_server(GraphOperationsServicer(), server)
    print(SERVER_STARTED)
    server.add_insecure_port(PORT_ADDRESS)
    server.start()
    server.wait_for_termination()


main()
