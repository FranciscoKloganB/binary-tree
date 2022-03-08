from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class BinaryTreeNode:
    parent: BinaryTreeNode | None
    left: BinaryTreeNode | None
    right: BinaryTreeNode | None
    value: Any

    @property
    def has_left(self):
        return self.left is not None

    @property
    def has_right(self):
        return self.right is not None

    @property
    def has_parent(self):
        return self.parent is not None

    @property
    def is_leaf(self):
        return not (self.has_left or self.has_right)


class BinaryTreeCallableProgram(ABC):
    """Abstract class that enforces children to implement the __call__ method."""

    @abstractmethod
    def __call__(self, node: BinaryTreeNode):
        raise NotImplementedError(
            "Classes inheriting from BinaryTreeCallableProgram must implement __call__(node: BinaryTreeNode) method"
        )
