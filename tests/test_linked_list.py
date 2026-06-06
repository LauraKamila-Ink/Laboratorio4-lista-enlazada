# tests/test_linked_list.py
import pytest
from src.linked_list import LinkedList, Node

# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                            #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"

def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0

def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"

def test_append_un_elemento():
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.data == 10
    assert len(ll) == 1

def test_append_varios_elementos():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert str(ll) == "1 -> 2 -> 3"
    assert len(ll) == 3

def test_append_orden_preservado():
    ll = LinkedList()
    for v in [5, 10, 15]:
        ll.append(v)
    current = ll.head
    for expected in [5, 10, 15]:
        assert current.data == expected
        current = current.next

# ------------------------------------------------------------------ #
# Pruebas Equipo C — search                                          #
# ------------------------------------------------------------------ #

def test_search_elemento_existente():
    ll = LinkedList()

    n1 = Node(10)
    n2 = Node(20)

    ll.head = n1
    n1.next = n2

    nodo = ll.search(10)

    assert nodo is not None
    assert nodo.data == 10


def test_search_elemento_inexistente():
    ll = LinkedList()

    ll.head = Node(5)

    assert ll.search(99) is None


def test_search_lista_vacia():
    ll = LinkedList()

    assert ll.search(1) is None


def test_search_ultimo_elemento():
    ll = LinkedList()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    ll.head = n1
    n1.next = n2
    n2.next = n3

    nodo = ll.search(3)

    assert nodo is not None
    assert nodo.data == 3
    

# ------------------------------------------------------------------ #
# Pruebas Equipo B — delete                                           #
# ------------------------------------------------------------------ #

def test_delete_elemento_existente():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    resultado = ll.delete(2)
    assert resultado is True
    assert str(ll) == "1 -> 3"

def test_delete_head():
    ll = LinkedList()
    ll.head = Node(10)
    ll.head.next = Node(20)
    ll.delete(10)
    assert ll.head.data == 20


def test_delete_elemento_inexistente():
    ll = LinkedList()
    ll.head = Node(5)
    
    resultado = ll.delete(99)
    assert resultado is False
    assert len(ll) == 1


def test_delete_lista_vacia():
    ll = LinkedList()
    assert ll.delete(1) is False

