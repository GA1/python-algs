import unittest

from src.datasctructures.queue import Queue


class MyTest(unittest.TestCase):

    def test_empty_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_empty_str_representation(self):
        q = Queue()
        self.assertEqual('[]', str(q))

    def test_with_one_item_is_not_empty(self):
        q = Queue()
        q.enqueue(3)
        self.assertFalse(q.is_empty())

    def test_one_item_str_representation(self):
        q = Queue()
        q.enqueue(3)
        self.assertEqual("""[{'item': 3, 'next': None}]""", str(q))

    def test_enque_and_dequeue_and_is_empty(self):
        q = Queue()
        q.enqueue(3)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_queue_and_dequeue(self):
        q = Queue()
        q.enqueue(3)
        self.assertEqual(3, q.dequeue())

    def test_size_after_2_enqueue(self):
        q = Queue()
        q.enqueue(3)
        q.enqueue(5)
        self.assertEqual(2, q.size())

    def test_peek_after_1_enqueue(self):
        q = Queue()
        q.enqueue(7)
        self.assertEqual(7, q.peek())

    def test_peek_after_2_enqueue(self):
        q = Queue()
        q.enqueue(7)
        q.enqueue(11)
        self.assertEqual(7, q.peek())

    def test_queue_and_dequeue(self):
        q = Queue()
        q.enqueue(3)
        q.enqueue(5)
        self.assertEqual(3, q.dequeue())
        self.assertEqual(5, q.dequeue())

    def test_exception_when_dequeue_empty_queue(self):
        q = Queue()
        self.assertRaises(ValueError, q.dequeue)

    def test_queue_and_dequeue(self):
        q = Queue()
        q.enqueue(2)
        q.enqueue(5)
        q.enqueue(7)
        self.assertEqual(2, q.dequeue())
        self.assertEqual(5, q.dequeue())
        self.assertEqual(7, q.dequeue())
