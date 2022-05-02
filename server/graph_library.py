import networkx as nx
from server_variables import NOT_A_NODE, INT64_LIMIT, ERROR, GRAPH_NOT_FOUND
from typing import Union


class GraphLib:

    def __init__(self) -> None:
        """
        Constructor for the graph library
        """
        self._graph_dic = {0: 1}
        self._graph_id = 0

    def create_graph(self, edge_list: list) -> int:
        """
        Creates a graph from a list of tuples representing edges
        :param edge_list:
        :return: Graph ID for the generated graph
        """
        try:
            graph = nx.Graph()
            for edge in edge_list:
                if NOT_A_NODE not in edge:
                    graph.add_edge(*edge)
                elif edge[0] != NOT_A_NODE:
                    graph.add_node(edge[0])
                elif edge[1] != NOT_A_NODE:
                    graph.add_node(edge[1])

            if self._graph_id == INT64_LIMIT:
                self._graph_id = 1
            while self._graph_id in self._graph_dic:
                self._graph_id += 1
            self._graph_dic[self._graph_id] = graph
            return self._graph_id
        except:
            return 0

    def distance_between_nodes(self, graph_identifier: int, source: Union[int, str],
                               destination: Union[int, str]) -> str:
        """
        Computes all shortest paths between source and destination nodes
        :param graph_identifier: ID of the graph that will be parsed
        :param source: Name of the source node
        :param destination: Name of target node
        :return: A list of the smallest path between the source and destination node
        """
        try:
            graph_value = self._graph_dic[graph_identifier]
        except:
            return GRAPH_NOT_FOUND
        try:
            return str(nx.shortest_path(graph_value, source=source, target=destination))
        except Exception as e:
            return f"{ERROR}{e}"

    def delete_graph(self, graph_identifier: int) -> bool:
        """
        Deletes an existing graph if present
        :param graph_identifier: Identifier of the graph
        :return: Success or failure
        """
        try:
            self._graph_dic.pop(graph_identifier)
            return True
        except:
            return False
