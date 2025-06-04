
import os
import random
import sys
import random
import json
import pygame 


pygame.init()

BLACK = (0,0,0)

font1 = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 60)


WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fight Gang")
background = pygame.transform.scale(pygame.image.load('assets/background.png'),(WIDTH,HEIGHT))




FPS = 60
clock = pygame.time.Clock()

class Character:
    def __init__(self, x, y,name):
        self.x = x
        self.y = y
        self.name = name

        self.width =330
        self.height = 394

        self.state = "idle"

        self.animation_count = 0
        self.animations = {
            "idle": [],
            "attack1": [],
            "attack2": [],
            "crouch": [],
            "block": [],
            "jump":[],
            "knife":[],
            "leg":[],
        }
        self.animation_speeds = {
            "idle": 0.5,
            "attack1": 0.5,
            "attack2": 0.5,
            "leg":0.5,
            "jump":0.3,
            "knife":0.6
        }
  
        self.reverse_speeds = {
            "crouch": 0.8,
            "block": 0.8
        }

        self.Rattack = False
        self.Rblock = False
        self.Rcrouch = False
        self.Rjump = False
        self.Rknife = False
        self.Rleg = False
        self.Rrage = False

        self.load_animations()

        self.attacking = False
        self.crouching = False
        self.blocking = False
        self.jumping = False
        self.leg = False
        self.knife = False

        self.win = False
        self.lose = False

        self.attack_cooldown = 0
        self.active_cooldown = 0
        self.invis_cooldown = 0
        self.attack_cooldown2 = 0
        self.ragecooldown = 0
        self.count = 0


        self.last_state = None
        self.reverse_animation = False
        self.attacks = ['attack1','attack2']
        self.last_attack = None

        self.rage = 0

        self.hits_data = heroes_hits_data 

        self.heroes_data = heroes_data_cards

        self.heroname = self.heroes_data[self.name]['name']
        self.fullhealth = self.heroes_data[self.name]['HP']
        self.defence = self.heroes_data[self.name]['DEF']
        self.damage = self.heroes_data[self.name]['DMG']
        self.ragex = self.heroes_data[self.name]['RAGE']

        self.health = self.fullhealth
        
        self.rect_pos_RED = [0,0,0,0]
        self.rect_pos_GREEN = [0,0,0,0]

        self.rect_pos_RAGE1 = [0,0,0,0]
        self.rect_pos_RAGE2 = [0,0,0,0]

    
    def load_animations(self):
        animation_data = {
            "idle": {"folder": "assets/heroes/"+self.name+"/idle", "frames": 13},
            "attack1": {"folder": "assets/heroes/"+self.name+"/attack1", "frames": 3},
            "attack2": {"folder": "assets/heroes/"+self.name+"/attack2", "frames": 3},
            "crouch": {"folder": "assets/heroes/"+self.name+"/crouch", "frames": 2},
            "block": {"folder": "assets/heroes/"+self.name+"/block", "frames": 2},
            "jump": {"folder": "assets/heroes/"+self.name+"/jump", "frames": 5},
            "knife": {"folder": "assets/heroes/"+self.name+"/knife", "frames": 8},
            "leg": {"folder": "assets/heroes/"+self.name+"/leg", "frames": 13},
        }
        
        for state, data in animation_data.items():
            folder = data["folder"]
            frame_count = data["frames"]
            
            
            for i in range(frame_count):
                file_path = os.path.join(folder, f"{i}.png")
                if os.path.exists(file_path):
                
                    img = pygame.image.load(file_path).convert_alpha()
                    original_width, original_height = img.get_size()
                    scale_factor = 7  
                    new_width = int(original_width * scale_factor)
                    new_height = int(original_height * scale_factor)
                    img = pygame.transform.scale(img, (new_width, new_height))
                    self.animations[state].append(img)
    
    def update(self,player2es):
 
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.active_cooldown > 0:
            self.active_cooldown -= 1
        if self.invis_cooldown > 0:
            self.invis_cooldown -= 1
        if self.attack_cooldown2 > 0:
            self.attack_cooldown2 -= 1
        if self.ragecooldown > 0:
            self.ragecooldown -= 1
        if self.count > 0:
            self.count -= 1

        if self.rage > 0 and self.ragecooldown <= 0 and self.rage != 200 and not self.Rrage:
            self.rage -= 2/self.ragex
            self.ragecooldown = 10

        if self.rage>200:
            self.rage = 200

        if self.Rrage and self.rage > 0 and self.ragecooldown <= 0:
            self.rage -= 16/self.ragex
            self.ragecooldown = 5
            if self.rage == 0:
                self.Rrage = False

        
        if self.win:
            ko_label = pygame.transform.scale(pygame.image.load('assets/heroes/'+str(self.name)+'/KO.png'),(300,300))
            screen.blit(ko_label,(490,210))
        
        if self.lose:
            if self.x < 1300 and self.x > -300:
                if player2es:
                    if self.x >720:
                        if self.count <= 0:
                            self.x+=150
                            self.count = 1
                    else:
                        if self.count <= 0:
                            self.x+=5
                            self.count = 1
                    
                else:
                    if self.x < 200:
                        if self.count <= 0:
                            self.x-=150
                            self.count = 1
                    else:
                        if self.count <= 0:
                            self.x-=5
                            self.count = 1
                
        if self.last_state != self.state:
            self.animation_count = 0
            self.last_state = self.state
            self.reverse_animation = False

        if player2es:

            self.rect_pos_RED = pygame.Rect(WIDTH - self.fullhealth, 680, self.fullhealth, 20)
            self.rect_pos_GREEN = pygame.Rect(WIDTH, 680, -self.health, 20) 
            self.rect_pos_GREEN.normalize()
            
            self.rect_pos_RAGE1 = pygame.Rect(WIDTH - 100*2, 650, 100*2, 20)
            self.rect_pos_RAGE2 = pygame.Rect(WIDTH, 650, -self.rage, 20)
            self.rect_pos_RAGE2.normalize()

        else:

            self.rect_pos_RED = pygame.Rect(0, 680, self.fullhealth, 20)
            self.rect_pos_GREEN = pygame.Rect(0, 680, self.health, 20)
            
            
            self.rect_pos_RAGE1 = pygame.Rect(0, 650, 100*2, 20)
            self.rect_pos_RAGE2 = pygame.Rect(0, 650, self.rage, 20)

        if gameplay:
        
            if self.state == 'attack1' and int(self.animation_count) == self.hits_data[self.name]['hit_attack1']:

                self.Rattack = True

                self.Rblock = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rknife = False
                self.Rleg = False

            elif self.state == 'attack2' and int(self.animation_count) == self.hits_data[self.name]['hit_attack2']:

                self.Rattack = True

                self.Rblock = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rknife = False
                self.Rleg = False

            elif self.state == 'block' and int(self.animation_count) == self.hits_data[self.name]['hit_block']:

                self.Rblock = True

                self.Rattack = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rknife = False
                self.Rleg = False

            elif self.state == 'crouch' and int(self.animation_count) == self.hits_data[self.name]['hit_crouch']:

                self.Rcrouch = True

                self.Rattack = False
                self.Rblock = False
                self.Rjump = False
                self.Rknife = False
                self.Rleg = False

            elif self.state == 'jump' and int(self.animation_count) in self.hits_data[self.name]['hit_jump']:

                self.Rjump = True

                self.Rcrouch = False
                self.Rattack = False
                self.Rblock = False
                self.Rknife = False
                self.Rleg = False

            elif self.state == 'knife' and int(self.animation_count) in self.hits_data[self.name]['hit_knife']:

                self.Rknife = True

                self.Rattack = False
                self.Rblock = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rleg = False

            elif self.state == 'leg' and int(self.animation_count) == self.hits_data[self.name]['hit_leg']:

                self.Rleg = True

                self.Rattack = False
                self.Rblock = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rknife = False
            
            else:
                self.Rleg = False
                self.Rattack = False
                self.Rblock = False
                self.Rcrouch = False
                self.Rjump = False
                self.Rknife = False

            
            speed = self.reverse_speeds.get(self.state, self.animation_speeds.get(self.state, 0.1))
            
            if not self.reverse_animation:
                self.animation_count += speed
                max_frame = len(self.animations[self.state]) - 1
                if int(self.animation_count) >= max_frame:
                    if self.state in ["attack1", "attack2","jump","knife","leg"]:
                        self.animation_count = max_frame
                        if self.attack_cooldown <= 0:
                            if self.state == 'attack1' or 'attack2':
                                self.attack_cooldown2 = 10
                            self.state = "idle"
                            self.attacking = False
                            self.jumping = False
                            self.leg = False
                            self.knife = False
                    elif self.state == "idle":
                        self.animation_count = 0
                    else: 
                        self.animation_count = max_frame
            else:
                self.animation_count -= speed
                if self.animation_count <= 0:
                    self.animation_count = 0
                    self.state = "idle"
                    self.reverse_animation = False
    
    def draw(self, screen,player2es):
        if not self.animations[self.state]: 
            self.create_placeholder_frame(self.state)
            
        frame = min(int(self.animation_count), len(self.animations[self.state]) - 1)
        if player2es:
            flipped_image = pygame.transform.flip(self.animations[self.state][frame], True, False)
            screen.blit(flipped_image, (self.x, self.y))
        else:
            screen.blit(self.animations[self.state][frame], (self.x, self.y))
    
    def attack(self):
        if self.attack_cooldown <= 0 and not self.attacking and not self.blocking and not self.crouching and not self.jumping and not self.leg and not self.knife and self.attack_cooldown2 <= 0:
            self.state = random.choice(self.attacks)
            if self.state == 'attack1' and self.last_attack == 'attack1':
                self.state == 'attack2'
            if self.state == 'attack2' and self.last_attack == 'attack2':
                self.state == 'attack1'
            self.last_attack = self.state
            self.animation_count = 0
            self.attacking = True
            self.attack_cooldown = 10
           
        
    
    def crouch(self, is_crouching):
        if self.active_cooldown <= 0 and not self.attacking and not self.blocking and not self.jumping and not self.leg and not self.knife:
            self.crouching = is_crouching
            if is_crouching:
                self.state = "crouch"
                self.animation_count = 0
                self.reverse_animation = False
            elif self.state == "crouch":
                self.reverse_animation = True
                self.active_cooldown = 1
            
    
    def block(self, is_blocking):
        if self.active_cooldown <= 0 and not self.attacking and not self.crouching and not self.jumping and not self.leg and not self.knife:
            self.blocking = is_blocking
            if is_blocking:
                self.state = "block"
                self.animation_count = 0
                self.reverse_animation = False
            elif self.state == "block":
                self.reverse_animation = True
                self.active_cooldown = 1
    
    def jump(self):
        if self.active_cooldown <= 0 and not self.attacking and not self.blocking and not self.crouching and not self.jumping and not self.leg and not self.knife:
            self.state = "jump"
            self.animation_count = 0
            self.jumping = True
            self.active_cooldown = 1

    def legp(self):
        if self.attack_cooldown <= 0 and not self.attacking and not self.blocking and not self.crouching and not self.jumping and not self.leg and not self.knife and self.attack_cooldown2 <= 0:
            self.state = "leg"
            self.animation_count = 0
            self.leg = True
            self.attack_cooldown = 2

    def knifedd(self):
        if self.attack_cooldown <= 0 and not self.attacking and not self.blocking and not self.crouching and not self.jumping and not self.leg and not self.knife and self.attack_cooldown2 <= 0:
            self.state = "knife"
            self.animation_count = 0
            self.knife = True
            self.attack_cooldown = 2
    def win1(self,player2es):
        self.win = True       
    def lose1(self,player2es):
        self.lose = True

