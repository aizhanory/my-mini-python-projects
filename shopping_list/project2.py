shopping_list = []

while True:
    print("Здравствуй! Я ваш шоппинг менеджер, чем могу помочь?😊")
    print("1 - добавить покупку")
    print("2 - показать весь список")
    print("3 - удалить товар")
    print("4 - очистить список")
    print("5 - сортировать список")
    print("6 - найти товар")
    print("7 - выйти")

    choice = input("> ").strip()

    if choice == "1":
        new_item = input("Напишите что купили: ").strip()
        shopping_list.append(new_item)
        print(f"Добавлена новая покупка: {new_item.capitalize()}")

    elif choice == "2":
        if len(shopping_list) != 0:
            print("Вот ваш список покупок:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. 🎀{item.capitalize()}")
        else:
            print("Ваш список пуст")

    elif choice == "3":
        if len(shopping_list) != 0:
            item_to_remove = input("Какую вещь хотите удалить? : ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove.capitalize()} удален(а).")
            else:
                print("Такую вещь вы не покупали😅")
        else:
            print("Вы еще ничего не купили, чтобы удалять😅")

    elif choice == "4":
        confirm = input("Ты точно уверена? да/нет : ").strip().lower()
        if confirm == "да":
            shopping_list.clear()
            print("Ваш список очищен.")
        elif confirm == "нет":
            print("Очищение отменено")
        else:
            print("Не поняла, можете написать да/нет.")

    elif choice == "5":
        answer = input("Как отсортировать? а - по алфавиту, н - наоборот: ").strip().lower()
        if answer == "а":
            shopping_list.sort()
            print("Ваш список по алфавиту:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. 🎀{item.capitalize()}")
        elif answer == "н":
            shopping_list.reverse()
            print("Ваш список от последнего к первому:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. 🎀{item.capitalize()}")
        else:
            print("Не поняла, можете написать а/н.")

    elif choice == "6":
        search = input("Что надо найти? : ").strip().lower()
        found = False
        for item in shopping_list:
            if search in item.lower():
                print(f"Нашла: {item.capitalize()}")
                found = True
        if not found:
            print("Не нашла😕")

    elif choice == "7":
        print("Пока!👋🏻")
        break

    else:
        print("Такой команды нет. Попробуйте снова.")
