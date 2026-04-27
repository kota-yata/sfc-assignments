import unittest

from analysis import process_items

class TestProcessItems(unittest.TestCase):
    def test_numeric_strings_average(self):
        data = ["1", "2", "3", "4"]
        self.assertEqual(process_items(data), 2.5)

    def test_non_numeric_string_raises_value_error(self):
        for bad in ["abc", "", "NaN"]:
            with self.assertRaises(ValueError):
                process_items(["1", bad, "3"])

    def test_float_like_string_raises_value_error(self):
        for bad in ["3.14", "1e3", "+2.0", "-0.1"]:
            with self.assertRaises(ValueError):
                process_items([bad])

    def test_uncastable_types_raise_type_error(self):
        samples = [object(), [], {}, set(), (lambda: 1)]
        for bad in samples:
            with self.assertRaises(TypeError):
                process_items(["1", bad])

    def test_empty_data_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            process_items([])

    def test_none_data_raises_type_error(self):
        with self.assertRaises(TypeError):
            process_items(None)

    def test_non_iterable_data_raises_type_error(self):
        with self.assertRaises(TypeError):
            process_items(123)

    def test_generator_without_len_raises_type_error(self):
        def gen():
            for x in ["1", "2", "3"]:
                yield x

        with self.assertRaises(TypeError):
            process_items(gen())

    def test_float_items_are_truncated_by_int(self):
        data = [1.9, 2.1]
        self.assertEqual(process_items(data), 1.5)

    def test_bools_treated_as_ints(self):
        data = [True, True, False]
        self.assertAlmostEqual(process_items(data), 2 / 3)

    def test_outlier_large_value_skews_mean(self):
        data = ["1", "2", "3", str(10**12)]
        expected = (1 + 2 + 3 + 10**12) / 4
        self.assertEqual(process_items(data), expected)

    def test_large_input_reasonable_runtime(self):
        data = ["1"] * 10000
        self.assertEqual(process_items(data), 1.0)

    def test_custom_object_with___int__(self):
        class Seven:
            def __int__(self):
                return 7

        data = [Seven(), Seven(), "7"]
        self.assertEqual(process_items(data), (7 + 7 + 7) / 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

