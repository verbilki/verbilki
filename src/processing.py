def filter_by_state(data: list, state: str = 'EXECUTED') -> list:
  """
  Функция фильтрует список словарей data по состоянию state.
  """
  return [item for item in data if item['state'] == state]

def sort_by_date(data: list, sort_order: bool = True) -> list:
  """
  Функция сортирует список словарей data по атрибуту dqte (по убыванию, если bool == True; по возрастанию, если bool == False).
  """
  return sorted(data, key=lambda item: item['date'], reverse=sort_order)