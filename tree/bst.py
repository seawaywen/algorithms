#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    """A node for the tree"""
    def __init__(self, parent, key):
        """init a node

        Args:
            parent: node's parent
            key: node's key
        """
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None


class BSTNode(Node):
    """A node for BST tree"""

    def _str(self):
        """Internal method for ASCII art dispaly."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
           self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

    def find(self, k):
        """return the node with key k from the subtree from this
        node as the root.

        Args:
            k: the key of node to be searched

        Returns:
            the node with key k
        """
        if k is None:
            return None

        if k == self.key:
            return self
        elif k < self.key:
            if self.left:
                return self.left.find(k)
            return None
        else:
            if self.right:
                return self.right.find(k)
            return None

    def find_min(self):
        """Find the node with smallest key in the subtree from this
        node as the root

        Returns:
            the node with minimum key
        """
        current = self
        while current.left:
            current = current.left
        return current

    def find_successor(self):
        """Find the node with next larger key

        Returns:
            the node with the next larger key in the subtree from this
            node as the root
        """
        if self.right:
            return self.right.find_min()
        current = self
        while current.parent and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):
        """Insert the node into the subtree rooted at this node

        Args:
            node: the node to be inserted

        """
        if node is None:
            return None

        if node.key < self.key:
            if self.left:
                return self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right:
                return self.right.insert(node)
            else:
                node.parent = self
                self.right = node

    def delete(self):
        """Delete and return this node"""
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right:
                    self.parent.right.parent = self.parent
            deleted = self
        else:
            s = self.find_successor()
            s.key, self.key = self.key, s.key
            deleted = s.delete()

        return deleted

class BST:
    """A binary search tree"""

    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root is None:
            return '<empty tree>'
        else:
            return str(self.root)

    def find(self, k):
        """Find the node with key k in the subtree has the root as this node

        Args:
            k: key of node to be searched
        """
        return self.root and self.root.find(k)

    def find_min(self):
        """Find the node with minimum key in the tree"""
        return self.root and self.root.find_min()

    def find_successor(self, k):
        """Find the node with the next larger key in the BST tree

        Args:
            k: the key of the node of which successor to be found

        Returns:
            the node with next larger key
        """
        node = self.find(k)
        return node and node.find_successor()

    def insert(self, k):
        """Insert a node with key k into the subtree has the root as this node

        Args:
            k: the key of the node to be inserted
        """
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)
        return node

    def delete(self, k):
        """Delete and return the node with the key k if it exists

        Args:
            k: the key of the node to be deleted

        Returns:
            the deleted node with the key k
        """
        node = self.find(k)
        if node is self.root:
            new_node = BSTNode(None, 0)
            new_node.left = self.root
            self.root.parent = new_node
            deleted = self.root.delete()
            self.root = new_node.left
            if self.root:
                self.root.parent = None
        else:
            deleted = node.delete()

        return deleted


if __name__ == '__main__':
    str_list = '8 9 12 3 5 7 39 13 45 2'
    data_list = [int(i) for i in str_list.split(' ')]
    tree = BST()
    for i in data_list:
        tree.insert(i)

    print(tree)

    print('*' * 10)
    print('delete 39 now...')
    tree.delete(39)
    print(tree)

    print('*' * 10)

    print('insert 4 now...')
    tree.insert(4)
    print(tree)

    print('delete ROOT 8 now...')
    tree.delete(8)
    print(tree)

    print('delete 2 now...')
    tree.delete(2)
    print(tree)
