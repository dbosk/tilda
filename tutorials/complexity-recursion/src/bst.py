#!/bin/env python3
""" Binary search trees """

class Node:
    """A node in a binary search tree"""
    def __init__(self, key, value, left=None, right=None):
        """A node consists of key, value; left, right"""
        self.__key = key
        self.value = value
        self.left = left
        self.right = right

    @property
    def key(self):
        """Read-only property key"""
        return self.__key

    def __str__(self):
        return str(self.value)


def insert(root: Node, key, value):
    """Insert key:value into the binary tree"""
    if not root:
        return Node(key, value)

    if root.key == key:
        root.value = value
    elif key < root.key:
        root.left = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)

    return root

def find(root: Node, key):
    """Find the node with key in the binary tree"""
    if not root or root.key == key:
        return root
    if key < root.key:
        return find(root.left, key)
    # key > root.key:
    return find(root.right, key)

def inorder(root: Node):
    """Return a string with the tree in in-order"""
    if not root:
        return ""
    return f"{inorder(root.left)} {root.value} {inorder(root.right)}"

def preorder(root: Node):
    """Return a string with the tree in pre-order"""
    if not root:
        return ""
    return f"{root.value} {preorder(root.left)} {preorder(root.right)}"

def postorder(root: Node):
    """Return a string with the tree in post-order"""
    if not root:
        return ""
    return f"{postorder(root.left)} {postorder(root.right)} {root.value}"


if __name__ == "__main__":
    values1 = [4, 2, 1, 6, 3, 7, 5]
    tree1 = None
    values2 = [5, 7, 3, 6, 1, 4, 2]
    tree2 = None

    for value in values1:
        tree1 = insert(tree1, value, value)

    print(f"inorder = {inorder(tree1)}")
    print(f"preorder = {preorder(tree1)}")
    print(f"postorder = {postorder(tree1)}")

    for value in values2:
        tree2 = insert(tree2, value, value)

    print(f"inorder = {inorder(tree2)}")
    print(f"preorder = {preorder(tree2)}")
    print(f"postorder = {postorder(tree2)}")

