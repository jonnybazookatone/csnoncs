# Breadth-first search

Breadth-first search is an algorithm used to traverse tree or graph-like data structures. The main feature is that it traverses first the neighbours in the tree, before it goes to the next level of nodes.

The node is marked by a distance, so if the bread-first search meets that node again while traversing some other nodes neighbours, it is not added to the chain.


Let's put this in Python following the example pseudo code on wikipedia: https://en.wikipedia.org/wiki/Breadth-first_search

First I'll make a node class

```Python
class Node(object):
    def __init__(self, name='node', distance=1000, parent=None):
        self.name = name
        self.distance = distance
        self.parent = parent

    def __repr__(self):
        return self.name

    def __str__(self):
        if self.parent:
            name = self.parent.name
        else:
            name = 'root'
        return 'Name: {}\nDistance: {}\nParent: {}\n\n'.format(self.name, self.distance, name)
```

Then set up a simple tree using 1-level of a python dictionary:
```python
a = Node(name='a')
b = Node(name='b')
c = Node(name='c')
d = Node(name='d')
e = Node(name='e')
f = Node(name='f')
g = Node(name='g')
h = Node(name='h')

tree = {
    a: [b, c],
    b: [a, d, e],
    c: [a, f, g],
    d: [b],
    e: [b, h],
    f: [c],
    g: [c],
    h: [e]
}
```

Then we can write the pseudo code:
```Python
def breadth_first_search(tree, root):

    root.distance = 0
    Q = [root]

    while len(Q) != 0:
        current = Q.pop(0)
        neighbours = tree[current]

        for n in neighbours:
            if n.distance == 1000:
                n.distance = current.distance + 1
                n.parent = current
                Q.append(n)
```


and then run the script and print the output:
```python
Name: a
Distance: 0
Parent: root

Name: b
Distance: 1
Parent: a

Name: c
Distance: 1
Parent: a

Name: d
Distance: 2
Parent: b

Name: e
Distance: 2
Parent: b

Name: f
Distance: 2
Parent: c

Name: g
Distance: 2
Parent: c

Name: h
Distance: 3
Parent: e
```





