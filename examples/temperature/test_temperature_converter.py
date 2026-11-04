"""temperature_converter 模块的单元测试（标准库 unittest）。"""

import unittest

from temperature_converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_basic_points(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0, places=7)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0, places=7)
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0, places=7)

    def test_additional_values(self):
        # 室温约 20°C -> 68°F
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68.0, places=7)
        # 37°C（体温） -> 98.6°F
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=7)
        # 负数 -10°C -> 14°F（低于冰点，保留）
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0, places=7)
        # 正小数 25.5°C -> 77.9°F
        self.assertAlmostEqual(celsius_to_fahrenheit(25.5), 77.9, places=7)
        # 高于沸点：150°C -> 302°F
        self.assertAlmostEqual(celsius_to_fahrenheit(150), 302.0, places=7)
        # 高于沸点：200°C -> 392°F
        self.assertAlmostEqual(celsius_to_fahrenheit(200), 392.0, places=7)
        # 返回类型应为 float
        self.assertIsInstance(celsius_to_fahrenheit(0), float)


class TestFahrenheitToCelsius(unittest.TestCase):
    def test_basic_points(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0, places=7)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0, places=7)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0, places=7)

    def test_additional_values(self):
        # 室温 68°F -> 20°C
        self.assertAlmostEqual(fahrenheit_to_celsius(68), 20.0, places=7)
        # 98.6°F（体温） -> 37°C
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=7)
        # 负数 14°F -> -10°C（低于冰点，保留）
        self.assertAlmostEqual(fahrenheit_to_celsius(14), -10.0, places=7)
        # 正小数 77.9°F -> 25.5°C
        self.assertAlmostEqual(fahrenheit_to_celsius(77.9), 25.5, places=7)
        # 高于沸点：300°F -> 148.888...°C（精确值 148 + 8/9）
        self.assertAlmostEqual(fahrenheit_to_celsius(300), 148.0 + 8 / 9, places=7)
        # 高于沸点：250°F -> 121.111...°C（精确值 121 + 1/9）
        self.assertAlmostEqual(fahrenheit_to_celsius(250), 121.0 + 1 / 9, places=7)
        # 返回类型应为 float
        self.assertIsInstance(fahrenheit_to_celsius(32), float)


class TestRoundTrip(unittest.TestCase):
    def test_round_trip_zero(self):
        self.assertAlmostEqual(
            fahrenheit_to_celsius(celsius_to_fahrenheit(0)), 0, places=7
        )

    def test_round_trip_positive(self):
        for c in (1, 25, 100, 37.5):
            self.assertAlmostEqual(
                fahrenheit_to_celsius(celsius_to_fahrenheit(c)), c, places=7
            )

    def test_round_trip_negative(self):
        for c in (-1, -40, -273.15):
            self.assertAlmostEqual(
                fahrenheit_to_celsius(celsius_to_fahrenheit(c)), c, places=7
            )

    def test_round_trip_room_temperature(self):
        room = 22.5
        self.assertAlmostEqual(
            celsius_to_fahrenheit(fahrenheit_to_celsius(room)), room, places=7
        )

    def test_round_trip_from_fahrenheit(self):
        # 华氏方向往返：F -> C -> F，覆盖 0、负数、正数、室温
        for f in (0, -40, 98.6, 68.0):
            self.assertAlmostEqual(
                celsius_to_fahrenheit(fahrenheit_to_celsius(f)), f, places=7
            )


class TestTypeError(unittest.TestCase):
    def test_celsius_non_number(self):
        for bad in ("abc", None, [1, 2], {"a": 1}):
            with self.assertRaises(TypeError):
                celsius_to_fahrenheit(bad)

    def test_fahrenheit_non_number(self):
        for bad in ("100F", None, (1,), {"x": 2}):
            with self.assertRaises(TypeError):
                fahrenheit_to_celsius(bad)


if __name__ == "__main__":
    unittest.main()