class RectDraw(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.color = color
    
    def update_surf(self, size, line=0):
        pygame.draw.rect(screen, self.color, size, line)

class IconDraw(pygame.sprite.Sprite):
    def __init__(self, filedir, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('assets/heroes/'+filedir+'/icon.png'), (160, 160))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.filedir = filedir  
    
    def update_surf(self):
        screen.blit(self.image, self.rect)

class TextDraw(pygame.sprite.Sprite):
    def __init__(self, text,font=False):
        super().__init__()
        if font:
            self.image = font2.render(text, True, (255, 255, 255))
        else:
            self.image = font1.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect()
    
    def update_surf(self,x,y):
        screen.blit(self.image, (x, y))

def start_start_anim(gameplay,start_anim):
    global count_startanim, counting 
    gameplay = False
    if count_startanim == 0:
        count_startanim = 25
        counting += 1
    elif count_startanim > 0:
        count_startanim -= 1
    if counting >3:
        start_anim = False
        gameplay = True
    else:
        if counting == 3:
            start_label = pygame.transform.scale(pygame.image.load('assets/start/' + str(counting) + '.png'), (744, 300))
            screen.blit(start_label, (300, 230))
        else:
            start_label = pygame.transform.scale(pygame.image.load('assets/start/' + str(counting) + '.png'), (300, 300))
            screen.blit(start_label, (490, 210))
    return gameplay,start_anim

def start_game(gameplay,start_anim,selected,choose_menu,gamerun):
    player1 = Character(310, 200,selected[0])
    player2 = Character(570, 200,selected[1])
    gameplay = True
    start_anim = True
    choose_menu = False
    gamerun = True
    return player1,player2,gameplay,start_anim,choose_menu,gamerun

space_esc_text = TextDraw('press "Space" to restart',True)

def reset():
    return False, True, False, False, True, False, None, [],0,25

space_pressed = False
ctrl_pressed = False
shift_pressed = False

with open('assets/heroes/heroes_data.txt', 'r') as f:
    json_data = json.load(f)  

with open('assets/heroes/heroes_hits_data.txt', 'r') as f:
    json_data_hits = json.load(f)  

with open('assets/json_files/heroes_data.json', 'w') as f:
    json.dump(json_data, f, indent=4)

with open('assets/json_files/heroes_hits_data.json', 'w') as f:
    json.dump(json_data_hits, f, indent=4)

with open('assets/json_files/heroes_data.json', 'r') as f:
    heroes_data_cards = json.load(f)

with open('assets/json_files/heroes_hits_data.json', 'r') as f:
    heroes_hits_data = json.load(f)

start_menu, choose_menu, gamerun, gameplay, running, start_anim, selected_hero, selected,counting,count_startanim = reset()

folder_path = "assets/heroes"
hero_folders = []
for d in os.listdir(folder_path):
    if os.path.isdir(os.path.join(folder_path, d)):
        hero_folders.append(d)

while running:

    screen.fill((255,255,255))

    if gamerun:
        if gameplay:  
            if player1.Rattack:
                if not player2.Rblock and not player2.Rcrouch:
                    if player2.invis_cooldown == 0:
                        if player1.Rrage:
                            player2.health -= int((random.randint(5,7)*player1.damage))*2
                        else:
                            player2.health -= int((random.randint(5,7)*player1.damage)/random.choice([1,player2.defence]))
                        player2.invis_cooldown = 15
                        player2.ragecooldown = 40
                        player2.rage += random.randint(5,10)*player2.ragex
                        if not player1.Rrage:
                            player1.ragecooldown = 20
                            player1.rage += random.randint(7,15)*player1.ragex
                elif player2.Rblock:
                    player2.health+=int(player2.fullhealth/100*2)
                    if player2.health>=player2.fullhealth:
                        player2.health = player2.fullhealth
                else:
                    player2.rage += random.randint(4,7)*player2.ragex
            

            if player2.Rattack:
                if not player1.Rblock and not player1.Rcrouch:
                    if player1.invis_cooldown == 0:
                        if player2.Rrage:
                            player1.health -= int((random.randint(5,7)*player2.damage))*3
                        else:
                            player1.health -= int((random.randint(5,7)*player2.damage)/random.choice([1,player1.defence]))
                        player1.invis_cooldown = 15
                        player1.ragecooldown = 40
                        player1.rage += random.randint(5,10)*player1.ragex
                        if not player2.Rrage:
                            player2.ragecooldown = 20
                            player2.rage += random.randint(7,15)*player2.ragex
                elif player1.Rblock:
                    player1.health+=int(player1.fullhealth/100*2)
                    if player1.health>=player1.fullhealth:
                        player1.health = player1.fullhealth
                else:
                    player1.rage += random.randint(4,7)*player1.ragex

            if player1.Rknife:
                if not player2.Rcrouch:
                    if player2.invis_cooldown == 0:
                        if player2.state == 'block':
                            player2.state = 'idle'
                        if player1.Rrage:
                            player2.health -= int((random.randint(2,7)*player1.damage))*3
                        else:
                            player2.health -= int((random.randint(2,7)*player1.damage)/random.choice([1,player2.defence]))
                        player2.invis_cooldown = 15
                        player2.ragecooldown = 40
                        player2.rage += random.randint(5,10)*player2.ragex
                        if not player1.Rrage:
                            player1.ragecooldown = 20
                            player1.rage += random.randint(5,10)*player1.ragex
                else:
                    player2.rage += random.randint(4,7)*player2.ragex

            if player2.Rknife:
                if not player1.Rcrouch:
                    if player1.invis_cooldown == 0:
                        if player1.state == 'block':
                            player1.state = 'idle'
                        if player2.Rrage:
                            player1.health -= int((random.randint(2,7)*player2.damage))*3
                        else:
                            player1.health -= int((random.randint(2,7)*player2.damage)/random.choice([1,player1.defence]))
                        player1.invis_cooldown = 15
                        player1.ragecooldown = 40
                        player1.rage += random.randint(5,10)*player1.ragex
                        if not player2.Rrage:
                            player2.ragecooldown = 20
                            player2.rage += random.randint(7,15)*player2.ragex
                else:
                    player1.rage += random.randint(4,7)*player1.ragex

            if player1.Rleg:
                if not player2.Rjump:
                    if player2.invis_cooldown == 0:
                        if player2.state == 'crouch':
                            player2.state = 'idle'
                        if player1.Rrage:
                            player2.health -= int((random.randint(2,7)*player1.damage))*3
                        else:
                            player2.health -= int((random.randint(2,7)*player1.damage)/random.choice([1,player2.defence]))
                        player2.invis_cooldown = 15
                        player2.ragecooldown = 40
                        player2.rage += random.randint(5,10)*player2.ragex
                        if not player1.Rrage:
                            player1.ragecooldown = 20
                            player1.rage += random.randint(7,15)*player1.ragex
                else:
                    player2.rage += random.randint(4,7)*player2.ragex

            if player2.Rleg:
                if not player1.Rjump:
                    if player2.invis_cooldown == 0:
                        if player1.state == 'crouch':
                            player1.state = 'idle'
                        if player2.Rrage:
                            player1.health -= int((random.randint(2,7)*player2.damage))*3
                        else:
                            player1.health -= int((random.randint(2,7)*player2.damage)/random.choice([1,player1.defence]))
                        player1.invis_cooldown = 15
                        player1.ragecooldown = 40
                        player1.rage += random.randint(5,10)*player1.ragex
                        if not player2.Rrage:
                            player2.ragecooldown = 20
                            player2.rage += random.randint(7,15)*player2.ragex
                else:
                    player1.rage += random.randint(4,7)*player1.ragex

            if player1.health <= 0:
                player1.lose1(False)
                player2.win1(True)
                gameplay = False
            elif player2.health <=0:
                player1.win1(False)
                player2.lose1(True)
                gameplay = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start_menu, choose_menu, gamerun, gameplay, running, start_anim, selected_hero, selected,counting,count_startanim = reset()
                if player1.lose or player1.win:
                    if event.key == pygame.K_SPACE:  
                        start_menu, choose_menu, gamerun, gameplay, running, start_anim, selected_hero, selected,counting,count_startanim = reset()
                if gameplay:
                    if event.key == pygame.K_d:  
                        player1.attack()
                    elif event.key == pygame.K_w:   
                        player1.jump()
                    elif event.key == pygame.K_f:  
                        player1.legp()
                    elif event.key == pygame.K_r:   
                        player1.knifedd()
                    elif event.key == pygame.K_s:  
                        player1.crouch(True)
                    elif event.key == pygame.K_a:
                        player1.block(True)
                    elif event.key == pygame.K_t:
                        if player1.rage == 200:
                            player1.Rrage = True
                    if event.key == pygame.K_LEFT:
                        player2.attack()
                    elif event.key == pygame.K_UP:
                        player2.jump()
                    elif event.key == pygame.K_l:
                        player2.legp()
                    elif event.key == pygame.K_k:
                        player2.knifedd()
                    elif event.key == pygame.K_DOWN:
                        player2.crouch(True)
                    elif event.key == pygame.K_RIGHT:
                        player2.block(True)
                    elif event.key == pygame.K_j:
                        if player2.rage == 200:
                            player2.Rrage = True       
            elif event.type == pygame.KEYUP:
                if gameplay:
                    if event.key == pygame.K_s:
                        player1.crouch(False)
                    elif event.key == pygame.K_a:
                        player1.block(False)
                    elif event.key == pygame.K_DOWN:
                        player2.crouch(False)
                    elif event.key == pygame.K_RIGHT:
                        player2.block(False)
        
        screen.blit(background,(0,0))

        player1.draw(screen,False)
        player2.draw(screen,True)

        player1.update(False)
        player2.update(True) 
        if player1.lose or player1.win:
            space_esc_text.update_surf(350,650)

        if start_anim == True:
           gameplay,start_anim = start_start_anim(gameplay,start_anim)

        pygame.draw.rect(screen,(255,0,0),player1.rect_pos_RED)
        pygame.draw.rect(screen,(0,255,0),player1.rect_pos_GREEN)

        pygame.draw.rect(screen,(255,0,0),player2.rect_pos_RED)
        pygame.draw.rect(screen,(0,255,0),player2.rect_pos_GREEN)

        pygame.draw.rect(screen,(255,128,0),player1.rect_pos_RAGE1)
        pygame.draw.rect(screen,(255,128,0),player2.rect_pos_RAGE1)

        if player2.rage != 200:
            pygame.draw.rect(screen,(255,51,51),player2.rect_pos_RAGE2)
        else:
            pygame.draw.rect(screen,(255,0,127),player2.rect_pos_RAGE2)

        if player1.rage != 200:
            pygame.draw.rect(screen,(255,51,51),player1.rect_pos_RAGE2)
        else:
            pygame.draw.rect(screen,(255,0,127),player1.rect_pos_RAGE2)


        HP = font1.render('HP:'+str(player1.health)+'/'+str(player1.fullhealth),True,(0,100,0))
        screen.blit(HP,(5,682))
        HP = font1.render('HP:'+str(player2.health)+'/'+str(player2.fullhealth),True,(0,100,0))
        screen.blit(HP,(1170,682))

    else:
        if choose_menu:
            pygame.draw.rect(screen,(96,96,96),[0,0,WIDTH,HEIGHT])
            pygame.draw.rect(screen,(50,50,50),[0,0,WIDTH,HEIGHT],10)
            choose_a_hero = font1.render('choose a hero',True,(255,255,255))
            screen.blit(choose_a_hero,(570,680))
            items = os.listdir(folder_path)

            counter = 0
            row = 0

            icons = []
            
            for i, hero_folder in enumerate(hero_folders):

                hero_data = heroes_data_cards.get(hero_folder)

                x_pos = 20 + counter * 270
                y_pos = 20 + row * 320

                background_card = RectDraw(hero_data['BACKGROUND_C'])
                background_card.update_surf((x_pos, y_pos, 250, 300))

                line_card = RectDraw((50, 50, 50))
                line_card.update_surf((x_pos, y_pos, 250, 300), 5)

                icon = IconDraw(hero_folder, x_pos + 10, y_pos + 10)
                icon.update_surf()
                icons.append(icon)


                instructions = [
                f"Name: {hero_data['name']}",
                f"Health: {hero_data['HP']}",
                f"Damage: x{hero_data['DMG']}",
                f"Defence: x{hero_data['DEF']}",
                f"Rage: x{hero_data['RAGE']}"
            ]
        
                for j, text in enumerate(instructions):
                    rendered = TextDraw(text)
                    rendered.update_surf(x_pos + 13, y_pos + 180 + j * 23)

                counter+=1
                if counter == 4:
                    row+=1
                    counter = 0
                if row >= 3:
                    items.remove(hero_folder)

        



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for icon in icons:
                        if icon.rect.collidepoint(event.pos):
                            selected_hero = icon.filedir
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  
                        selected_hero = None
                        selected.clear()
                    elif event.key == pygame.K_SPACE:
                        if len(selected) == 2:  
                            player1,player2,gameplay,start_anim,choose_menu,gamerun = start_game(gameplay,start_anim,selected,choose_menu,gamerun)

            if selected_hero:
                if not selected_hero in selected:
                    selected.append(selected_hero)
                instruc = font1.render('"Q" - reset "Space" - start',True,(255,255,255))
                screen.blit(instruc, (20, HEIGHT - 65))
                if len(selected) > 1:

                    selection_text = font1.render(f"Selected: {heroes_data_cards[selected[0]]['name']} and {heroes_data_cards[selected[1]]['name']}", True, (255, 255, 0))
                
                else:

                    selection_text = font1.render(f"Selected: {heroes_data_cards[selected[0]]['name']}", True, (255, 255, 0))
                if len(selected) > 2:
                    del selected[2]

                screen.blit(selection_text, (20, HEIGHT - 40))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()
