import unittest

from src.datasctructures.queue import Queue
from src.pe.pe_0001 import solve


class MyTest(unittest.TestCase):

    def test_empty_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_with_one_item_is_not_empty(self):
        q = Queue()
        q.enqueue(3)
        self.assertFalse(q.is_empty())

    def test_with_one_item_is_not_empty(self):
        q = Queue()
        q.enqueue(3)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_queue_and_dequeue(self):
        q = Queue()
        q.enqueue(3)
        self.assertEquals(3, q.dequeue())






