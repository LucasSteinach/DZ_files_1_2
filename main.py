import os


def lines_counter(file_name: str):
    if file_name == 'result.txt':
        return 'Usage this file is not allowed'
    elif file_name[-3:] == 'txt':
        with open(file_name) as file:
            lines_list = file.readlines()
            return {'file_name': file_name, 'lines_count': len(lines_list), 'content': lines_list}
    else:
        print('Формат файла не .txt')


def sort_by_lines_count(input_element):
    return input_element['lines_count']


def directory_worker():
    files_list = os.listdir(os.getcwd())
    data_list = []

    for file in files_list:
        if file[-3:] == 'txt' and file != 'result.txt':
            data_list += [lines_counter(file)]
        else:
            continue

    # print(data_list)
    # print('-----------------')
    # print(data_list)

    data_list.sort(key=sort_by_lines_count)

    with open('result.txt', 'w', encoding='utf-8') as result:
        for data in data_list:
            result.write(f'Название файла: {data["file_name"]}\nКоличество строк: {data["lines_count"]}\n\n')
            result.writelines(data["content"])
            result.write('\n')
    print('Сборка файла завершена. Результат находится в файле result.txt текущей директории')


directory_worker()
