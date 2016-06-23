# Linked Lists



Normal arrays have the limitation of fixed size, as they are first defined (in C at least). Waste memory when you allocate randomly large array sizes. Insertion at the beginning of the array is also expensive, as each item as to be moved along once. When allocating memory to an array, it is all done at once on the heap.

A linked list should address a lot of these features. A linked list consists of distinc *nodes*, where each node holds the *value* and a *pointer*. The *pointer* points to the next value in the list. This allows the memory allocation to be done invidiually for each node in the list. These lists, however, take longer traverse and the time grows linearly with the number of additions, unlike that of normal arrays for which you can access directly an index.

A hackish way of demonstrating a linked list in Python using dicts:
```Python
def get_length(head):
  counter = 0
  current = head
  while current != None:
    counter += 1
    current = current['next']

  return counter

# Setup the linked list
head = {'data': 1, 'next': None}
first = {'data': 1, 'next': None}
second = {'data': 1, 'next': None}

head['next'] = first
first['next'] = second


print get_length(head)
>>> 3
```

Prepending to a linked list
```Python

def prepend(new_head, old_head):
  new_head['next'] = old_head
  return new_head

# Setup the linked list
head = {'data': 1, 'next': None}
first = {'data': 1, 'next': None}
second = {'data': 1, 'next': None}

head['next'] = first
first['next'] = second

new_head = {'data': 4, 'next': None}

head = prepend(new_head, head)

print get_length(head)
>>> 4
```

# Alternative linked lists

 * **Circular**: the last entry in the list points back to the head
 * **Tail Pointer**: the list is characterised with two pointers, one to the head, and one to the tail, making pushing/appending easier
 * **Head/dummy Struct**: a way to get around the first instance of pushing a new value onto an empty linked list. One is to have a dummy entry, the other is to have header information.
 * **Doubly Linked**: both a *previous* and *next* operation
 * **Chunked List**: put more entries in a single node to improve performance if required
 * **Dynamic Array**: instead of using linked lists can just allocate memory in the heap, and deallocate when remove an entry

# Reading and references

  * http://cslibrary.stanford.edu/103/LinkedListBasics.pdf


