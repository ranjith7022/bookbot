def word_count(text: str) -> int:
    return len(text.split())


def char_count(text: str) -> dict:
    count = {}

    text = text.lower()
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def sort_on(items: list[tuple[str, int]]) -> list[tuple[str, int]]:
    items.sort(reverse=True, key=lambda x: x[1])
    return items
