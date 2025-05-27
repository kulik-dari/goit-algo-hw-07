"""
Завдання 4: Реалізація системи коментарів з ієрархічною структурою

Система дозволяє:
- Створювати коментарі з відповідями
- Додавати відповіді до коментарів (нескінченна вкладеність)
- Видаляти коментарі (залишаючи відповіді)
- Виводити ієрархічну структуру коментарів
"""

class Comment:
    """
    Клас для представлення коментаря в ієрархічній системі коментарів.
    
    Attributes:
        text (str): Текст коментаря
        author (str): Автор коментаря
        replies (list): Список відповідей на коментар
        is_deleted (bool): Прапорець, що вказує чи був коментар видалений
    """
    
    def __init__(self, text, author):
        """
        Ініціалізує новий коментар.
        
        Args:
            text (str): Текст коментаря
            author (str): Автор коментаря
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    
    def add_reply(self, reply):
        """
        Додає відповідь до коментаря.
        
        Args:
            reply (Comment): Об'єкт коментаря-відповіді
        """
        if not isinstance(reply, Comment):
            raise TypeError("Відповідь має бути об'єктом класу Comment")
        
        self.replies.append(reply)
    
    def remove_reply(self):
        """
        Видаляє коментар, замінюючи його текст на стандартне повідомлення
        та встановлюючи прапорець is_deleted в True.
        
        Відповіді залишаються незмінними.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
    
    def display(self, indent=0):
        """
        Рекурсивно виводить коментар та всі його відповіді
        з відступами для відображення ієрархічної структури.
        
        Args:
            indent (int): Рівень відступу (кількість пробілів)
        """
        # Створюємо відступ
        spacing = "    " * indent
        
        # Виводимо поточний коментар
        if self.is_deleted:
            print(f"{spacing}{self.text}")
        else:
            print(f"{spacing}{self.author}: {self.text}")
        
        # Рекурсивно виводимо всі відповіді
        for reply in self.replies:
            reply.display(indent + 1)
    
    def count_replies(self):
        """
        Підраховує загальну кількість відповідей (включно з вкладеними).
        
        Returns:
            int: Загальна кількість відповідей
        """
        total = len(self.replies)
        for reply in self.replies:
            total += reply.count_replies()
        return total
    
    def get_all_authors(self):
        """
        Повертає множину всіх унікальних авторів у цьому коментарі та відповідях.
        
        Returns:
            set: Множина імен авторів
        """
        authors = set()
        
        # Додаємо автора поточного коментаря, якщо він не видалений
        if not self.is_deleted:
            authors.add(self.author)
        
        # Рекурсивно збираємо авторів з відповідей
        for reply in self.replies:
            authors.update(reply.get_all_authors())
        
        return authors
    
    def find_replies_by_author(self, author):
        """
        Знаходить всі коментарі певного автора.
        
        Args:
            author (str): Ім'я автора для пошуку
            
        Returns:
            list: Список коментарів цього автора
        """
        found_comments = []
        
        # Перевіряємо поточний коментар
        if not self.is_deleted and self.author == author:
            found_comments.append(self)
        
        # Рекурсивно шукаємо у відповідях
        for reply in self.replies:
            found_comments.extend(reply.find_replies_by_author(author))
        
        return found_comments
    
    def get_max_depth(self):
        """
        Повертає максимальну глибину вкладеності відповідей.
        
        Returns:
            int: Максимальна глибина
        """
        if not self.replies:
            return 1
        
        max_reply_depth = max(reply.get_max_depth() for reply in self.replies)
        return 1 + max_reply_depth
    
    def to_dict(self):
        """
        Конвертує коментар та всі відповіді в словник для серіалізації.
        
        Returns:
            dict: Представлення коментаря у вигляді словника
        """
        return {
            'text': self.text,
            'author': self.author,
            'is_deleted': self.is_deleted,
            'replies': [reply.to_dict() for reply in self.replies]
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Створює коментар з словника.
        
        Args:
            data (dict): Дані коментаря
            
        Returns:
            Comment: Відновлений об'єкт коментаря
        """
        comment = cls(data['text'], data['author'])
        comment.is_deleted = data.get('is_deleted', False)
        
        for reply_data in data.get('replies', []):
            reply = cls.from_dict(reply_data)
            comment.add_reply(reply)
        
        return comment


def create_sample_discussion():
    """Створює приклад обговорення для демонстрації"""
    # Створюємо кореневий коментар
    root_comment = Comment("Яка чудова книга!", "Бодя")
    
    # Створюємо відповіді першого рівня
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    
    # Додаємо відповіді до кореневого коментаря
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    
    # Створюємо відповідь до reply1
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)
    
    # Видаляємо reply1
    reply1.remove_reply()
    
    return root_comment


def create_complex_discussion():
    """Створює складніше обговорення для демонстрації можливостей"""
    root = Comment("Хто дивився новий фільм?", "Олексій")
    
    # Перша гілка обговорення
    reply1 = Comment("Дивився вчора, просто супер!", "Марія")
    reply1_1 = Comment("А що саме сподобалося?", "Дмитро")
    reply1_1_1 = Comment("Сюжет і акторська гра на висоті", "Марія")
    reply1_1_2 = Comment("Погоджуюся, особливо головний актор", "Анна")
    
    reply1.add_reply(reply1_1)
    reply1_1.add_reply(reply1_1_1)
    reply1_1.add_reply(reply1_1_2)
    
    # Друга гілка обговорення
    reply2 = Comment("Мені не сподобався, занадто довгий", "Петро")
    reply2_1 = Comment("Та ні, нормальна тривалість", "Ігор")
    reply2_1_1 = Comment("Для такого жанру - так", "Петро")
    
    reply2.add_reply(reply2_1)
    reply2_1.add_reply(reply2_1_1)
    
    # Третя гілка
    reply3 = Comment("Де можна подивитися?", "Світлана")
    reply3_1 = Comment("У кінотеатрах ще йде", "Володимир")
    reply3_2 = Comment("І онлайн вже є", "Тетяна")
    
    reply3.add_reply(reply3_1)
    reply3.add_reply(reply3_2)
    
    # Додаємо всі відповіді до кореня
    root.add_reply(reply1)
    root.add_reply(reply2)
    root.add_reply(reply3)
    
    return root


def main():
    """Демонстрація роботи системи коментарів"""
    print("💬 Завдання 4: Система коментарів з ієрархічною структурою")
    print("=" * 70)
    
    # Створюємо приклад з умови завдання
    print("📝 Приклад з умови завдання:")
    print("-" * 40)
    
    root_comment = create_sample_discussion()
    root_comment.display()
    
    # Статистика базового прикладу
    print(f"\n📊 Статистика обговорення:")
    print(f"   Загальна кількість відповідей: {root_comment.count_replies()}")
    print(f"   Максимальна глибина: {root_comment.get_max_depth()}")
    print(f"   Унікальні автори: {', '.join(sorted(root_comment.get_all_authors()))}")
    
    # Складніший приклад
    print(f"\n" + "=" * 70)
    print("🗣️  Складніший приклад обговорення:")
    print("-" * 40)
    
    complex_discussion = create_complex_discussion()
    complex_discussion.display()
    
    # Статистика складного прикладу
    print(f"\n📊 Статистика складного обговорення:")
    print(f"   Загальна кількість відповідей: {complex_discussion.count_replies()}")
    print(f"   Максимальна глибина: {complex_discussion.get_max_depth()}")
    authors = complex_discussion.get_all_authors()
    print(f"   Унікальні автори ({len(authors)}): {', '.join(sorted(authors))}")
    
    # Демонстрація пошуку
    print(f"\n🔍 Пошук коментарів:")
    maria_comments = complex_discussion.find_replies_by_author("Марія")
    print(f"   Коментарі від Марії ({len(maria_comments)}):")
    for i, comment in enumerate(maria_comments, 1):
        print(f"     {i}. \"{comment.text}\"")
    
    petro_comments = complex_discussion.find_replies_by_author("Петро")
    print(f"   Коментарі від Петра ({len(petro_comments)}):")
    for i, comment in enumerate(petro_comments, 1):
        print(f"     {i}. \"{comment.text}\"")
    
    # Демонстрація видалення
    print(f"\n🗑️  Демонстрація видалення коментарів:")
    print("Видаляємо коментар Петра...")
    
    # Знаходимо і видаляємо перший коментар Петра
    if petro_comments:
        petro_comments[0].remove_reply()
    
    print("Структура після видалення:")
    complex_discussion.display()
    
    # Демонстрація серіалізації
    print(f"\n💾 Демонстрація серіалізації:")
    discussion_dict = complex_discussion.to_dict()
    print("Обговорення конвертовано в словник (показуємо перші рівні):")
    
    # Показуємо структуру словника
    print(f"Корінь: {discussion_dict['author']}: \"{discussion_dict['text']}\"")
    print(f"Кількість відповідей: {len(discussion_dict['replies'])}")
    
    # Відновлення з словника
    restored_discussion = Comment.from_dict(discussion_dict)
    print("\nВідновлене обговорення:")
    restored_discussion.display()
    
    print(f"\n✅ Система коментарів працює коректно!")
    print("Реалізовано всі вимоги:")
    print("• Клас Comment з текстом, автором та списком відповідей")
    print("• Метод add_reply для додавання відповідей")
    print("• Метод remove_reply для видалення коментарів")
    print("• Метод display для рекурсивного виводу з відступами")
    print("• Додаткові функції для аналізу та роботи з обговореннями")


if __name__ == "__main__":
    main()
