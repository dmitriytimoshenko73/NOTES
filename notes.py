import json
import datetime


def create_note():
    id = input("Введите идентификатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = str(datetime.datetime.now())

    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    return note


def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")


def read_notes():
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print("ID:", note["id"])
            print("Title:", note["title"])
            print("Body:", note["body"])
            print("Timestamp:", note["timestamp"])
            print()


def edit_note():
    id = input("Введите идентификатор заметки для редактирования: ")

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note["id"] == id:
                note["title"] = input("Введите новый заголовок: ")
                note["body"] = input("Введите новый текст: ")
                note["timestamp"] = str(datetime.datetime.now())
            json.dump(note, file)
            file.write("\n")


def delete_note():
    id = input("Введите идентификатор заметки для удаления: ")

    with open("notes.json", "r") as file:
        lines = file.readlines()

    with open("notes.json", "w") as file:
        for line in lines:
            note = json.loads(line)
            if note["id"] != id:
                json.dump(note, file)
                file.write("\n")


def main():
    while True:
        print("1. Создать заметку")
        print("2. Посмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Заметка сохранена.")
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
            print("Заметка отредактирована.")
        elif choice == "4":
            delete_note()
            print("Заметка удалена.")
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()