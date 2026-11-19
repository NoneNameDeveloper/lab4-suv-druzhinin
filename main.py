"""Небольшое приложение для практикума по Git."""


def get_greeting(name: str) -> str:
    return f"Привет, {name}!"


if __name__ == "__main__":
    print(get_greeting("Git"))
