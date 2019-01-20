import pytest

from src.datasctructures.queue import Queue


def test_empty_is_empty():
    q = Queue()
    assert q.is_empty() == True


def test_empty_str_representation():
    q = Queue()
    assert '[]', str(q)


def test_with_one_item_is_not_empty():
    q = Queue()
    q.enqueue(3)
    assert q.is_empty() == False


def test_one_item_str_representation():
    q = Queue()
    q.enqueue(3)
    assert """[{'item': 3, 'next': None}]""", str(q)


def test_enque_and_dequeue_and_is_empty():
    q = Queue()
    q.enqueue(3)
    q.dequeue()
    assert q.is_empty() == True


def test_queue_and_dequeue():
    q = Queue()
    q.enqueue(3)
    assert q.dequeue() == 3


def test_size_after_2_enqueue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    assert q.size() == 2


def test_peek_after_1_enqueue():
    q = Queue()
    q.enqueue(7)
    assert q.peek() == 7


def test_peek_after_2_enqueue():
    q = Queue()
    q.enqueue(7)
    q.enqueue(11)
    assert q.peek() == 7


def test_queue_and_dequeue():
    q = Queue()
    q.enqueue(3)
    q.enqueue(5)
    assert q.dequeue() == 3
    assert q.dequeue() == 5


def test_exception_when_dequeue_empty_queue():
    with pytest.raises(ValueError):
        q = Queue()
        q.dequeue()


def test_queue_and_dequeue():
    q = Queue()
    q.enqueue(2)
    q.enqueue(5)
    q.enqueue(7)
    assert q.dequeue() == 2
    assert q.dequeue() == 5
    assert q.dequeue() == 7
