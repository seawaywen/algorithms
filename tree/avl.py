#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bst import BST


def height(node):
    return -1 if node is None else node.height


class AVL(BST):
    def update_height(self, node):
        node.height = max(height(node.left), height(node.right)) + 1

    def rotate_left(self, k2):
        k1 = k2.right
        k1.parent = k2.parent
        if k1.parent:
            if k2 is k1.parent.left:
                k1.parent.left = k1
            elif k2 is k1.parent.right:
                k1.parent.right = k1

        k2.right = k1.left
        if k2.right:
            k2.right.parent = k2

        k1.left = k2
        k2.parent = k1

        self.update_height(k2)
        self.update_height(k1)

    def rotate_right(self, k2):
        k1 = k2.left
        k1.parent = k2.parent
        if k1.parent:
            if k2 is k1.parent.left:
                k1.parent.left = k1
            elif k2 is k1.parent.right:
                k1.parent.right = k1

        k2.left = k1.right
        if k2.left:
            k2.left.parent = k2

        k1.right = k2
        k2.parent = k1

        self.update_height(k2)
        self.update_height(k1)

    def reblance(self, node):
        while node:
            self.update_height(node)

            if height(node.left) - height(node.right) >= 2:
                if height(node.left.left) < height(node.left.right):
                    self.rotate_left(node.left)

                self.rotate_right(node)

            elif height(node.right) - height(node.left) >= 2:
                if height(node.right.right) < height(node.right.left):
                    self.rotate_right(node.right)

                self.rotate_left(node)

            node = node.parent

    def insert(self, k):
        node = super().insert(k)
        self.reblance(node)
        return node

    def delete(self, k):
        node = super().delete(k)
        self.reblance(node)
        return node


str_list = '8 9 12 3 5 7 39 13 45 2'
data_list = [int(i) for i in str_list.split(' ')]
tree = AVL()
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
