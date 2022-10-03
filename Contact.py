class Contact:

    field_columns = [
        'name',
        'last_name',
        'email',
        'phone'
    ]

    def __init__(self, name: str, last_name: str, email: str, phone: str):
        self._name = name
        self._last_name = last_name
        self._email = email
        self._phone = phone

