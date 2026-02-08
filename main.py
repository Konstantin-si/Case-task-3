from worker import Worker
from datetime import datetime


def main():
    workers = []

    try:
        count = int(input("Сколько работников добавить? "))
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Неверное число.")
        return

    for i in range(count):
        print(f"\nРаботник {i + 1}:")
        name = input("ФИО: ").strip() or "Не указано"
        pos = input("Должность: ").strip() or "Не указано"

        try:
            sal = float(input("Зарплата: ") or 0)
        except ValueError:
            sal = 0.0

        try:
            year = int(input("Год поступления: ") or datetime.now().year)
        except ValueError:
            year = datetime.now().year

        workers.append(Worker(name, pos, sal, year))

    try:
        min_exp = int(input("\nВведите минимальный стаж (лет): "))
    except ValueError:
        print("Неверный ввод.")
        return

    current_year = datetime.now().year
    found = False

    print(f"\nРаботники со стажем больше {min_exp} лет:")
    for w in workers:
        if w.get_experience(current_year) > min_exp:
            print(w)
            found = True

    if not found:
        print("Таких работников нет.")


if __name__ == "__main__":
    main()