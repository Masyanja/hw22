# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    pass


def _read(csv):
    return [x.split(';') for x in csv.split('\n')]


def _sort(split_csv):
    return sorted(split_csv, key=lambda x: int(x[1]))

def _filter(sorted_csv):
    return [x for x in sorted_csv if int(x[1]) > 10]

split_csv = _read(csv)
sorted_csv = _sort(split_csv)
filter_csv = _filter(sorted_csv)

print(_filter(_sort(_read(csv))))


#     # Фильтрация
#     result_data = []
#     for person in _new_data:
#         if person['age'] < 10:
#             continue
#         else:
#             result_data.append(person)
#     return result_data
#
#
# if __name__ == '__main__':
#     print(get_users_list())
