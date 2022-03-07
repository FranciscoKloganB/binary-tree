from __future__ import annotations

from domain.binary_tree import *


class PrintBinaryTreeProgram(BinaryTreeCallableProgram):
    def __call__(node: BinaryTreeNode):
        return print(node.value)

if __name__ == "__main__":
    print("Hello world.")
