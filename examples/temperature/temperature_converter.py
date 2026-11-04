"""温度转换纯函数模块（仅使用标准库）。"""


def celsius_to_fahrenheit(celsius):
    """将摄氏度转换为华氏度。

    F = C * 9/5 + 32

    :param celsius: 摄氏温度（数字类型）
    :return: float 华氏温度
    :raises TypeError: 当输入不是数字（如 str 或 None）时
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("celsius 必须是数字 (int 或 float)")
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """将华氏度转换为摄氏度。

    C = (F - 32) * 5/9

    :param fahrenheit: 华氏温度（数字类型）
    :return: float 摄氏温度
    :raises TypeError: 当输入不是数字（如 str 或 None）时
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("fahrenheit 必须是数字 (int 或 float)")
    return (fahrenheit - 32) * 5 / 9
