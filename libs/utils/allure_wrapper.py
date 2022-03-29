from allure import description as _desc, step as _step


def description(test_description):
    return _desc(test_description)


def step(info):
    return _step(info)




