from edge import PsqlEdge
from node import PsqlNode
from sqlalchemy.orm import Query


class GraphQuery(Query):
    """Query subclass implementing graph specific operations."""

    def with_edge_to_node(self, edge_label, target_node):
        """Returns a new query that filters the query to just those nodes that
        have an edge with label ``edge_label`` to ``target_node``.

        :param str edge_label: label of the edge to use for restricting
        :param PsqlNode target_node: node used to filter the result set such
        that each result node must be the source of an edge whose
        destination is ``target_node``

        """

        assert self._entity_zero().type == PsqlNode
        # first we construct a subquery for edges of the correct label
        # to the target_node
        session = self.session
        sq = session.query(PsqlEdge).filter(PsqlEdge.label == edge_label)\
                                    .filter(PsqlEdge.dst_id == target_node.node_id)\
                                    .subquery()
        return self.filter(PsqlNode.node_id == sq.c.src_id)

    def with_edge_from_node(self, edge_label, source_node):
        """Like ``with_edge_to_node``, but in the opposite direction.  Filters
        the query such that ``source_node`` must have an edge pointing
        to a node in the result set.

        :param str edge_label: label of the edge to use for
        restricting :param PsqlNode source_node: node used to filter
        the result set such that each result node must be the dst of an edge that
        originates at ``source_node``.

        """

        assert self._entity_zero().type == PsqlNode
        # first we construct a subquery for edges of the correct label
        # to the target_node
        session = self.session
        sq = session.query(PsqlEdge).filter(PsqlEdge.label == edge_label)\
                                    .filter(PsqlEdge.src_id == source_node.node_id)\
                                    .subquery()
        return self.filter(PsqlNode.node_id == sq.c.dst_id)