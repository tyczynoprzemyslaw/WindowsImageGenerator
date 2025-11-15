class Window:
    def __init__(self,width, height,sash_count,frame_width):
        self.width = width
        self.height = height
        self.sash_count = sash_count
        self.frame_width = frame_width 
    # okno ma wymiary, szerokośc ramki i skrzydła

    def __repr__(self):
        return f"Window({self.width},{self.height},{self.glaze_count},{self.frame_width})"


class BaseSash:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    

class RegularSash(BaseSash):
    def __init__(self,width, height):
        super().__init__(width,height)
       # self.tilt_points = tilt_points
       # self.open_points = open_points
       # rewt


    def tilt_points(self):
        bottom_left = (0,0)
        top_middle = (self.width/2,self.height)
        bottom_right = (self.width,0)
        return bottom_left, top_middle, bottom_right     

    def open_points(self, direction):
        """Left or right is site of klamka"""
        left_middle = (0,self.height/2)
        top_right = (self.width,self.height)
        bottom_right = (self.width,0)
        return left_middle, top_right, bottom_right

class SlideSash:
    pass


class FixSash:
    pass

        



if __name__ == "__main__":
    w1 = Window(100,150,5,8)
    print (w1.__dict__)
    sash1 = BaseSash(100,500)
    print(RegularSash.open_points.__doc__)

