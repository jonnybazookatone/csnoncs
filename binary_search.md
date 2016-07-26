# Binary search

Binary search is carried out by first going to the middle entry in the array. If that is the value you're lookin for, it its returned. Instead, if the value you're looking for is smaller than the one you found, a sub-array is created from the elements to the left of the central value, and the process is repeated until the value of interest is found. If the value is larger, then the sub-array is created from the right. This search only works if the array is sorted

Take this example:
```
x = [1, 3, 6, 8, 9, 10, 11]
```

We want to find the position of 6:
  1. We go to 8, 6 < 8, and so we take a sub-array of the left, [1, 3, 6]
  2. We go to 3, 6 > 3, and so we take a sub-array of the right, [6]
  3. we get 6, and the index.

There are many ways to write this algorithm:
  * recursively
  * iteratively

## Recursively

```python

def binary_search(array, value):
    centre = len(array)/2

    if value == array[centre]:
        return centre

    elif value > array[centre]:
        array = array[centre+1:]
        return binary_search(array, value) + centre + 1

    elif value < array[centre]:
        array = array[0:centre]
        return binary_search(array, value)
```

Have a look inside `bs_recursive.py` and play around. This is meant to have a big-O of O(logN). You can imagine if you are to go the furthest you can, you will repetitively make sub-arrays of half size; so you have this chain of options: N + N/2 + N/4 + N/8 + N/16 + .... + N/2^x. This grows with the number of levels (x) you need to go until you have 1 single value remaining:
```
N/2^x = 1
N = 2^x
x = log_2(N)

## Iteratively

```python
def binary_search(array, value):

    left = 0
    right = len(array)

    while left < right:
        centre = (right + left)/2

        if array[centre] == value:
            return centre

        if value > array[centre]:
            left = centre + 1
        elif value < array[centre]:
            right = centre
```

I guess a subtle note for some languages, is that the recursive algorithm will keep appending to the stack as it keeps calling the binary search, whereas in the iterative method, the stack should not grow.

# Reading

  * https://en.wikipedia.org/wiki/Binary_search_algorithm
  * http://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly
