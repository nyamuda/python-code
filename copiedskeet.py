"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

class Point:
    
    """ Initialize of point object, used by Rifle, Bullet, Target """
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        
class Velocity:
    
    """ Initialize velocity object, used by Rifle, Bullet, Target """
    def __init__(self, init_dx, init_dy):
        self.dx = init_dx
        self.dy = init_dy
        
class flying_object:
    
    """ Initialize of a flying object, which utilizes classes: Point and Velocity """
    def __init__(self):
        self.center = Point(0,0) 
        self.velocity = Velocity(0,0)

class Bullet(flying_object):
    """ Bullet object, and its methods """
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.alive = True
        
        # Initialize new bullet starting point to (25, 25)
        self.center.x = 25 
        self.center.y = 25
        
        # Sounds
        self.bullet_sound = arcade.load_sound("pepSound1.ogg")
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def draw(self, angle):
        """ Missle Sprite """
        texture = arcade.load_texture("spaceMissiles_012.png")
        scale = .5
        arcade.draw_texture_rectangle(self.center.x, self.center.y, scale * texture.width, scale * texture.height, texture, angle - 90)
        # UNUSED: arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)
    
    # Check if bullet is in screen, return boolean to caller
    def is_off_screen(self, SWidth, SHeight):
        is_bullet_in_range = False # Initalize bool variable
        if (self.center.x < SWidth) and (self.center.y < SHeight):
            is_bullet_in_range = False
        else:
            is_bullet_in_range = True
        return is_bullet_in_range
        
    def fire(self, angle: float):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
        
class Target(flying_object):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_RADIUS
        self.alive = True    # Target bool
        self.target_type = -1    # Initialize target type
        self.lifes = 1   # Initialize target lifes
        
        #Sounds
        random_sound = random.randint(0, 1)
        
        if random_sound == 0:
            self.safe_sound = arcade.load_sound("wrong.ogg")
        elif random_sound == 1:
            self.safe_sound = arcade.load_sound("war_medic.ogg")
        
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def draw(self):
        text_x = self.center.x - (self.radius * 1.2)
        text_y = self.center.y - (self.radius / 500)
        safe_square_length = TARGET_SAFE_RADIUS * 2
        
        if self.target_type == 0:
            """ Meteor Sprite """
            scale = .18
            texture = arcade.load_texture("spaceMeteors_001.png")
            arcade.draw_texture_rectangle(self.center.x, self.center.y, scale * texture.width, scale * texture.height, texture, 90)
#            UNUSED: arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)   
        elif self.target_type == 1:
            """ Alien sprite """
            scale = .3
            texture = arcade.load_texture("shipGreen_manned.png")
            arcade.draw_texture_rectangle(self.center.x, self.center.y, scale * texture.width, scale * texture.height, texture, 0)
#            UNUSED: arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
            arcade.draw_text(repr(self.lifes), text_x, text_y, TARGET_COLOR, font_size = 15)
        elif self.target_type == 2:
            """ Bomb Sprite """
            scale = .8
            texture = arcade.load_texture("spaceBuilding_003.png")
            arcade.draw_texture_rectangle(self.center.x, self.center.y, scale * texture.width, scale * texture.height, texture, 90)
#            UNUSED: arcade.draw_rectangle_filled(self.center.x, self.center.y, safe_square_length, safe_square_length, TARGET_SAFE_COLOR)
        else:
            print("Target Error")
        
    def is_off_screen(self, SWidth, SHeight):
        is_target_in_range = False # Initalize bool variable
        if (self.center.x < SWidth) and (self.center.y < SHeight):
            is_target_in_range = False
        else:
            is_target_in_range = True
        return is_target_in_range
    
    def hit(self):
        
        if self.target_type == 0:  # Standard Target (Asteroid)
            self.alive = False  # Decalre dead target
            return 1
                    
        elif self.target_type == 1:  # Strong Target (Alien)
            if self.lifes == 1:
                self.alive = False  # Decalre dead target
                return 5
            else:
                self.lifes -= 1  # decrement lifes 
                return 1
            
        elif self.target_type == 2:  # Safe Target (Bomb)
            self.alive = False  # Decalre dead target
            return -10
             
        else:
            print("Target Deletion Error")
        
        
        

class Rifle:
    """ The rifle is a rectangle that tracks the mouse. """
    def __init__(self):
        self.center = Point(20,20) # Offset to (20, 20) so that you can see the ship
        self.angle = 45

    def draw(self):
        """ Space Ship Sprite """ 
        texture = arcade.load_texture("spaceShips_007.png")
        scale = .3
        arcade.draw_texture_rectangle(self.center.x, self.center.y, scale * texture.width, scale * texture.height, texture, self.angle - 90)
        # UNUSED: arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        
        # Background image
        self.background = None

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []
        self.targets = []

#        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game background """

        # Load the background image.
        self.background = arcade.load_texture("Space_background.jpg")

    def on_draw(self):
        """ Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements. """
        
        # clear the screen to begin drawing
        arcade.start_render()
        
         # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw(self.angle)

        # iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """ Puts the current score on the screen """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE)

    def update(self, delta_time):
        """ Update each object in the game. :param delta_time:
        tells us how much time has actually elapsed """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # DONE: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        # TODO: Decide what type of target to create and append it to the list
        target = Target()
        target.center.x = random.uniform(10, SCREEN_WIDTH / 2)
        target.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT) 
        random_target = random.randint(0, 2) # Random target chooser
        
        if random_target == 0:  # Standard Target
            target.target_type = 0
            target.velocity.dx = random.randint(1, 5)
            target.velocity.dy = random.randint(-2, 5)
        elif random_target == 1:  # Strong Target
            target.lifes = 3  # Give strong target 3 lifes
            target.target_type = 1
            target.velocity.dx = random.randint(1, 3)
            target.velocity.dy = random.randint(-2, 3)
        elif random_target == 2:  # Safe Target
            target.target_type = 2
            target.velocity.dx = random.randint(1, 5)
            target.velocity.dy = random.randint(-2, 5)
            
        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()
                        if target.target_type == 2:
                            arcade.play_sound(target.safe_sound)

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        self.angle = self._get_angle_degrees(x, y)
        
        bullet = Bullet()
        bullet.fire(self.angle)

        self.bullets.append(bullet)
        arcade.play_sound(bullet.bullet_sound)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
window.setup()
arcade.run()
