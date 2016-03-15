## Hash maps

*Note: this is not meant to replace the extensive information found and copied from https://en.wikipedia.org/wiki/Hash_table*.

A hash map is a structure that implements *associative arrays*, ie., an array for which a given key points to a given index. For example, in Python:
```python
x = {
 'key1': 100,
 'key2': 200
}

print 'lookup the value for key1:'
print x['key1']
>>> 100
```




This is done by:
  1. First, converting the key to a hash, via a hash function `hash = hf(key)`
  2. Second, allocating an index to the hash for its value in the value array `index = hash % array_size`
  3. The value is then obtained via `value = f(key, array_size)`

Hash maps are usuall independent of the number of keys in the array, and as such are O(1). As a result, they are commonly used for tasks such as indexing and caching.

The speed at which they run depends highly on the hash function. Occasionally, the hash function can lead to two hashes pointing to the same key; **collisions**.

### Load Factor

A key statistic used by hash tables is the *Load Factor*:
```python
  load_factor = n / k
```
`n` is the number of entries in the array
`k` is the number of buckets

*buckets* refers to the number of *areas* at which a hash points to. Normally, one hash points to 1 bucket, but this is not always true, and is how *collisions* arise. Therefore, if there is a *high load*, then there is more than one value in a given bucket and so the look-up time will take longer. If there is a *low load* then this is equally bad, as there are more buckets available than keys used, which means memory is being used up - given the fastest this can be is O(1), there is no advantage to have extra free buckets.

### Collision Resolution

Some hashing functions can lead to more than one value existing in a given bucket. To get around this, they usually have a way to resolve collisions.

* **Separate Chaining**: each bucket is independent, and contains a list of keys. The time for look-up is then O(1)+t(list operation).

 * *linked lists*: A bucket uses linked lists; ie, each element also has a pointer to the next element in the list. This takes `O(1)+(O(n_bucket)) ~ O(1)+load_factor`. This can be sped up by using *ordered lists*.

 * *list head cells*: The first entry sits inside the bucket, with the following entries in a linked list. This can reduce the look-up speed by 1 entry, but empty buckets still take up space (reducing load).

 * *other structures*: It is possible to use more complex structures to reduce the look up time, rather than using linked lists, where O(logn) is viable.

* **Open Addressing / Closed Hashing**: This first looks up the bucket via the hash. It then proceeds to look for an open slot in a certain manner, until it finds one. On hash look-up, the look up will go through the slots until the value is found (or it finds an empty entry). The open slots traveresed is called *probing* and can be done in different ways:
 * *linear probing*: interval between probes is 1
 * *quadratic probing*: goes with a quadratic polynomial
 * *double hashing*: another hash is used to find the slot

 Open addressing is limited by the size of the buckets

* **Colaesced Hashing**: A hybrid of chained lists and open addressing.

* **Cookoo Hashing**: Uses three hash functions. When trying to create a hash, if there is a collision, the second hash is used, if there is a third the third hash is used. If there is still a collision, the collided key is replaced by the new key, and the old key is rehashed using the second and third hash functions. This is repeated until there are no more collisions. If the entire table is traversed, the table size is increased.

* **Hopscotch Hasing**: Similar to cookoo hashing and open addressing. First it tries to place the key at the hash look up position. If there is a collision, it looks for an empty slot within a given *neighbourhood*. If a slot is found outside the *neighbourhood*, the slot is *hopscotched* to be within the *neighbourhood* of the hash.

* **Robinhood Hashing**: Uses double-hashing, except when a new key tries to fill a slot taken by another key, the new key replaced the old key if the probing distance (defined by the double hashing) is larger for the old key than the new. ( Needs more explanation)

* **2-choice Hashing**: 2 hashing functions are used. The key is placed in the slot that has fewer keys.

* **Leapfrog probing**: At each bucket there are also two delta values stored. The first delta refers to the **probe length for the next item, in a different bucket**, and the second to the **probe length for the next iteme in the same bucket**. If either are 0, that means it is the end of the probe length for that bucket. When the second delta is 0, it carries on using linear probing. So it can be slow on the first insertion, however, is faster on look-up. A nice description is given <a href='http://preshing.com/20160314/leapfrog-probing/'>here</a>.

### Dynamic Resizing
Tables may reach a load larger than that needed, and as a result, need to resize (and thus rehash). The alternate is true when the table can reduce its size to reduce memory consumption.

Incremental resizing is normally used, whereby the hash map is not completely rebuilt on disk, but is instead rebuild on each insert. One each insert, a new table is used to place the new entry, and *r* entries are copied from the old table. When all the old entries have been copied over, the old table is freed from memory. During the period there are two tables, look-ups will occur on both of them.

### Uses

 * Associative Arrays in interpreted languages, eg., Python, Ruby, PHP, Java.
 * Database indexs
 * Caches, eg., Redis, Varnish
 * Sets
 * Unique data representation, eg., Lisp does not store the same string twice, but instead uses a hash. This technique is called **hash consing**.

## Hash maps in Python

Python uses *open addresses* when trying to handle hash collisions. The probe length is defined by a *pseudo-random* process. There is a nice description <a href='http://www.shutupandship.com/2012/02/how-hash-collisions-are-resolved-in.html'>here</a>.

## Hash maps in Java

Java uses *linked lists* for JVMs < 7, but now uses *tree* style storing of items in the linked list, ie., sorted entries in the linked-list, which can speed up look-up times to O(logn) rather than O(n). Nice descriptions can be seen here about <a href="http://javarevisited.blogspot.in/2011/02/how-hashmap-works-in-java.html">Java HashMap</a> and a <a href='http://www.nurkiewicz.com/2014/04/hashmap-performance-improvements-in.html'>performance of Java 7 vs Java 8 (linked list chaining, vs. tree)</a>