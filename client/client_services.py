from os.path import exists, splitext
import graph_pb2
import pandas as pd
from client_variables import *


class Client:

    def __init__(self, stub) -> None:
        """
        Constructor
        """
        self.stub = stub

    def create_graph(self) -> None:
        """
        Creates a new graph on the server
        :return: Prints output indicating if creation was successful or not
        """
        data = self.get_graph_csv(input(REQUEST_FILE))
        if data[SUCCESS]:
            reply = self.stub.CreateGraph(graph_pb2.Graph(graph=data[MESSAGE]))
            print(GRAPH_ID_TEXT, reply.response)
        else:
            print(ERROR_PREFIX,data[MESSAGE])

    def get_graph_csv(self, filename: str) -> dict:
        """
        Helper function to validate input csv file
        :param filename: CSV file containing the edges in the graph
        :return: A dictionary with operation status and corresponding message/data
        """
        file, file_extension = splitext(filename)
        if exists(filename):
            if file_extension == CSV:
                try:
                    df = pd.read_csv(filename, header=None, dtype=str)
                    if df.shape[1] == 2:
                        records = df.to_records(index=False)
                        return {SUCCESS: True,
                                MESSAGE: [graph_pb2.Edge(start=str(edge[0]), end=str(edge[1])) for edge in records]}
                    else:
                        return {SUCCESS: False, MESSAGE: INVALID_CONTENT}
                except Exception as e:
                    return {SUCCESS: False, MESSAGE: e}
            else:
                return {SUCCESS: False, MESSAGE: INVALID_EXTENSION}
        else:
            return {SUCCESS: False, MESSAGE: MISSING_FILE}

    def delete_graph(self) -> None:
        """
        Deletes an existing graph
        :return: Prints action status
        """
        graph_id = input(REQUEST_GRAPH_ID)
        try:
            reply = self.stub.DeleteGraph(graph_pb2.GraphId(graphid=graph_id))
            if reply:
                print(GRAPH_RESPONSE, graph_id, DELETED)
            else:
                print(GRAPH_RESPONSE, graph_id, NOT_DELETED)
        except Exception as e:
            print(ERROR_PREFIX, e)

    def get_distance_between_two_nodes(self) -> None:
        """
        Displays the path between two nodes in the form of a list
        :return: Prints action results
        """
        graph_id = input(REQUEST_GRAPH_ID)
        source = input(REQUEST_SOURCE_NODE)
        target = input(REQUEST_TARGET_NODE)
        try:
            reply = self.stub.GetDistance(graph_pb2.SourceTarget(source=source, target=target, graphid=graph_id))
            print(RESPONSE, reply.response)
        except Exception as e:
            print(ERROR_PREFIX, e)
