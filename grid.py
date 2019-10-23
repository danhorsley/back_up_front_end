import arcade
from curl_examples import *

floor_number = input('please input floor number : ')
floor_number = int(floor_number)
arq = heroku_query(all_rooms_query)['data']['rooms']
arq0 = [x for x in arq if x['floor'] == floor_number]
#print(arq0[0])


ROW_COUNT = 8
COLUMN_COUNT = 10

WIDTH = 50
HEIGHT = 50

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 10
CORRIDOR_y = MARGIN * 2
CORRIDOR_x = MARGIN
x = y = 0
bc = arcade.color.WHITE
color_region = {'in a castle' : [arcade.color.ASH_GREY,arcade.color.AUROMETALSAURUS],
                'on a mountain' : [arcade.color.AIR_SUPERIORITY_BLUE,arcade.color.AIR_FORCE_BLUE],
                'in the sewers' : [arcade.color.APPLE_GREEN,arcade.color.AO],
                'in an old abandoned mine' : [arcade.color.ANTIQUE_BRONZE,arcade.color.BISTRE_BROWN],
                'in a dungeon' : [arcade.color.BOSTON_UNIVERSITY_RED,arcade.color.BURGUNDY],
                'in a forest' : [arcade.color.BRITISH_RACING_GREEN,arcade.color.BUD_GREEN],
                'in an endless cave' : [arcade.color.CADET_BLUE,arcade.color.BRIGHT_NAVY_BLUE]}



SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """

        super().__init__(width, height, title)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = 0 #arcade.color.GREEN
                else:
                    color = 1 #arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                
                
                #matching to grid
                room_ref = [c for c in arq0 if c['x'] == column and c['y'] == row][0]

                # Draw the box
                my_color = color_region[room_ref['region']]
                
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, my_color[color])

                room_keys = ['nTo','sTo','eTo','wTo']
                for k in room_keys:
                    if room_ref[k] is not None:
                        directions = {'nTo' : [0, HEIGHT/2 ,CORRIDOR_x, CORRIDOR_y],
                                        'sTo' : [0, -HEIGHT/2 ,CORRIDOR_x, CORRIDOR_y],
                                        'eTo' : [WIDTH/2, 0 ,CORRIDOR_y, CORRIDOR_x],
                                        'wTo' : [-WIDTH/2, 0 ,CORRIDOR_y, CORRIDOR_x]}
                        m = directions[k]
                        arcade.draw_rectangle_filled(x +m[0], y +m[1] , m[2], m[3], my_color[color])   

                

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()