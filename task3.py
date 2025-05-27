"""
Завдання 3: Знаходження суми всіх значень у двійковому дереві пошуку або AVL-дереві

Реалізація включає:
- Клас Node для представлення вузла дерева
- Клас BinarySearchTree для двійкового дерева пошуку
- Функцію sum_values для знаходження суми всіх значень
- Різні варіанти обходу дерева для обчислення суми
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
    
    def sum_values(self):
        """
        Знаходить суму всіх значень в дереві.
        
        Returns:
            int/float: Сума всіх значень в дереві або 0, якщо дерево порожнє
        """
        return self._sum_recursive(self.root)
    
    def _sum_recursive(self, node):
        """
        Рекурсивна функція для обчислення суми всіх значень.
        
        Args:
            node (Node): Поточний вузол
            
        Returns:
            int/float: Сума значень у піддереві з коренем у node
        """
        if node is None:
            return 0
        
        # Сума = значення поточного вузла + сума лівого піддерева + сума правого піддерева
        return node.key + self._sum_recursive(node.left) + self._sum_recursive(node.right)
    
    def count_nodes(self):
        """Підраховує кількість вузлів у дереві"""
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        """Рекурсивна функція для підрахунку вузлів"""
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    def average_value(self):
        """Обчислює середнє арифметичне значення всіх вузлів"""
        total_sum = self.sum_values()
        node_count = self.count_nodes()
        
        if node_count == 0:
            return 0
        
        return total_sum / node_count
    
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

def sum_tree_iterative(root):
    """
    Ітеративна версія підрахунку суми за допомогою стека.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Сума всіх значень в дереві
    """
    if root is None:
        return 0
    
    stack = [root]
    total_sum = 0
    
    while stack:
        current = stack.pop()
        total_sum += current.key
        
        # Додаємо дітей до стека
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return total_sum

def sum_tree_level_order(root):
    """
    Підрахунок суми за допомогою обходу в ширину (level-order).
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        int/float: Сума всіх значень в дереві
    """
    if root is None:
        return 0
    
    from collections import deque
    queue = deque([root])
    total_sum = 0
    
    while queue:
        current = queue.popleft()
        total_sum += current.key
        
        # Додаємо дітей до черги
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return total_sum

def tree_statistics(root):
    """
    Обчислює різноманітні статистики дерева.
    
    Args:
        root (Node): Корінь дерева
        
    Returns:
        dict: Словник зі статистиками
    """
    if root is None:
        return {
            'sum': 0,
            'count': 0,
            'average': 0,
            'min': None,
            'max': None
        }
    
    # Збираємо всі значення для статистичного аналізу
    values = []
    stack = [root]
    
    while stack:
        current = stack.pop()
        values.append(current.key)
        
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return {
        'sum': sum(values),
        'count': len(values),
        'average': sum(values) / len(values),
        'min': min(values),
        'max': max(values)
    }

# Демонстрація роботи
def main():
    """Демонстрація роботи алгоритму підрахунку суми всіх значень"""
    print("🌳 Завдання 3: Сума всіх значень у двійковому дереві пошуку")
    print("=" * 70)
    
    # Створюємо дерево
    bst = BinarySearchTree()
    
    # Додаємо значення
    values = [15, 10, 20, 8, 12, 17, 25, 6, 11, 13, 22, 27]
    print(f"Додаємо значення: {values}")
    print(f"Очікувана сума (перевірка): {sum(values)}")
    
    for value in values:
        bst.insert(value)
    
    # Виводимо дерево
    sorted_values = bst.display_inorder()
    print(f"Дерево (відсортовані значення): {sorted_values}")
    
    # Обчислюємо суму різними способами
    print(f"\n🔍 Результати обчислення суми:")
    
    # Рекурсивний метод класу
    sum_recursive = bst.sum_values()
    print(f"   Рекурсивний метод: {sum_recursive}")
    
    # Ітеративний підхід
    sum_iterative = sum_tree_iterative(bst.root)
    print(f"   Ітеративний метод: {sum_iterative}")
    
    # Обхід у ширину
    sum_level_order = sum_tree_level_order(bst.root)
    print(f"   Обхід у ширину: {sum_level_order}")
    
    # Додаткова статистика
    node_count = bst.count_nodes()
    average = bst.average_value()
    
    print(f"\n📊 Статистика дерева:")
    print(f"   Кількість вузлів: {node_count}")
    print(f"   Сума всіх значень: {sum_recursive}")
    print(f"   Середнє значення: {average:.2f}")
    
    # Комплексна статистика
    stats = tree_statistics(bst.root)
    print(f"\n📈 Детальна статистика:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"   {key.capitalize()}: {value:.2f}")
        else:
            print(f"   {key.capitalize()}: {value}")
    
    # Тести на особливих випадках
    print(f"\n🧪 Тести на особливих випадках:")
    
    # Порожнє дерево
    empty_bst = BinarySearchTree()
    print(f"   Порожнє дерево: {empty_bst.sum_values()}")
    
    # Дерево з одним елементом
    single_bst = BinarySearchTree()
    single_bst.insert(42)
    print(f"   Дерево з одним елементом (42): {single_bst.sum_values()}")
    
    # Дерево з від'ємними числами
    negative_bst = BinarySearchTree()
    negative_values = [-10, -5, -15, -3, -7]
    for val in negative_values:
        negative_bst.insert(val)
    expected_negative_sum = sum(negative_values)
    actual_negative_sum = negative_bst.sum_values()
    print(f"   Від'ємні числа {negative_values}: {actual_negative_sum} (очікувано: {expected_negative_sum})")
    
    # Дерево з дробовими числами
    float_bst = BinarySearchTree()
    float_values = [3.14, 2.71, 1.41, 4.5, 0.5]
    for val in float_values:
        float_bst.insert(val)
    expected_float_sum = sum(float_values)
    actual_float_sum = float_bst.sum_values()
    print(f"   Дробові числа {float_values}: {actual_float_sum:.2f} (очікувано: {expected_float_sum:.2f})")
    
    # Дерево з нулями
    zero_bst = BinarySearchTree()
    zero_values = [0, 5, -5, 3, -3]
    for val in zero_values:
        zero_bst.insert(val)
    expected_zero_sum = sum(zero_values)
    actual_zero_sum = zero_bst.sum_values()
    print(f"   Числа з нулем {zero_values}: {actual_zero_sum} (очікувано: {expected_zero_sum})")
    
    print(f"\n✅ Основна сума всіх значень у дереві: {sum_recursive}")

if __name__ == "__main__":
    main()
