from Source.tiles import Tiles


class Wall(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)

class PIN(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)
