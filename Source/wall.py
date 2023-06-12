from Source.tiles import Tiles


class Wall(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)

class Pin(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)

class lava(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)

class castle(Tiles):
    def __init__(self, size, start_coordinates, image):
        super().__init__(size, start_coordinates, image)
