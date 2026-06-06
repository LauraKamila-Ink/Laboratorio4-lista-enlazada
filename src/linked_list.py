# src/linked_list.py

class Node:
    """Nodo de la lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Lista enlazada simple."""
    def __init__(self):
        self.head = None

    def __str__(self):
        """Retorna una representación legible de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Lista vacía"

    def __len__(self):
        """Retorna el número de nodos."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def delete(self, data):
        """Elimina la primera ocurrencia de un nodo con el valor dado."""
        if self.head is None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
            
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
            
        return False

    def search(self, data):
        """Busca un valor en la lista.

        Args:
            data: El valor a buscar.

        Returns:
            El nodo que contiene data, o None si no existe.
        """
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None
  
    
    


