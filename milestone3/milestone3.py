"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import arcade
import random
from abc import ABC
import math
import time

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30
SHIP_LIVES = 4

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

#Abstract Class
class Flying_object(ABC):
    def __init__(self,img):
        self.centre = Point()
        self.velocity = Velocity()
        self.alive = True
        self.img=img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.angle = 0
       

    def is_alive(self):
        pass

    def advance(self):
        pass
    
    def draw(self):
        arcade.draw_texture_rectangle(self.centre.x, self.centre.y, self.width,self.height,self.texture, self.angle, 255)

    def wrap(self) :
        #if it goes to top edge of the screen
        if self.centre.y > SCREEN_HEIGHT:
            #appear on the botton edge
            self.centre.y -= SCREEN_HEIGHT
        #if it goes to bottom edge of the screen
        if self.centre.y < 0:
            #appear on the top edge
            self.centre.y += SCREEN_HEIGHT
        #if it goes to the right edge of the screen
        if self.centre.x > SCREEN_WIDTH:
            #appear on the left edge
            self.centre.x -= SCREEN_WIDTH
        #if it goes to the right edge of the screen
        if self.centre.x < 0:
            #appear on the left edge
            self.centre.x += SCREEN_WIDTH

#ASTEROIDS

class Asteroid(Flying_object):
    def __init__(self,img):
        super().__init__(img)
        self.radius = 0.0
    def is_alive(self):
        return self.alive

    def advance(self):
        self.wrap()
        self.centre.x += self.velocity.dx
        self.centre.y += self.velocity.dy
    
    
        
        
class SmallRock(Asteroid):
    def __init__(self):
        self.radius = SMALL_ROCK_RADIUS
        super().__init__("images/meteorGrey_small1.png")
        self.explosion_sound3 = arcade.load_sound("sounds/mixkit-short-explosion-1694.wav")
        
        
    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN\

    def breaking(self, asteroids):
        #playing the explosion sound
        self.explosion_sound3.play()
        self.alive = False
 
        
class MediumRock(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.explosion_sound2 = arcade.load_sound("sounds/mixkit-arcade-game-explosion-2759.wav")
        
    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN

    def breaking(self, asteroids):
        #playing the explosion sound
        self.explosion_sound2.play()
        small = SmallRock()
        small.centre.x = self.centre.x
        small.centre.y = self.centre.y
        small.velocity.dy = self.velocity.dy + 1.5
        small.velocity.dx = self.velocity.dx + 1.5
        small2 = SmallRock()
        small2.centre.x = self.centre.x
        small2.centre.y = self.centre.y
        small2.velocity.dy = self.velocity.dy - 1.5
        small2.velocity.dx = self.velocity.dx - 1.5
        asteroids.append(small)
        asteroids.append(small2)
        self.alive = False

  


class BigRock(Asteroid):
    def __init__(self):
        super().__init__('images/meteorGrey_big1.png')
        self.radius = BIG_ROCK_RADIUS
        self.centre.x = random.randrange(1,200)
        self.centre.y = random.randrange(1, 250)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        self.explosion_sound1 = arcade.load_sound("sounds/mixkit-truck-crash-with-explosion-1616.wav")

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN
    
    def breaking(self, asteroids):
        #playing the explosion sound
        self.explosion_sound1.play()
        med1 = MediumRock()
        med1.centre.x = self.centre.x
        med1.centre.y = self.centre.y
        med1.velocity.dy = self.velocity.dy + 2
        med1.velocity.dx = self.velocity.dx + 2
        med2=MediumRock()
        med2.centre.x = self.centre.x
        med2.centre.y = self.centre.y
        med2.velocity.dy = self.velocity.dy - 2
        med2.velocity.dx = self.velocity.dx - 2
        small=SmallRock()
        small.centre.x = self.centre.x
        small.centre.y = self.centre.y
        small.velocity.dy = self.velocity.dy + 5
        small.velocity.dx = self.velocity.dx + 5
        asteroids.append(med1)
        asteroids.append(med2)
        asteroids.append(small)
        self.alive = False

#OTHER FLYING OBJECTS

class Bullet(Flying_object):
    def __init__(self,ship_x,ship_y,angleOfShip):
        super().__init__("images/laserBlue01.png")
        self.angle=angleOfShip
        self.speed=BULLET_SPEED
        self.centre.x=ship_x
        self.centre.y=ship_y
        self.life=BULLET_LIFE
        self.radius=BULLET_RADIUS

    def advance(self) :
        self.wrap()
        self.centre.x += self.velocity.dx
        self.centre.y += self.velocity.dy
        self.life -= 1
        if (self.life <= 0):
            self.alive = False

    def is_alive(self) :
        return self.alive

    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle)) * BULLET_SPEED


    
    

