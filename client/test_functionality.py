import pytest
import unittest

from client import run
from client_variables import *
from unittest.mock import patch


class TestClient(unittest.TestCase):
    """Performs end-to-end functional testing """

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    @patch('builtins.input')
    def test_create_graph_client(self, m_input):
        """
        Checks the end to end graph creation functionality
        :param m_input:
        :return:
        """
        m_input.side_effect = [CREATE_GRAPH, SAMPLE_CSV, EXIT]
        run()
        captured = self.capsys.readouterr()
        graph_id = captured.out.split(':')[-1]
        graph_id = int("".join(graph_id.split()))
        self.assertGreater(graph_id, 0)

    @patch('builtins.input')
    def test_delete_graph_client(self, m_input):
        m_input.side_effect = [CREATE_GRAPH, SAMPLE_CSV, EXIT]
        run()
        captured = self.capsys.readouterr()
        graph_id = captured.out.split(':')[-1]
        graph_id = int("".join(graph_id.split()))
        m_input.side_effect = [DELETE_GRAPH, str(graph_id), EXIT]
        run()
        captured = self.capsys.readouterr()
        self.assertTrue(DELETED in captured.out)

    @patch('builtins.input')
    def test_distance_between_nodes_client(self, m_input):
        m_input.side_effect = [CREATE_GRAPH, SAMPLE_CSV, EXIT]
        run()
        captured = self.capsys.readouterr()
        graph_id = captured.out.split(':')[-1]
        graph_id = int("".join(graph_id.split()))

        # Change if there are changes made to sample_data.csv file
        source_node = "1"
        target_node = "2"
        m_input.side_effect = [DISTANCE_BETWEEN_NODES, str(graph_id), source_node, target_node, EXIT]
        run()
        captured = self.capsys.readouterr()
        self.assertTrue("['1', '2']" in captured.out)


if __name__ == '__main__':
    unittest.main()