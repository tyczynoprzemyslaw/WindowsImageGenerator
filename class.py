class Window:
    def __init__(self,size,sash_count,frame_width):
        self.size = WindowSize(*size)
        self.sash_count = sash_count
        self.frame_width = frame_width 
    # okno ma wymiary, szerokośc ramki i skrzydła

    def __repr__(self):
        return f"Window({self.size},{self.glaze_count},{self.frame_width})"


class WindowSize:
    def __init__(self,width, height):
        self.width= width
        self.height = height
    
    def __repr__(self):
        return f"WindowSize({self.width},{self.height})"
    

class SashSize (WindowSize):
    pass


class BaseSash:
    def __init__(self,sash_size):
        self.sash_size = sash_size
    

class RegularSash:
    def __init__(self,sash_size):
        super(self).__init__(sash_size)
        self.tilt_points = tilt_points
        self.open_points = open_points


    def tilt_points(self):
        x = (0,0)
        y = (self.)


        return x,y,z        

class SlideSash:
    pass


class FixSash:
    pass

        



if __name__ == "__main__":
    s1 = WindowSize(100,100)
    print (s1)
    w1 = Window((100,150),5,8)
    print (w1.__dict__)
    sash1 = BaseSash((100,500))
    

