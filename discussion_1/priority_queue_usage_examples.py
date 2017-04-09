"""
Author: Moshe Lichman

Simple example of how to use the priority queue "library"
"""
from __future__ import division
from priority_dict import priorityDictionary as PQueue


def extract_min(queue):
    """
    Utility function -- returns the key with the min value and removes it from the queue.

    Args
        queue:  <priority queue object> queue to extract min from

    Returns
        key with the smallest value or None if the queue is empty.
    """
    if len(queue) == 0:
        return None

    val = queue.smallest()
    del queue[val]

    return val


def queue_bad_extract_min_example():
    """
    Shows what happens when you don't extract and just call smallest()
    """
    queue = PQueue()
    queue['first'] = 0
    queue['second'] = 1

    # Both print commands will print 'first'
    print queue.smallest()
    print queue.smallest()


def queue_extract_min_example():
    """
    Shows what happens when using the utility function extract_min.
    """
    queue = PQueue()
    queue['first'] = 0
    queue['second'] = 1

    print extract_min(queue)    # prints 'first'
    print extract_min(queue)    # prints 'second'


def queue_change_priority():
    queue = PQueue()
    queue['first'] = 0
    queue['second'] = 1

    print queue.smallest()

    queue['second'] = -1

    print queue.smallest()


if __name__ == '__main__':
    queue_bad_extract_min_example()
    print '---------------'
    queue_extract_min_example()
    print '---------------'
    queue_change_priority()
