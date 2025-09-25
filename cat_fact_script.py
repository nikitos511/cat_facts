import requests
from typing import Optional

BASE_URL = "https://catfact.ninja/facts"


def get_first_page(url: str):
    """Получает первую страницу с фактами и возвращает JSON или None при ошибке."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при запросе первой страницы: {e}")
        return None


def get_last_page(url: str, last_page_num: int):
    """Запрашивает последнюю страницу фактов и возвращает JSON или None при ошибке."""
    try:
        response = requests.get(url, params={"page": last_page_num}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при запросе последней страницы: {e}")
        return None


def find_shortest_fact(facts: list[dict]) -> Optional[str]:
    """
    Находит самый короткий факт по полю 'length'.
    Если список пустой или нет ключа 'fact', возвращает None.
    """
    if not facts:
        return None

    try:
        shortest = min(facts, key=lambda f: f.get("length", float("inf")))
        return shortest.get("fact")
    except (ValueError, TypeError):
        return None


def main():
    # 1. Получаем первую страницу
    first_page = get_first_page(BASE_URL)
    if not first_page:
        print("Не удалось получить первую страницу фактов.")
        return

    # 2. Сколько всего фактов
    total = first_page.get("total")
    per_page = first_page.get("per_page")

    if not total or not per_page:
        print("Не удалось определить общее количество фактов или размер страницы.")
        return

    # 3. Последняя страница
    last_page = (total + per_page - 1) // per_page

    # 4. Запрос последней страницы
    last_page_data = get_last_page(BASE_URL, last_page)
    if not last_page_data:
        print("Не удалось получить данные с последней страницы или они пустые.")
        return

    # 5. Самый короткий факт
    shortest_fact = find_shortest_fact(last_page_data.get("data", []))
    if shortest_fact:
        print("Самый короткий факт с последней страницы:")
        print(shortest_fact)
    else:
        print("Факт не найден.")


if __name__ == "__main__":
    main()