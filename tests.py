from unittest import TestCase, main
import windows

class TestFixPoints(TestCase):
    def setUp(self):
        self.sash = windows.RegularSash(100,150)


    def test_tilt_points_returns_3_elements(self):
        points = self.sash.tilt_points()
        self.assertEqual(3,len(points))

    def test_tilt_points_returns_correct_results(self):
        points = self.sash.tilt_points()
        expected = ((0,0),(50,150),(100,0))
        self.assertEqual(expected, points)

    def test_open_points_returns_3_elements(self):
        points = self.sash.open_points()
        self.assertEqual(3,len(points))

    def test_open_points_returns_correct_results_when_open_left(self):
        points = self.sash.open_points("left")
        expected = ((0,75),(100,150),(100,0))
        self.assertEqual(expected, points)
        #assert almost equal - for comapring floats

if __name__ == '__main__':
    main()