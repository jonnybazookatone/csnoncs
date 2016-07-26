"""
Binary search algorithm, recursive example
"""

def binary_search(array, value):

    centre = len(array)/2
    print 'Current centre: index[{}] = {}\n'.format(centre, array[centre])  

    if value == array[centre]:
        print 'Centre [{}] == value [{}] at index {}\n'.format(array[centre], value, centre)
        return centre

    elif value > array[centre]:
        print 'Centre [{}] < value [{}], new sub-array {}'.format(array[centre], value, array[centre+1:])
        array = array[centre+1:]
        index = binary_search(array, value)
        print 'Returning: {}\n'.format(index+centre+1)
        return index + centre + 1

    elif value < array[centre]:
        print 'Centre [{}] > value [{}], new sub-array {}'.format(array[centre], value, array[0:centre])
	array = array[0:centre]
        index = binary_search(array, value)
        print 'Returning: {}\n'.format(index)
        return index


x = [1, 3, 6, 8, 9, 10, 11]

index = binary_search(array=x, value=8)
assert index == 3 
print '\n\n'

print x, ' looking for 6'
index = binary_search(array=x, value=6)
print 'Index: {}'.format(index)
assert index == 2
print ''

print x, 'looking for 10'
index = binary_search(array=x, value=9)
assert index == 4
print 'Index: {}'.format(index)



x = [1, 2]
print x, 'looking for 10'
index = binary_search(array=x, value=1)
assert index == 0
print 'Index: {}'.format(index)

x = [1, 2, 3, 4]
print x, 'looking for 10'
index = binary_search(array=x, value=1)
assert index == 0
print 'Index: {}'.format(index)

