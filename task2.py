"""
Завдання 2: Знаходження найменшого значення у двійковому дереві пошуку або AVL-дереві

Реалізація включає:
- Клас Node для представлення вузла дерева
- Клас BinarySearchTree для двійкового дерева пошуку
- Функцію find_min для знаходження найменшого значення
"""

class Node:
    """Клас для представлення вузла дерева"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Клас для двійкового дерева пошуку"""
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Вставка нового значення в дерево"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """Рекурсивна вставка значення"""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
        # Якщо key == node.key, не вставляємо дублікат
    
    def find_min(self):
        """
        Знаходить найменше значення в дереві.
        
        У двійковому дереві пошуку найменше значення завжди знаходиться
        в найлівішому вузлі дерева.
        
        Returns:
            int/float: Найменше значення в дереві або None, якщо дерево порожнє
        """
        if self.root is None:
            return None
        
        current = self.root
        # Йдемо вліво до тих пір, поки не досягнемо найлівішого вузла
        while current.left is not None:
            current = current.left
        
        return current.key
    
    def display_inorder(self):
        """Виводить дерево в порядку зростання (in-order traversal)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Рекурсивний обхід дерева в порядку зростання"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

def find_min_in_bst(root):
    """
    Альтернативна функція для знаходження найменшого значення.
    Приймає корінь дерева як параметр.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Найменше значення в дереві або None, якщо дерево порожнє
    """
    if root is None:
        return None
    
    current = root
    while current.left is not None:
        current = current.left
    
    return current.key

def find_min_recursive(root):
    """
    Рекурсивна версія пошуку найменшого значення.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Найменше значення в дереві або None, якщо дерево порожнє
    """
    if root is None:
        return None
    
    # Якщо немає лівої дитини, поточний вузол має мінімальне значення
    if root.left is None:
        return root.key
    
    # Інакше рекурсивно шукаємо в лівому піддереві
    return find_min_recursive(root.left)

def find_min_max_pair(root):
    """
    Знаходить пару мінімальне-максимальне значення в дереві.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        tuple: (min_value, max_value) або (None, None) для порожнього дерева
    """
    if root is None:
        return None, None
    
    # Знаходимо мінімальне значення (найлівіший вузол)
    min_node = root
    while min_node.left is not None:
        min_node = min_node.left
    
    # Знаходимо максимальне значення (найправіший вузол)
    max_node = root
    while max_node.right is not None:
        max_node = max_node.right
    
    return min_node.key, max_node.key

# Демонстрація роботи
def main():
    """Демонстрація роботи алгоритму пошуку найменшого значення"""
    print("🌳 Завдання 2: Пошук найменшого значення в двійковому дереві пошуку")
    print("=" * 70)
    
    # Створюємо дерево
    bst = BinarySearchTree()
    
    # Додаємо значення
    values = [15, 10, 20, 8, 12, 17, 25, 6, 11, 13, 22, 27]
    print(f"Додаємо значення: {values}")
    
    for value in values:
        bst.insert(value)
    
    # Виводимо дерево
    sorted_values = bst.display_inorder()
    print(f"Дерево (відсортовані значення): {sorted_values}")
    
    # Знаходимо найменше значення різними способами
    print(f"\n🔍 Результати пошуку найменшого значення:")
    
    # Метод класу
    min_value_1 = bst.find_min()
    print(f"   Метод класу: {min_value_1}")
    
    # Функція з параметром root
    min_value_2 = find_min_in_bst(bst.root)
    print(f"   Функція з root: {min_value_2}")
    
    # Рекурсивна функція
    min_value_3 = find_min_recursive(bst.root)
    print(f"   Рекурсивна функція: {min_value_3}")
    
    # Пара мін-макс
    min_val, max_val = find_min_max_pair(bst.root)
    print(f"   Пара мін-макс: ({min_val}, {max_val})")
    
    # Перевірка на порожньому дереві
    empty_bst = BinarySearchTree()
    min_empty = empty_bst.find_min()
    print(f"   Порожнє дерево: {min_empty}")
    
    print(f"\n✅ Найменше значення в дереві: {min_value_1}")
    
    # Додаткові тести
    print(f"\n🧪 Додаткові тести:")
    
    # Тест з одним елементом
    single_bst = BinarySearchTree()
    single_bst.insert(42)
    print(f"   Дерево з одним елементом (42): {single_bst.find_min()}")
    
    # Тест з від'ємними числами
    negative_bst = BinarySearchTree()
    negative_values = [-10, -5, -15, -3, -7, -12, -20]
    for val in negative_values:
        negative_bst.insert(val)
    print(f"   Дерево з від'ємними числами {negative_values}: {negative_bst.find_min()}")
    
    # Тест з дробовими числами
    float_bst = BinarySearchTree()
    float_values = [3.14, 2.71, 1.41, 4.5, 0.5]
    for val in float_values:
        float_bst.insert(val)
    print(f"   Дерево з дробовими числами {float_values}: {float_bst.find_min()}")
    
    # Тест з лінійним деревом (всі вузли зліва)
    left_linear_bst = BinarySearchTree()
    left_values = [10, 9, 8, 7, 6, 5]
    for val in left_values:
        left_linear_bst.insert(val)
    print(f"   Лінійне дерево (ліва сторона) {left_values}: {left_linear_bst.find_min()}")
    
    # Тест з лінійним деревом (всі вузли справа)
    right_linear_bst = BinarySearchTree()
    right_values = [1, 2, 3, 4, 5, 6]
    for val in right_values:
        right_linear_bst.insert(val)
    print(f"   Лінійне дерево (права сторона) {right_values}: {right_linear_bst.find_min()}")

if __name__ == "__main__":
    main()