class Ship(Flying_object):
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        self.alpha = 0
        self.angle = 1
        self.radius = SHIP_RADIUS
        self.alive = True
        self.centre.x = (SCREEN_WIDTH / 2)
        self.centre.y = (SCREEN_HEIGHT / 2)
        self.protected = False
        self.lives=SHIP_LIVES

    def thrust_up(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        

    def thrust_down(self):
        self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        
    def moveRight(self) :
        self.angle -= SHIP_TURN_AMOUNT
    def moveLeft(self) :
        self.angle += SHIP_TURN_AMOUNT
    def advance(self):
        self.wrap()
        self.centre.x += self.velocity.dx
        self.centre.y += self.velocity.dy

    




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

        self.bullet_sound=arcade.load_sound("sounds/mixkit-laser-gun-shot-3110.wav")
        self.victory_sound=arcade.load_sound("sounds/sfx-victory6.mp3")
        self.game_over_sound=arcade.load_sound("sounds/sfx-defeat4.mp3")

        self.asteroids = []
        self.gameOver=False
        self.ship=Ship()
        
        self.bullets=[]
        #creating the large rocks
        for i in range(INITIAL_ROCK_COUNT) :
            big_rock=BigRock()
            self.asteroids.append(big_rock)


    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()

        for bullet in self.bullets:
            bullet.draw()
        
        self.ship.draw()
        
    
    #remove any dead objects
    def dead_flying_objects(self) :
        #checking if the bullet is dead
        for bullet in self.bullets :
            if not bullet.is_alive() :
                self.bullets.remove(bullet)
        
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    #checking for any collisions

    def checkForCollisions(self):
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if (bullet.alive) and (asteroid.alive):
                    distance_x = abs(asteroid.centre.x - bullet.centre.x)
                    distance_y = abs(asteroid.centre.y - bullet.centre.y)
                    max_dist = asteroid.radius + bullet.radius
                    if (distance_x < max_dist) and (distance_y < max_dist):
                        bullet.alive = False
                        asteroid.breaking(self.asteroids)
        for asteroid in self.asteroids:
            if (self.ship.alive) and (asteroid.alive) and (self.ship.protected ==False):
                distance_x = abs(asteroid.centre.x - self.ship.centre.x)
                distance_y = abs(asteroid.centre.y - self.ship.centre.y)
                max_dist = asteroid.radius + self.ship.radius
                if (distance_x < max_dist) and (distance_y < max_dist):
                    asteroid.breaking(self.asteroids)
                    print(self.ship.lives)
                    self.ship.lives -= 0.25
                    if self.ship.lives > 0:
                        # self.ship.protected = True
                        self.ship.alpha = 0
                    else: 
                        time.sleep(1)
                        self.ship.alive = False
                        self.game_over_sound.play()
                        self.ship.velocity.dx=0
                        self.ship.velocity.dy=0
                        
                        print("Game Over")



    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        if self.gameOver==False :
            self.check_keys()
            # TODO: Tell everything to advance or move forward one step in time
            for asteroid in self.asteroids:
                asteroid.advance()

            for bullet in self.bullets:
                bullet.advance()

            self.ship.advance()

            # TODO: Check for collisions
            self.checkForCollisions()

            #remove dead flying objects
            self.dead_flying_objects()

            # if all asteroids are gone -- you WIN
            if len(self.asteroids) == 0:
                self.victory_sound.play()
                # time.sleep(10)
                self.gameOver=True
                # self.victory_sound.play()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.moveLeft()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.moveRight()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust_up()

        if arcade.key.DOWN in self.held_keys:
            self.ship.thrust_down()

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
                #creating the bullets
                the_bullet=Bullet(self.ship.centre.x, self.ship.centre.y, self.ship.angle)
                #adding the bullet to the bullets list
                self.bullets.append(the_bullet)
                #move the bullet
                the_bullet.fire()

                #play the bullet sound
                self.bullet_sound.play()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()