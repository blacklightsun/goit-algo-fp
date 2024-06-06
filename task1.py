class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        i = 0
        while current:
            i += 1
            print(f'{i}: {current.data}')
            current = current.next

    def link_reverse_list(self):
        # мій код - варіант вирішення першої підзадачі через зміну вказівників (On**1)
        start_node = self.head
        while start_node.next:
            self.insert_at_beginning(start_node.next.data)
            start_node.next = start_node.next.next

    def buble_sort(self):
        # мій код
        # використовуємо бульбашкове сортування, як найшвидше (On**2)
        # проходимось по списку двома повними циклами
        # не використовуємо сортування вставками та злиттям, бо там потрібні доступи всередину списку по індексу
        # для чого або треба дублювати зв'язаний список у іншій структурі даних (тобто реалізовувати функцію у іншій структурі даних,
        # тоді нахіба зв'язний список взагалі),
        # або робити це через пошук (складність O2**n) для кожного циклу (тобто кожен пошук елемента - цикл проходу по зв'язаному списку)
        ext_cycle_current_node = self.head
        while ext_cycle_current_node.next:
            int_cycle_current_node = self.head
            while int_cycle_current_node.next:
                if int_cycle_current_node.data > int_cycle_current_node.next.data:
                    int_cycle_current_node.data, int_cycle_current_node.next.data = int_cycle_current_node.next.data, int_cycle_current_node.data
                int_cycle_current_node = int_cycle_current_node.next
            ext_cycle_current_node = ext_cycle_current_node.next

    def return_last_node(self):
        # мій код - повертає останню ноду в зв'язному списку
        current = self.head
        while current.next is not None:
            current = current.next
        return current


def stack_reverse_list(llist) -> None:
    # мій код - варіант вирішення першої підзадачі (реверсування) через стек (On**4 з урахуванням циклів у всіх методах, що використовуються)
    stack = []
    current = llist.head
    while current:
        stack.append(current.data)
        llist.delete_node(current.data)
        current = current.next
    while stack:
        llist.insert_at_end(stack.pop())

def sort_sorted_llist(list1 : LinkedList, list2 : LinkedList) -> LinkedList:
# мій код - сортування сортованих списків у один
    result_llist = LinkedList()

    if type(list1) != type(result_llist) or type(list2) != type(result_llist):
        raise TypeError

    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        if current1.data < current2.data:
            result_llist.insert_at_end(current1.data)
            current1 = current1.next
        elif current1.data > current2.data:
            result_llist.insert_at_end(current2.data)
            current2 = current2.next
        else:
            result_llist.insert_at_end(current1.data)
            current1 = current1.next
            result_llist.insert_at_end(current2.data)
            current2 = current2.next

    # коли закінчилися елементи в найкоротшому з вхідних списків - прив'язуємо залишок іншого списку до результуючого
    if current1:
        result_llist.return_last_node().next = current1

    if current2:
        result_llist.return_last_node().next = current2

    return result_llist


# створюємо за'язаний список
llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_beginning(20)
llist.insert_at_beginning(25)

print("Зв'язний список:")
llist.print_list()

print("\nЗв'язний список після реверсування через стек:")
stack_reverse_list(llist)
llist.print_list()

print("\nЗв'язний список після реверсування через зміну посилань:")
llist.link_reverse_list()
llist.print_list()

print("\nЗв'язний список після бульбашкового сортування:")
llist.buble_sort()
llist.print_list()



# створюємо ще один сортований за'язний список
llist2 = LinkedList()
llist2.insert_at_beginning(78)
llist2.insert_at_beginning(45)
llist2.insert_at_beginning(24)
llist2.insert_at_beginning(21)
llist2.insert_at_beginning(13)
llist2.insert_at_beginning(11)
llist2.insert_at_beginning(4)
print("\nЗв'язний список #2 (сортований):")
llist2.print_list()

print('\nРезультат сортування сортованих списків:')
sort_sorted_llist(llist, llist2).print_list()
