import logging
import grpc
import graph_pb2_grpc
from client_services import Client
from client_variables import *


def run() -> None:
    """ Implements all client side functionality """
    while True:
        user_input = input(WELCOME_MESSAGE)
        with grpc.insecure_channel(NETWORK_ADDRESS) as channel:
            stub = graph_pb2_grpc.GraphOperationsStub(channel)
            client = Client(stub)
            if user_input == CREATE_GRAPH:
                client.create_graph()
            elif user_input == DISTANCE_BETWEEN_NODES:
                client.get_distance_between_two_nodes()
            elif user_input == DELETE_GRAPH:
                client.delete_graph()
            else:
                break


if __name__ == '__main__':
    logging.basicConfig()
    run()
