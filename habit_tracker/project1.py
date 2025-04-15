habit_list = []

print("Привет! Добро пожаловать в трекер привычек 💛")

while True:
    print("\nЧто хочешь сделать?")
    print("1 — Добавить привычку")
    print("2 — Показать все")
    print("3 — Удалить по названию")
    print("4 — Очистить список")
    print("5 — Отсортировать")
    print("6 — Найти привычку")
    print("7 — Выйти")

    choice = input("> ")

    if choice == "1":
        new_habit = input("Введи новую привычку: ").strip()
        habit_list.append(new_habit)
        print(f"✅ Добавлено: {new_habit.capitalize()}")

    elif choice == "2":
        if habit_list:
            print("\n🌿 Твои привычки:")
            for i, habit in enumerate(habit_list, start=1):
                print(f"{i}. {habit}")
        else:
            print("Список пока пуст.")

    elif choice == "3":
        habit_to_remove = input("Что удалить?").strip()
        if habit_to_remove in habit_list:
            habit_list.remove(habit_to_remove)
            print(f"🗑️ Удалено: {habit_to_remove}")
        else:
            print("Такой привычки нет в списке.")

    elif choice == "4":
        confirm = input("Ты точно хочешь всё удалить? (да/нет): ").lower()
        if confirm == "да":
            habit_list.clear()
            print("🧹 Список очищен.")

    elif choice == "5":
        habit_list.sort()
        print("📚 Привычки отсортированы.")

    elif choice == "6":
        found = False
        search = input("Что ищешь? ").strip().lower()
        for habit in habit_list:
            if search in habit.lower():
                print(f"🔍 Найдено: {habit}")
                found = True
            if not found:
                print("Ничего не найдено.")

    elif choice == "7":
        print("До встречи! 💫")
        break

    else:
        print("Неизвестная команда. Попробуй снова.")
