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
        if direction == "left":
            left_middle = (0,self.height/2)
            top_right = (self.width,self.height)
            bottom_right = (self.width,0)
            return left_middle, top_right, bottom_right
        else:
            bottom_left = (0,0)
            top_left = (0,self.height)
            right_middle = (self.width, self.height/2)
            return bottom_left, top_left, right_middle

class SlideSash(BaseSash):
    def __init__(self, width, height, sash_count):
        super().__init__(width, height)
        self.sash_count = sash_count
    
    def slide_points(self):
        middle_bottom = (self.width/2,0)
        middle_top = (self.width/2,self.height)
        left_bottom = (0,0)
        right_bottom = (self.width,0)
        left_top = (0,self.height)
        right_top =(self.width,self.height)
        return middle_bottom, middle_top, left_bottom, right_bottom,left_top, right_top
        

class FixSash:
    pass

        



if __name__ == "__main__":
    w1 = Window(100,150,5,8)
    print (w1.__dict__)
    sash1 = BaseSash(100,500)
    #print(RegularSash.open_points.__doc__)
    sash2 = SlideSash(100,150,5)
    print (sash2.sash_count)

