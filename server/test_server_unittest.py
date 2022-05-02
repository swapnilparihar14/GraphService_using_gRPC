import unittest

from graph_library import GraphLib

CREATION_FAILED = 0
INCORRECT_ID = -1
NOT_A_NODE = "nan"


class TestGraphLib(unittest.TestCase):
    """ Class performs unit tests on all graph library functions"""
    def setUp(self) -> None:
        self.graph = GraphLib()

    def test_create_graph(self) -> None:
        """ Unit tests for create_graph function in GraphLib"""
        # Positive testcase
        self.assertNotEqual(self.graph.create_graph([[1, 2], [2, 3], [4, 5]]), CREATION_FAILED)
        self.assertNotEqual(self.graph.create_graph([[1, NOT_A_NODE], [2, 3], [NOT_A_NODE, 5]]), CREATION_FAILED)

        # Negative testcase
        self.assertEqual(self.graph.create_graph([[1, None], [2, 3], [None, 5]]), CREATION_FAILED)

    def test_delete_graph(self) -> None:
        """ Unit tests for delete_graph function in GraphLib"""
        graph_id = self.graph.create_graph([[1, 2], [2, 3], [4, 5]])
        # Positive testcase
        self.assertTrue(self.graph.delete_graph(graph_id))

        # Negative testcase
        self.assertFalse(self.graph.delete_graph(INCORRECT_ID))

    def test_distance_between_nodes(self):
        """ Unit tests for distance_between_nodes function in GraphLib"""
        graph_id = self.graph.create_graph([[1, 2], [2, 3], [5, NOT_A_NODE]])
        # Positive testcase
        self.assertEqual(self.graph.distance_between_nodes(graph_id, 1, 3), "[1, 2, 3]")
        self.assertEqual(self.graph.distance_between_nodes(graph_id, 1, 5), "Error: No path between 1 and 5.")

        # Negative testcase
        self.assertEqual(self.graph.distance_between_nodes(graph_id, 1, 6),
                         "Error: Either source 1 or target 6 is not in G")
