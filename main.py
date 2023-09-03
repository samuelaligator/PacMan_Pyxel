import pyxel
import numpy as np

# In the grid, there are two columns before the start of the maze, to avoid teleportation problems.
# So I have to move many elements two columns in my program.

grid = np.array([  # The maze : 0 = empty square, 1 = wall, 2 = dot, 3 = large dot
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

direction_offset = {
    0: (0, 1),  # Down
    1: (0, -1),  # Up
    2: (-1, 0),  # Left
    3: (1, 0)  # Right
}


def draw_dots():
    for column_number in range(2, grid.shape[1]):  # 2, = two-column offset (see grid)
        for line_number in range(grid.shape[0]):
            if grid[line_number, column_number] == 2:
                pyxel.rect(column_number * 8 + 3 - 16, line_number * 8 + 3, 2, 2,
                           2)  # -16 = two-column offset (see grid)
            elif grid[line_number, column_number] == 3:
                pyxel.blt(column_number * 8 - 16, line_number * 8, 0, 224, 0, 8, 8,
                          0)  # -16 = two-column offset (see grid)
            # to see the wall hitbox :
            # elif grid[line_number, column_number] == 1:
            #    pyxel.rect(column_number * 8 - 16, line_number * 8, 8, 8, 4)


class Pacman:

    def __init__(self):
        self.x = 104  # 106 position de depart
        self.y = 184
        self.x_grid = 13
        self.y_grid = 23
        self.input_direction = 2
        self.direction = 2
        self.walking = True
        self.mouth = 2
        self.i_mouth = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_position_saved = False
        self.swiped = False
        self.swipe_sensitivity = 15

    def draw_pacman(self):

        # to center pacman
        x = self.x - 2
        y = self.y - 3

        tile_x = {1: 19, 2: 3}
        tile_y = {0: 49, 1: 33, 2: 17, 3: 1}

        if self.mouth == 0:
            pyxel.blt(x, y, 1, 35, 1, 13, 13, 0)
        else:
            pyxel.blt(x, y, 1, tile_x[self.mouth], tile_y[self.direction], 13, 13, 0)

    def main(self):

        self.direction_detection()
        self.pacman_mouth()

        if self.x % 8 == 0 and self.y % 8 == 0:
            self.x_grid = self.x // 8 + 2  # +2 = two-column offset (see grid)
            self.y_grid = self.y // 8
            self.pacman_eats()
            self.check_walls()

        self.teleportation()
        self.pacman_movement()

    def direction_detection(self):
        direction_keys = {0: (pyxel.KEY_DOWN, pyxel.KEY_S, pyxel.GAMEPAD1_BUTTON_DPAD_DOWN),
                          1: (pyxel.KEY_UP, pyxel.KEY_Z, pyxel.GAMEPAD1_BUTTON_DPAD_UP),
                          2: (pyxel.KEY_LEFT, pyxel.KEY_Q, pyxel.GAMEPAD1_BUTTON_DPAD_LEFT),
                          3: (pyxel.KEY_RIGHT, pyxel.KEY_D, pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)}
        for i, (key1, key2, key3) in direction_keys.items():
            if pyxel.btn(key1) or pyxel.btn(key2) or pyxel.btn(key3):
                self.input_direction = i
                break  # Exit the loop after finding the first pressed key

        # swipe system for touch screens
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            if self.mouse_position_saved and not self.swiped:
                if abs(self.mouse_x - pyxel.mouse_x) >= self.swipe_sensitivity:
                    self.input_direction = 2 if self.mouse_x - pyxel.mouse_x > 0 else 3
                    self.swiped = True
                elif abs(self.mouse_y - pyxel.mouse_y) >= self.swipe_sensitivity:
                    self.input_direction = 1 if self.mouse_y - pyxel.mouse_y > 0 else 0
                    self.swiped = True
            elif not self.mouse_position_saved:
                self.mouse_x, self.mouse_y = pyxel.mouse_x, pyxel.mouse_y
                self.mouse_position_saved = True
        else:
            self.mouse_position_saved, self.swiped = False, False

    def pacman_mouth(self):
        converter = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 1, 7: 1}

        if self.walking:
            self.mouth = converter[self.i_mouth]
            self.i_mouth = (self.i_mouth + 1) % 8
        elif self.mouth == 0:
            self.i_mouth = 2
            self.mouth = 1

    def pacman_eats(self):
        grid[self.y_grid, self.x_grid] = 0

    def check_walls(self):
        x_offset, y_offset = direction_offset[self.input_direction]
        x_offset2, y_offset2 = direction_offset[self.direction]

        if grid[self.y_grid + y_offset, self.x_grid + x_offset] != 1:
            self.direction = self.input_direction
            self.walking = True
        elif grid[self.y_grid + y_offset2, self.x_grid + x_offset2] == 1:
            self.walking = False

    def teleportation(self):
        x = {2: 224, 3: -8}
        if self.x <= -8 or self.x >= 224:
            self.x = x[self.direction]

    def pacman_movement(self):
        if self.walking:
            offset_x, offset_y = direction_offset[self.direction]
            self.x += offset_x
            self.y += offset_y


class App:
    def __init__(self):
        pyxel.init(224, 248, "Pac-Man", 65, pyxel.KEY_ESCAPE, 10)
        pyxel.load("theme.pyxres")
        self.pacman = Pacman()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.pacman.main()

    def draw(self):
        pyxel.cls(0)
        draw_dots()
        pyxel.blt(0, 0, 0, 0, 0, 224, 248, 0)
        self.pacman.draw_pacman()


App()
