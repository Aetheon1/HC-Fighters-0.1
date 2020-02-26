# noinspection PyUnresolvedReferences
import pgzrun, random, pygame

WIDTH = 1200

HEIGHT = 620

music.play('default')

cat = Actor('idle')
cat.x = 600
cat.y = 570

cat_icon = Actor('idle')

sans = Actor('sans_idle')
sans.x = 350
sans.y = 150

kirby = Actor('kirby_idle')
kirby.x = 550
kirby.y = 150
kirb = False
dj = 0

shrek = Actor('shrek_idle')
shrek.x = 750
shrek.y = 150
c_shrek = False
is_boost = False
boost = 1000
boost_end = 1500

knuckles = Actor('knuckles_idle')
knuckles.x = 950
knuckles.y = 150

fish = Actor('fish')
store = []

ak_47 = Actor('ak_47')
guns = []


#start screen var
start_screen = True
#if we want to run out main game code
run = False
#character select screen
character_menu = False
#music select screen
music_screen = False


state = 0

reset = 0

state_images = [
    "right",
    "left"
]

#varibales that deal with player movement
isJump = False
jumpCount = 10
left = False
right = True
vel = 10
#variables for the fish
fall = 5
time_delay = 1000
#whether to drop a fish or not
drop = False
#start of fish drop
start = True
#players score
score = 0
#amount of player lives
lives = 5
#checks to end the game
end_game = False

boss_fight = False

title = 'cat hopper'
#start button
start_button = Actor('start')
start_button.x = 600
start_button.y = 240

#go again button
cont_button = Actor('again')
cont_button.x = 600
cont_button.y = 100

#characters button
character_select = Actor('characters')
character_select.x = 600
character_select.y = 300

#back button
back = Actor('back')
back.x = 100
back.y = 40

#music_button
music_button = Actor('music')
music_button.x = 600
music_button.y = 360

#button
default_music = Actor('default')
default_music.x = 150
default_music.y = 250

#button
all_star = Actor('all_star')
all_star.x = 150
all_star.y = 300

def place_fish():
    fish.x = random.randint(50, 1150)

def on_mouse_down(pos):
    global run, start_screen, lives, vel, end_game, score, fall, start, character_menu, sans, \
        cat, state_images, kirb, music_screen, c_shrek

    if start_button.collidepoint(pos):
        run = True
        start_screen = False

    if cont_button.collidepoint(pos):
        run = False
        start_screen = True
        lives = 5
        vel = 10
        end_game = False
        score = 0
        fall = 5
        start = True


    if character_select.collidepoint(pos):
        music.play('epic')
        run = False
        start_screen = False
        music_screen = False
        character_menu = True

    if music_button.collidepoint(pos):
        run = False
        start_screen = False
        character_menu = False
        music_screen = True

    if default_music.collidepoint(pos):
        music.play('default')
    if all_star.collidepoint(pos):
        music.play('smash')

    if cat_icon.collidepoint(pos):
        cat = Actor('idle')
        state_images = [
            "right",
            "left"
        ]
        kirb = False
        c_shrek = False

    if sans.collidepoint(pos):
        cat = Actor('sans_idle')
        state_images = [
            "sans_left",
            "sans_right"
        ]
        kirb = False
        c_shrek = False

    if kirby.collidepoint(pos):
        cat = Actor('kirby_idle')
        state_images = [
            "kirby_right",
            "kirby_left"
        ]
        kirb = True
        c_shrek = False

    if shrek.collidepoint(pos):
        cat = Actor('shrek_idle')
        state_images = [
            "shrek_right",
            "shrek_left"
        ]
        kirb = False
        c_shrek = True

    if knuckles.collidepoint(pos):
        cat = Actor("knuckles_idle")
        state_images =[
            "knuckles_right",
            "knuckles_left"
        ]
        kirb = False
        c_shrek = False

    if back.collidepoint(pos):
        music.play('default')
        start_screen = True
        character_menu = False
        music_screen = False

def draw():
    if start_screen:
        screen.clear()
        screen.blit('menu_backdrop', (0,0))
        screen.blit(title, (0, 0))
        cat.x = 600
        cat.y = 570
        cat.draw()
        start_button.draw()
        character_select.draw()
        music_button.draw()

    if character_menu:
        cat_icon.x = 150
        cat_icon.y = 150
        screen.clear()
        screen.blit('menu_backdrop', (0, 0))
        back.draw()

        cat_icon.draw()
        sans.draw()
        kirby.draw()
        shrek.draw()
        knuckles.draw()

    if music_screen:
        screen.clear()
        screen.blit('menu_backdrop', (0, 0))
        back.draw()

        default_music.draw()
        all_star.draw()

    if run:
        screen.clear()

        screen.blit('forest', (0, -55))

        cat.image = state_images[state]
        cat.draw()

        for i in range(0, len(store)):
            store[i].draw()

        screen.draw.text("Score: " + str(score), (15, 5))
        screen.draw.text("Lives: " + str(lives), (1020, 5))

        if end_game:
            screen.draw.text("YOU SUCK!!!", (540, 310))
            cont_button.draw()

    #if boss_fight:
        #screen.clear()
        #screen.blit('forest', (0, -55))

        #for i in range(0, len(store)):
            #guns[i].draw()

        #cat.image = state_images[state]
        #cat.draw()


