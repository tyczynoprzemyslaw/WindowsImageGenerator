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
        points = self.sash.open_points("left")
        self.assertEqual(3,len(points))

    def test_open_points_returns_correct_results_when_open_left(self):
        points = self.sash.open_points("left")
        expected = ((0,75),(100,150),(100,0))
        self.assertEqual(expected, points)
        #assert almost equal - for comapring floats

    def test_open_points_returns_correct_results_when_opne_right(self):
        points = self.sash.open_points("right")
        expected = ((0,0),(0,150),(100,75))
        self.assertEqual(expected, points)

if __name__ == '__main__':
    main()

class TestSlidePoints(TestCase):
        def setUp(self):
            self.sash = windows.SlideSash(300,230,2)

        def test_slide_points_returns_6_elements(self):
            points = self.sash.slide_points()
            expected = ((150,0),(150,230),(0,0),(300,0),(0,230),(300,230))
            self.assertEqual(expected, points)


if __name__ == '__main__':
    main()