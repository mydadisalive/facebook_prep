#!/usr/bin/python3

class Node:
    ''' Class Tree Definition. '''

    val = None
    left = None
    right = None
    parent = None

    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def print(self):
        if self.val == None:
            return
        print(self.val)
        if self.left is not None:
            self.left.print()
        if self.right is not None:
            self.right.print()


def commonAncestor(p,q):
    ''' Return the closest common ancestor of two node p and q. Assumes such exists. '''

    if p == None or q == None:
        return

    path_p = []
    path_q = []
    p_prev = None
    q_prev = None
    p_orig = p
    q_orig = q

    while p is not None:
        #print(p.val)
        path_p = [p] + path_p
        p = p.parent

    while q is not None:
        path_q = [q] + path_q
        q = q.parent

    print([x.val for x in path_p])
    print([x.val for x in path_q])

    for i in range(min(len(path_p),len(path_q))):
        if path_p[i] is not path_q[i]:
            return path_p[i-1]

    if i == 0:
        return None
    return path_p[i-1]

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

#       1
#    2    3
#  4   5
# 6 7 8 9

n1.left = n2
n1.right = n3
n2.parent = n1
n3.parent = n1
n2.left = n4
n2.right = n5
n4.parent = n2
n5.parent = n2
n4.left = n6
n4.right = n7
n6.parent = n4
n7.parent = n4
n5.left = n8
n5.right = n9
n8.parent = n5
n9.parent = n5

t = n1
t.print()

ca = commonAncestor(n6,n9)
if ca is not None:
    print(ca.val)
else:
    print(None)
