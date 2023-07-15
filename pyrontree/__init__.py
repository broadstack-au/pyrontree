from __future__ import annotations
from dataclasses import dataclass, field
from uuid import uuid4
import typing


@dataclass
class Tree:

    """
    A tree of nodes...
    """

    root: Node = field(default=None)

    def _get_root(self):
        if not self.root:
            self.root = Node()

        return self.root

    def add(self, node: Node, parent: Node = None) -> Node:
        """
        Add a new node to the tree, either at the root if parent is None or attached to the parent node
        """
        if not parent:
            parent = self._get_root()

        if not parent.children:
            parent.children = []

        node.parent = parent
        parent.children.append(node)

    def move(self, node: Node, parent: typing.Optional[Node] = None) -> Node:
        """
        Detatch a node from its current position and attach it to the provided parent, or the root if None
        """
        if node.parent == parent:
            return node

        if node.parent:
            self.rem(node)

        self.add(node, parent)
        return node

    def rem(self, node: Node):
        """
        Remove the node from its parent if it has one, or the root of the tree if it's there
        """

        if not node.parent:
            return

        if not node.parent.children:
            return

        _newchildren = [_node for _node in node.parent.children if _node.id != node.id]
        node.parent.children = _newchildren
        return

    def find_by_id(
        self, node_id: uuid4, base: typing.Optional[Node] = None
    ) -> typing.Optional[Node]:
        """
        Find a node within the tree based on its id.
        """

        if not base:
            base = self._get_root()

        if len(base.children) < 1:
            return None

        return self._find(node_id, base)

    def _iterfind(
        self, node_id: uuid4, nodes: typing.List[Node]
    ) -> typing.Optional[Node]:
        """
        Given a list of nodes, traverse the tree and _find for it
        """
        for node in nodes:
            _node = self._find(node_id, node)
            if _node:
                return _node

        return None

    def _find(self, node_id: uuid4, base: Node) -> typing.Optional[Node]:
        """
        Check whether the given node matches the search condition, or whether any of its children do
        """
        if base.id == node_id:
            return base

        if not base.children:
            return None

        return self._iterfind(node_id, base.children)

    def export(self) -> typing.Dict:
        """
        Return the tree structure as a tree dict
        """
        return self._get_root().export()

    def load_nodes(
        self, parent_node: Node, node_data: typing.List[typing.Dict]
    ) -> None:
        """
        Recusively process node data dict and attach the new struct to the parent node
        """
        for node in node_data:
            _children: typing.Optional[typing.List[typing.Dict]] = node.get(
                "children", None
            )

            child_node = Node(**{k: v for k, v in node.items() if k != "children"})
            if _children:
                self.load_nodes(child_node, _children)

            self.add(child_node, parent_node)

    @classmethod
    def load(cls: Tree, tree_struct: typing.Dict) -> Tree:
        """
        Create a new tree that contains the provided tree structure
        """
        _children: typing.Optional[typing.List[typing.Dict]] = tree_struct.get(
            "children", None
        )
        if not _children:
            return cls(root=Node(**tree_struct))

        base_node = Node(**{k: v for k, v in tree_struct.items() if k != "children"})
        tree: Tree = cls(root=base_node)
        tree.load_nodes(base_node, _children)
        return tree


@dataclass
class Node:
    """
    A tree node.
    """

    id: uuid4 = field(default=None)
    parent: typing.Optional[Node] = field(default=None)
    children: typing.Optional[typing.List[Node]] = field(default=None)
    data: typing.Any = field(default=None)

    def __post_init__(self):
        if not self.id:
            self.id = uuid4()

    def export(self) -> typing.Dict:
        """
        Return the node and it's children without any parent links.
        Can be passed to Tree.import
        """
        _rtn = {
            "id": self.id,
        }
        if self.data:
            _rtn["data"] = self.data
        if self.children:
            _rtn["children"] = [_child.export() for _child in self.children]

        return _rtn
