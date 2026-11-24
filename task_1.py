from typing import TypedDict, NotRequired


class User(TypedDict):
    name: str
    age: NotRequired[int | None]
    email: NotRequired[str | None]


def filter_adult_names(users: list[User]) -> list[str]:
    return [
        user['name'] for user in users
        if (user.get('age') or 0) >= 18
        and user.get('email')
    ]


if __name__ == '__main__':
    users: list[User] = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 30, "email": "charlie@example.com"},
        {"name": "David", "email": "david@example.com"},
    ]
    assert filter_adult_names(users) == ['Alice', 'Charlie']
