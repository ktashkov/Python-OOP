from project.toy_store import ToyStore
from unittest import TestCase


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_init(self):
        self.assertEqual(self.store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy_success(self):
        result = self.store.add_toy("A", "car")
        self.assertEqual(result, "Toy:car placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "car")

    def test_add_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("H", "car")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertEqual(self.store.toy_shelf["A"], None)

    def test_add_toy_shelf_taken(self):
        self.store.add_toy("A", "car")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "train")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")
        self.assertEqual(self.store.toy_shelf["A"], "car")

    def test_add_toy_toy_already_in_shelf(self):
        self.store.add_toy("A", "car")

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("B", "car")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")
        self.assertEqual(self.store.toy_shelf["A"], "car")
        self.assertEqual(self.store.toy_shelf["B"], None)

    def test_remove_toy_success(self):
        self.store.add_toy("A", "car")
        result = self.store.remove_toy("A", "car")
        self.assertEqual(result, "Remove toy:car successfully!")
        self.assertEqual(self.store.toy_shelf["A"], None)

    def test_remove_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("H", "car")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")
        self.assertEqual(self.store.toy_shelf["A"], None)

    def test_remove_toy_toy_not_in_shelf(self):
        self.store.add_toy("A", "car")

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "train")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")
        self.assertEqual(self.store.toy_shelf["A"], "car")

    def test_repr(self):
        self.store.add_toy("A", "car")
        self.store.add_toy("B", "train")
        self.store.add_toy("C", "doll")
        self.store.add_toy("D", "ball")
        self.store.add_toy("E", "puzzle")
        self.store.add_toy("F", "book")
        self.store.add_toy("G", "blocks")

        self.assertEqual(str(self.store), "Toy Store:\nA: car\nB: train\nC: doll\nD: ball\nE: puzzle\nF: book\nG: blocks")
