import unittest
from unittest.mock import patch
from io import StringIO
import math
from mylib import Shape, Circle, Triangle, calculate_area

class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), 78.54, places=2)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0, places=2)

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(6, 8, 10)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right_triangle())

    def test_is_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(3,5,15)

    def test_invalid_shape_choice(self):
        with patch("builtins.input", return_value="3"):
            with self.assertRaises(ValueError):
                Shape.choose_shape()

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_negative_triangle_side(self):
        with self.assertRaises(ValueError):
            Triangle(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()