# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
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
    assert nodo.data == 3