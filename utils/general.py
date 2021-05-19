def get_choice_value(key: int, choices: list):
    for choice in choices:
        if isinstance(choice, tuple) and choice[0] == key and len(choice) == 2:
            return choice[1]
    return 'none'