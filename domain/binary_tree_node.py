from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from operator import le
from typing import Any


class BinaryTreeNode:
    def __init__(
        self,
        value: Any,
        parent: BinaryTreeNode = None,
        left: BinaryTreeNode = None,
        right: BinaryTreeNode = None,
    ) -> None:
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    @property
    def has_parent(self):
        return self.parent is not None

    def has_single_child(self):
        return (self.has_left and not self.has_right) or (
            self.has_right and not self.has_left
        )

    def is_leaf(self):
        return not (self.has_left or self.has_right)


class BinaryTreeCallableProgram(ABC):
    """Abstract class that enforces children to implement the __call__ method."""

    @abstractmethod
    def __call__(self, node: BinaryTreeNode):
        raise NotImplementedError(
            "Classes inheriting from BinaryTreeCallableProgram must implement __call__(node: BinaryTreeNode) method"
        )
