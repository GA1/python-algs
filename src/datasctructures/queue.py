class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def __str__(self):
        nodes = []
        curr = self.first
        while curr:
            nodes.append(curr)
            curr = curr['next']
        return str(nodes)

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n

    def peek(self):
        if self.is_empty():
            raise ValueError('Queue: peek() on empty queue')
        return self.first['item']

    def enqueue(self, item):
        old_last = self.last
        new_node = {
            'item': item,
            'next': None
        }
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            old_last['next'] = new_node
            self.last = new_node
        self.n = self.n + 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue: dequeue() on empty queue')
        item = self.first['item']
        self.first = self.first['next']
        self.n = self.n - 1
        if self.is_empty():
            self.last = None
        return item

