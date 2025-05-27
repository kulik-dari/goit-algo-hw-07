"""
Завдання 1: Знаходження найбільшого значення у двійковому дереві пошуку або AVL-дереві

Реалізація включає:
- Клас Node для представлення вузла дерева
- Клас BinarySearchTree для двійкового дерева пошуку
- Функцію find_max для знаходження найбільшого значення
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
    
    def find_max(self):
        """
        Знаходить найбільше значення в дереві.
        
        У двійковому дереві пошуку найбільше значення завжди знаходиться
        в найправішому вузлі дерева.
        
        Returns:
            int/float: Найбільше значення в дереві або None, якщо дерево порожнє
        """
        if self.root is None:
            return None
        
        current = self.root
        # Йдемо вправо до тих пір, поки не досягнемо найправішого вузла
        while current.right is not None:
            current = current.right
        
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

def find_max_in_bst(root):
    """
    Альтернативна функція для знаходження найбільшого значення.
    Приймає корінь дерева як параметр.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Найбільше значення в дереві або None, якщо дерево порожнє
    """
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
    
    return current.key

def find_max_recursive(root):
    """
    Рекурсивна версія пошуку найбільшого значення.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Найбільше значення в дереві або None, якщо дерево порожнє
    """
    if root is None:
        return None
    
    # Якщо немає правої дитини, поточний вузол має максимальне значення
    if root.right is None:
        return root.key
    
    # Інакше рекурсивно шукаємо в правому піддереві
    return find_max_recursive(root.right)

# Демонстрація роботи
def main():
    """Демонстрація роботи алгоритму пошуку найбільшого значення"""
    print("🌳 Завдання 1: Пошук найбільшого значення в двійковому дереві пошуку")
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
    
    # Знаходимо найбільше значення різними способами
    print(f"\n🔍 Результати пошуку найбільшого значення:")
    
    # Метод класу
    max_value_1 = bst.find_max()
    print(f"   Метод класу: {max_value_1}")
    
    # Функція з параметром root
    max_value_2 = find_max_in_bst(bst.root)
    print(f"   Функція з root: {max_value_2}")
    
    # Рекурсивна функція
    max_value_3 = find_max_recursive(bst.root)
    print(f"   Рекурсивна функція: {max_value_3}")
    
    # Перевірка на порожньому дереві
    empty_bst = BinarySearchTree()
    max_empty = empty_bst.find_max()
    print(f"   Порожнє дерево: {max_empty}")
    
    print(f"\n✅ Найбільше значення в дереві: {max_value_1}")
    
    # Додаткові тести
    print(f"\n🧪 Додаткові тести:")
    
    # Тест з одним елементом
    single_bst = BinarySearchTree()
    single_bst.insert(42)
    print(f"   Дерево з одним елементом (42): {single_bst.find_max()}")
    
    # Тест з від'ємними числами
    negative_bst = BinarySearchTree()
    negative_values = [-10, -5, -15, -3, -7, -12, -20]
    for val in negative_values:
        negative_bst.insert(val)
    print(f"   Дерево з від'ємними числами {negative_values}: {negative_bst.find_max()}")
    
    # Тест з дробовими числами
    float_bst = BinarySearchTree()
    float_values = [3.14, 2.71, 1.41, 4.5, 0.5]
    for val in float_values:
        float_bst.insert(val)
    print(f"   Дерево з дробовими числами {float_values}: {float_bst.find_max()}")

if __name__ == "__main__":
    main()