def update():
    global state, neg, jumpCount, isJump, vel, left, right, reset, jumpReady, time_delay, drop, start, score, \
        fall, lives, end_game, boost, is_boost, boost_end, boss_fight, cat, run, state_images, store
#play music

#move right
    if run:
        if keyboard.d and cat.x < 1140:
            state = 0
            cat.x += vel
            right = True
            left = False
    #move left
        if keyboard.a and cat.x > 50:
            state = 1
            cat.x -= vel
            right = False
            left = True
    #jump code
        if not kirb:
            if not c_shrek:
                if not(isJump) and pygame.time.get_ticks() - reset > 500:
                    if keyboard.SPACE:
                        isJump = True
                        right = False
                        left = False
                        jump = True
                        vel = 15
                        reset = pygame.time.get_ticks()
                if isJump:
                    if jumpCount >= -10:
                        neg = 1
                        if jumpCount < 0:
                            neg = -1
                        cat.y -= (0.7*jumpCount ** 2) * 0.9 * neg
                        jumpCount -= 1
                    else:
                        isJump = False
                        vel = 10
                        jumpCount = 10

    #Fish spawner
        if start:
            store.append(fish)
            place_fish()
            drop = True
            start = False
        if drop:
            fish.y += fall
    #Getting rid of fish if they hit screen border
        if not c_shrek:
            if fish.y > 620:
                store.pop(0)
                drop = False
                start = True
                fish.y = 0
                lives = lives-1
                sounds.miss.play()
    #Hit detection for Fish and Cat
        for i in range(len(store)):
            if cat.colliderect(store[i]):
                store.pop()
                drop = False
                start = True
                fish.y = 0
                score = score+1
    #Cat Lives
        if lives == 0:
            start = False
            drop = False
            end_game = True

        if not c_shrek:
            if score > 10:
                fall = 6
            if score > 20:
                fall = 7.5
            if score > 30:
                fall = 8
            if score > 40:
                fall = 9
                vel = 11.5
            if score > 50:
                fall = 10
                vel = 13.5

        if kirb:
            if pygame.time.get_ticks() - reset > 10:
                if keyboard.SPACE:
                    isJump = True
                    right = False
                    left = False
                    jump = True
                    vel = 15
                    reset = pygame.time.get_ticks()
            if isJump:
                if jumpCount >= -10:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                    cat.y -= (0.5*jumpCount ** 2) * 1 * neg
                    jumpCount -= 1
                else:
                    isJump = False
                    vel = 10
                    jumpCount = 10

        if c_shrek:

            if fish.y > 620:
                store.pop(0)
                drop = False
                start = True
                fish.y = 0
                lives = lives - 1
                sounds.shrek_yell.play()

            if not(isJump) and pygame.time.get_ticks() - reset > 1000:
                if keyboard.SPACE:
                    isJump = True
                    right = False
                    left = False
                    jump = True
                    vel = 28
                    reset = pygame.time.get_ticks()
            if isJump:
                if jumpCount >= -10:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                    cat.y -= (1*jumpCount ** 2) * 0.7 * neg
                    jumpCount -= 1
                else:
                    isJump = False
                    vel = 10
                    jumpCount = 10

            if score > 10:
                fall = 6
            if score > 20:
                fall = 7.5
            if score > 30:
                fall = 8
            if score > 40:
                fall = 9
            if score > 50:
                fall = 10

    #if score > 150:
        #boss_fight = True

    #if boss_fight:
       # ak_47.x = 600
        #ak_47.y = 570
        #run = False
        #guns.append(ak_47)
        #if keyboard.d and cat.x < 1140:
            #state = 0
            #cat.x += vel
            #right = True
            #left = False
# move left
        #if keyboard.a and cat.x > 50:
            #state = 1
            #cat.x -= vel
            #right = False
            #left = True

        #if cat.colliderect(ak_47):
            #cat = Actor('ak_47_cat')
            #state_images = [
                #"ak_47_cat_left",
                #"ak_47_cat_right"]
            #guns.pop(0)



pgzrun.go()












