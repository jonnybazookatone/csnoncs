# ecoding: utf-8
"""
Breadth-first search
"""


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


def breadth_first_search(tree, root):

    root.distance = 0
    Q = [root]
    visited = []
    while len(Q) != 0:
        current = Q.pop(0)
        neighbours = tree[current]

        for n in neighbours:
            if n.distance == 1000:
                n.distance = current.distance + 1
                n.parent = current
                Q.append(n)
                visited.append(n.name)

    return visited
if __name__ == "__main__":

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

    print breadth_first_search(tree, root=a)

    print str(a)
    print str(b)
    print str(c)
    print str(d)
    print str(e)
    print str(f)
    print str(g)
    print str(h)

    # Let's try with their Germany example
    Frankfurt = Node(name='Frankfurt')
    Mannheim = Node(name='Mannheim')
    Wuerzburg = Node(name='Wuerzburg')
    Stuttgart = Node(name='Stuttgart')
    Kassel = Node(name='Kassel')
    Karlsruhe = Node(name='Karlsruhe')
    Erfurt = Node(name='Erfurt')
    Nuernberg = Node(name='Nuernberg')
    Augsburg = Node(name='Augsburg')
    Muenchen = Node(name='Muenchen')

    tree = {
        Frankfurt: [Mannheim, Wuerzburg, Kassel],
        Mannheim: [Frankfurt, Karlsruhe],
        Wuerzburg: [Frankfurt, Erfurt, Nuernberg],
        Stuttgart: [Nuernberg],
        Kassel: [Frankfurt, Muenchen],
        Karlsruhe: [Mannheim, Augsburg],
        Erfurt: [Wuerzburg],
        Nuernberg: [Wuerzburg, Stuttgart, Muenchen],
        Augsburg: [Karlsruhe, Muenchen],
        Muenchen: [Augsburg, Kassel]
    }

    breadth_first_search(tree, root=Frankfurt)

    print str(Frankfurt)
    print str(Mannheim)
    print str(Stuttgart)
    print str(Kassel)
    print str(Karlsruhe)
    print str(Erfurt)
    print str(Nuernberg)
    print str(Augsburg)
    print str(Muenchen)
