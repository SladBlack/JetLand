# По ссылке доступен файл (внутри zip-архива), который содержит список dict-объектов
# (по одному объекту на каждой строке) следующего вида:
#   {«key1»: «value1», «k2»: «v2»},
#   {«k1»: «v1», «k2»: «v2», «k3»: «v3»},
#   {},
#   {},
#   {«k2»: «v2», «key1»: «value1»},
#   {«key1»: «value1»},
#   {«key2»: «value2»}.
#
# Необходимо удалить все дубликаты из этого файла. Для примера выше после удаления дубликатов должны остаться  объекты
#   {«key1»: «value1», «k2»: «v2»},
#   {«key1»: «value1»},
#   {«k1»: «v1», «k2»: «v2», «k3»: «v3»},
#   {},
#   {«key2»: «value2»}.
#
# Обратите внимание, что объекты считаются дубликатами, если они равны в Python. Например,
#   {«key1»: «value1», «k2»: «v2»} и {«k2»: «v2», «key1»: «value1»} — это дубликаты.
import json


def get_duplicate_count(file_name: str) -> int:
    """
    Get duplicate lines count
    :param file_name: str
    :return: int
    """
    unique_lines = set()
    deletion_counter = 0
    total_counter = 0
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break

            total_counter += 1
            item = json.dumps(dict(sorted(json.loads(line).items())))
            if item not in unique_lines:
                unique_lines.add(item)
                continue

            deletion_counter += 1

    return total_counter - deletion_counter


if __name__ == '__main__':
    print(get_duplicate_count(file_name='dicts.json'))
