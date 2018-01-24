import unittest


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.begin = None
        self.end = None
        self.size = 0

    # tail insertion
    def add_node(self, node):
        if not self.begin:
            self.begin = node
            self.end = node
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node

    def rm_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.begin = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.end = node.prev

    def print_list(self):
        iter = self.begin
        result = []
        while iter != None:
            result.append('{}-{}'.format(iter.key, iter.value))
            iter = iter.next
        print(', '.join(result))


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.list = LinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.cache:
            return -1
        node = self.cache[key]
        self.list.rm_node(node)
        self.list.add_node(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.list.rm_node(node)
            self.list.add_node(node)
        elif self.size < self.capacity:
            self.size += 1
            node = Node(key, value)
            self.cache[key] = node
            self.list.add_node(node)
        else:
            begin_node = self.list.begin
            self.list.rm_node(begin_node)
            del self.cache[begin_node.key]

            node = Node(key, value)
            self.cache[key] = node
            self.list.add_node(node)


class TestSolution(unittest.TestCase):

    def test_link_list(self):
        li = LinkedList()
        n1 = Node(1, 1)
        n2 = Node(2, 2)
        n3 = Node(3, 3)

        li.add_node(n1)
        li.add_node(n2)
        li.add_node(n3)
        self.assertEqual(li.end.value, 3)

        li.rm_node(n3)
        self.assertEqual(li.end.value, 2)

    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put(1, 1);
        cache.put(2, 2);
        v = cache.get(1);       # returns 1
        self.assertEqual(v, 1)
        cache.put(3, 3);        # evicts key 2
        v = cache.get(2);       # returns -1 (not found)
        self.assertEqual(v, -1)
        cache.put(4, 4);        # evicts key 1
        v = cache.get(1);       # returns -1 (not found)
        self.assertEqual(v, -1)
        v = cache.get(3);       # returns 3
        self.assertEqual(v, 3)
        v = cache.get(4);       # returns 4
        self.assertEqual(v, 4)

    def test_lru_cache_2(self):
        operations = [[2],[2,1],[2,2],[2],[1,1],[4,1]]
        cache = LRUCache(operations[0][0])
        for op in operations[1:]:
            if len(op) == 2:
                cache.put(op[0], op[1])
            else:
                cache.get(op[0])

    def test_lru_cache_3(self):
        operations = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        cache = LRUCache(operations[0][0])
        for op in operations[1:]:
            if len(op) == 2:
                print('put', op[0], op[1])
                cache.put(op[0], op[1])
            else:
                print('get', op[0])
                cache.get(op[0])
            cache.list.print_list()

