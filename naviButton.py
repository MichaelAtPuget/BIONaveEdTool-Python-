class NaviButton:
    def __init__(self, upper_left_corner, bottom_right_corner):
        self.upper_left_corner = upper_left_corner
        self.bottom_right_corner = bottom_right_corner

    def get_upper_left(self):
        return self.upper_left_corner

    def get_bottom_right(self):
        return self.bottom_right_corner
