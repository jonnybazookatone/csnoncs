"""
Binary search algorithm, iterative example
"""

def binary_search(array, value):

    left = 0
    right = len(array)
    centre = (right + left)/2

    while left < right:

         if array[centre] == value:
             return centre

         if value > array[centre]:
             print 'Centre [{}] < value [{}]'.format(array[centre], value)
             left = centre + 1
             centre = (right + left)/2
             print 'New left: {}, new centre: {}'.format(left, centre)

         elif value < array[centre]:
             print 'Centre [{}] > value [{}]'.format(array[centre], value)
             right = centre
             centre = (right + left)/2         
             print 'New right: {}, new centre: {}'.format(right, centre)

x = [1, 3, 6, 8, 9, 10, 11]

index = binary_search(array=x, value=8)
assert index == 3 
print '\n\n'

print x, ' looking for 6'
index = binary_search(array=x, value=6)
print 'Index: {}'.format(index)
assert index == 2
print ''

print x, 'looking for 9'
index = binary_search(array=x, value=9)
assert index == 4
print 'Index: {}'.format(index)



x = [1, 2]
print x, 'looking for 1'
index = binary_search(array=x, value=1)
assert index == 0
print 'Index: {}'.format(index)

x = [1, 2, 3, 4]
print x, 'looking for 1'
index = binary_search(array=x, value=1)
assert index == 0
print 'Index: {}'.format(index)


x = [1, 2, 3, 4]
print x, 'looking for non-existent 5'
index = binary_search(array=x, value=5)
print index
