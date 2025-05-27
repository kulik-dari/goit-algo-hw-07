#!/usr/bin/env python3
"""
Скрипт для запуску всіх завдань домашнього завдання #7
Дерева та балансування
"""

import sys
import time
import traceback

def run_task(task_name, task_function):
    """
    Запускає окреме завдання з обробкою помилок
    
    Args:
        task_name (str): Назва завдання
        task_function (callable): Функція для виконання
    
    Returns:
        bool: True якщо завдання виконано успішно, False інакше
    """
    print(f"\n{'='*70}")
    print(f"🚀 {task_name}")
    print(f"{'='*70}")
    
    try:
        start_time = time.time()
        task_function()
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"\n✅ {task_name} виконано успішно!")
        print(f"⏱️  Час виконання: {execution_time:.3f} секунд")
        return True
        
    except Exception as e:
        print(f"\n❌ Помилка в {task_name}:")
        print(f"   {str(e)}")
        print("\nДетальна інформація про помилку:")
        traceback.print_exc()
        return False

def task1_main():
    """Запуск завдання 1: Пошук найбільшого значення"""
    # Імпортуємо та запускаємо завдання 1
    try:
        import task1
        if hasattr(task1, 'main'):
            task1.main()
        else:
            print("Функція main() не знайдена в task1.py")
            # Якщо main() відсутня, спробуємо виконати базовий код
            exec(open('task1.py').read())
    except ImportError:
        print("❌ Файл task1.py не знайдено")
        raise

def task2_main():
    """Запуск завдання 2: Пошук найменшого значення"""
    try:
        import task2
        if hasattr(task2, 'main'):
            task2.main()
        else:
            print("Функція main() не знайдена в task2.py")
            exec(open('task2.py').read())
    except ImportError:
        print("❌ Файл task2.py не знайдено")
        raise

def task3_main():
    """Запуск завдання 3: Сума всіх значень"""
    try:
        import task3
        if hasattr(task3, 'main'):
            task3.main()
        else:
            print("Функція main() не знайдена в task3.py")
            exec(open('task3.py').read())
    except ImportError:
        print("❌ Файл task3.py не знайдено")
        raise

def task4_main():
    """Запуск завдання 4: Система коментарів"""
    try:
        import task4
        if hasattr(task4, 'main'):
            task4.main()
        else:
            print("Функція main() не знайдена в task4.py")
            exec(open('task4.py').read())
    except ImportError:
        print("❌ Файл task4.py не знайдено")
        print("💡 Завдання 4 є опціональним, пропускаємо...")
        return

def main():
    """Головна функція для запуску всіх завдань"""
    print("🌳 ДОМАШНЄ ЗАВДАННЯ #7: ДЕРЕВА ТА БАЛАНСУВАННЯ")
    print("Виконання всіх завдань")
    print("=" * 70)
    
    # Список завдань для виконання
    tasks = [
        ("ЗАВДАННЯ 1: Пошук найбільшого значення в дереві", task1_main),
        ("ЗАВДАННЯ 2: Пошук найменшого значення в дереві", task2_main),
        ("ЗАВДАННЯ 3: Сума всіх значень у дереві", task3_main),
        ("ЗАВДАННЯ 4: Система коментарів (опціонально)", task4_main)
    ]
    
    results = []
    total_start_time = time.time()
    
    # Виконуємо всі завдання
    for task_name, task_function in tasks:
        success = run_task(task_name, task_function)
        results.append((task_name, success))
        
        # Пауза між завданнями для зручності перегляду
        if success:
            if task_name != tasks[-1][0]:  # Не паузимо після останнього завдання
                try:
                    input("\n⏸️  Натисніть Enter для продовження до наступного завдання...")
                except KeyboardInterrupt:
                    print("\n\n⚠️  Виконання перервано користувачем")
                    break
        else:
            # При помилці питаємо чи продовжувати
            try:
                user_choice = input("\n❓ Продовжити виконання інших завдань? (y/n): ")
                if user_choice.lower() not in ['y', 'yes', 'так', 'т']:
                    break
            except KeyboardInterrupt:
                print("\n\n⚠️  Виконання перервано користувачем")
                break
    
    total_end_time = time.time()
    total_time = total_end_time - total_start_time
    
    # Виводимо підсумки
    print(f"\n{'='*70}")
    print("📊 ПІДСУМКИ ВИКОНАННЯ ДОМАШНЬОГО ЗАВДАННЯ")
    print(f"{'='*70}")
    
    successful_tasks = 0
    for task_name, success in results:
        status = "✅ Успішно" if success else "❌ Помилка"
        print(f"{status} - {task_name}")
        if success:
            successful_tasks += 1
    
    
    # Додаткова інформація
    print(f"\n📋 Додаткова інформація:")
    print("   • Всі файли завдань мають бути в одній директорії")
    print("   • Переконайтеся, що Python 3.7+ встановлено")
    print("   • Для завдання 4 потрібна бібліотека collections (стандартна)")
    
    return successful_tasks == len([t for t in tasks if "опціонально" not in t[0]])

def interactive_mode():
    """Інтерактивний режим вибору завдань"""
    print("🔄 ІНТЕРАКТИВНИЙ РЕЖИМ")
    print("Виберіть завдання для виконання:")
    print("1. Завдання 1: Пошук найбільшого значення")
    print("2. Завдання 2: Пошук найменшого значення") 
    print("3. Завдання 3: Сума всіх значень")
    print("4. Завдання 4: Система коментарів")
    print("5. Виконати всі завдання")
    print("0. Вихід")
    
    tasks_map = {
        '1': ("ЗАВДАННЯ 1", task1_main),
        '2': ("ЗАВДАННЯ 2", task2_main),
        '3': ("ЗАВДАННЯ 3", task3_main),
        '4': ("ЗАВДАННЯ 4", task4_main),
        '5': ("ВСІ ЗАВДАННЯ", main)
    }
    
    while True:
        try:
            choice = input("\nВаш вибір (0-5): ").strip()
            
            if choice == '0':
                print("👋 До побачення!")
                break
            elif choice in tasks_map:
                task_name, task_function = tasks_map[choice]
                if choice == '5':
                    task_function()
                    break
                else:
                    run_task(task_name, task_function)
            else:
                print("❌ Невірний вибір. Спробуйте ще раз.")
                
        except KeyboardInterrupt:
            print("\n\n⚠️  Програма перервана користувачем")
            break
        except EOFError:
            print("\n\n👋 До побачення!")
            break

if __name__ == "__main__":
    print("🌳 Домашнє завдання #7: Дерева та балансування")
    print("=" * 50)
    
    # Перевіряємо аргументи командного рядка
    if len(sys.argv) > 1:
        if sys.argv[1] == "--interactive" or sys.argv[1] == "-i":
            interactive_mode()
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("Використання:")
            print("  python3 all_tasks.py           # Виконати всі завдання")
            print("  python3 all_tasks.py -i        # Інтерактивний режим")
            print("  python3 all_tasks.py --help    # Показати цю довідку")
        else:
            print(f"❌ Невідомий аргумент: {sys.argv[1]}")
            print("Використайте --help для довідки")
    else:
        # Запускаємо всі завдання за замовчуванням
        try:
            success = main()
            sys.exit(0 if success else 1)
        except KeyboardInterrupt:
            print("\n\n⚠️  Виконання перервано користувачем")
            sys.exit(1)
