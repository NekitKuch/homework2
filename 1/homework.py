def total_salary(path):
    try:
        total_salary = 0
        num_developers = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділити рядок на прізвище та заробітну плату за комою
                name, salary_str = line.strip().split(',')
                
                # Конвертувати заробітну плату у ціле число
                salary = int(salary_str)

                # Додати до загальної суми
                total_salary += salary
                num_developers += 1

        # Обчислити середню заробітну плату
        average_salary = total_salary / num_developers if num_developers > 0 else 0

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

total, average = total_salary("1/salary.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
