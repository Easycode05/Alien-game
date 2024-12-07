import pygame
import sys

from settings import Settings
from ship import Ship
from bullets import Bullet

class AlienInvasion:
    '''overall class to manage game assets and behaviour'''
    
    def __init__(self):
        '''Initialize the game, and create game resources. '''
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
         
        #set up the screen dimension
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        
        #set background color
        self.bg_color = (self.settings.bg_color) 
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        
    def run_game(self):
        '''Check the main loop for the game'''
        
        while True:
        #watch for keyboard and mouse events.
            
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.bullets.update()
            self.clock.tick(60) #framerate = 60                   
            #Redraw the screen during each pass through the loop
        
    def _check_events(self):
        '''respond to keypresses and mouse events'''
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)   
            
            elif event.type == pygame.K_q:
                sys.exit()
    
    def  _check_keydown_events(self,event):
        """respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True                
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True                   
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True    
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True        
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _fire_bullet(self):
        '''create new bullet and add it it to bullets group'''
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme() 
            
        #make the most recently drawn screen visible
        pygame.display.flip()
        
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    