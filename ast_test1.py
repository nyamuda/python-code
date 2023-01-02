"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import arcade

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class Velocity:
    def __init__(self):
        self.dx = 0 
        self.dy = 0

class Flying_object(ABC):
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.angle = 0

    def is_alive(self):
        return self.alive

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width,self.height,self.texture, self.angle, 255)

class Bullet(Flying_object):
    def __init__(self, ship_angle, ship_x, ship_y):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
        self.angle = ship_angle
        self.center.x = ship_x
        self.center.y = ship_y
   
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle)) * BULLET_SPEED
    
    def advance(self):
        super().advance()
        self.life -= 1
        if (self.life <= 0):
            self.alive = False
    

class Asteroid(Flying_object):
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0

class Small_rock(Asteroid):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_small1.png")
        self.radius = SMALL_ROCK_RADIUS
        self.hit_sound3 = arcade.load_sound(":resources:sounds/hit1.wav")
    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN
    def break_apart(self, asteroids):
        self.hit_sound3.play()
        self.alive = False
        
class Medium_rock(Asteroid):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.hit_sound2 = arcade.load_sound(":resources:sounds/explosion2.wav")
    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN
    def break_apart(self, asteroids):
        self.hit_sound2.play()
        small = Small_rock()
        small.center.x = self.center.x
        small.center.y = self.center.y
        small.velocity.dy = self.velocity.dy + 1.5
        small.velocity.dx = self.velocity.dx + 1.5
        small2 = Small_rock()
        small2.center.x = self.center.x
        small2.center.y = self.center.y
        small2.velocity.dy = self.velocity.dy - 1.5
        small2.velocity.dx = self.velocity.dx - 1.5
        asteroids.append(small)
        asteroids.append(small2)
        self.alive = False


class Large_rock(Asteroid):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/meteorGrey_big1.png")
        self.radius = BIG_ROCK_RADIUS
        self.center.x = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
        self.center.y = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        self.hit_sound1 = arcade.load_sound(":resources:sounds/explosion1.wav")

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN

    def break_apart(self, asteroids):
        self.hit_sound1.play()
        med1 = Medium_rock()
        med1.center.x = self.center.x
        med1.center.y = self.center.y
        med1.velocity.dy = self.velocity.dy + 2
        med1.velocity.dx = self.velocity.dx + 2
        med2 
        Medium_rock()
        med2.center.x = self.center.x
        med2.center.y = self.center.y
        med2.velocity.dy = self.velocity.dy - 2
        med2.velocity.dx = self.velocity.dx - 2
        small 
        Small_rock()
        small.center.x = self.center.x
        small.center.y = self.center.y
        small.velocity.dy = self.velocity.dy + 5
        small.velocity.dx = self.velocity.dx + 5
        asteroids.append(med1)
        asteroids.append(med2)
        asteroids.append(small)
        self.alive = False




class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()