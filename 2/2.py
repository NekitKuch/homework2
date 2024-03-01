def get_cats_info(path):
    cats_info_list = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # розділити рядок на ідентифікатор, ім'я та вік кота
                cat_data = line.strip().split(',')
                
                # створити словник із інформацією про кота та додати його до списку
                cat_info = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats_info_list.append(cat_info)

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

    return cats_info_list

cats_info = get_cats_info("2/cats.txt")

if cats_info:
    print(cats_info)
