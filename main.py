import os
import sys
import pygame
import math
from pygame.locals import *
from pygame import Surface, Vector2
from achievements import Achievement, achievements

egg = False


def asset(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "assets", relative_path)


def findAchBin(dir=os.getcwd(), target="Achievements.bin"):
    while True:
        achBin = os.path.join(dir, target)
        if os.path.isfile(achBin):
            return achBin
        parent = os.path.dirname(dir)
        if parent == dir:
            return None
        dir = parent


def checkAch():
    global egg
    achBin = findAchBin()
    eggCount = 0
    if not achBin:
        for ach in achievements:
            ach.unlocked = False
        return
    with open(achBin, "r") as file:
        pos = 0
        for ach in achievements:
            file.seek(pos)
            byte = file.read(1)
            ach.unlocked = True  # byte != '\x00'
            if ach.unlocked:
                eggCount += 1
            pos += 4
    egg = eggCount == 18


def Sin512(v): return math.floor(math.sin(v / 256 * math.pi) * 512)
def Cos512(v): return math.floor(math.cos(v / 256 * math.pi) * 512)
def Sin256(v): return Sin512(v * 2) >> 1
def Cos256(v): return Cos512(v * 2) >> 1


def renderBG(screen: Surface):
    colors = eggColors
    screen.fill(colors[0])

    def circle(screen: Surface, c: int, radius: float, drawPos: Vector2):
        center = Vector2(screen.get_size()) / 2
        pygame.draw.circle(screen, colors[c], center, radius, 8)
        pygame.draw.circle(screen, colors[c], drawPos + center, 32)
        pygame.draw.circle(screen, colors[c], center - drawPos, 16)
        pygame.draw.circle(screen, colors[0], drawPos + center, 26)

    radius = (Sin512(timer) >> 3) + 116
    drawPos = Vector2((radius - 4) * Sin256(timer) >> 8,
                      (radius - 4) * Cos256(timer) >> 8)
    circle(screen, 1, radius, drawPos)

    radius = ((Cos512(timer) >> 3) + 148)
    drawPos = Vector2((radius - 4) * Cos256(timer) >> 8,
                      (radius - 4) * Sin256(timer) >> 8)
    circle(screen, 2, radius, drawPos)


def drawText(surface: Surface, text: str, color, rect) -> int:
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -3
    fontHeight = font.size("Tg")[1]
    while text:
        i = 1
        if y + fontHeight > rect.bottom:
            break
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1
        image = font.render(text[:i], False, color)
        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing
        text = text[i:]
    return y


def drawAchievement(ach: Achievement, x: int, y: int):
    width = 200
    unlocked = ach.unlocked
    desc = ach.desc2 if unlocked else ach.desc

    screen.blit(ach.image if unlocked and ach.image else achLocked, (x, y))

    textA = Surface((width, 50), SRCALPHA)
    color = "#00a000" if unlocked else "#ad0000"
    yOffset = drawText(textA, ach.name, color, Rect(0, 0, width, 50)) + 5
    ySize = yOffset

    textB = Surface((width, 50), SRCALPHA)
    ySize += drawText(textB, desc, "#FFFFFF", Rect(0, 0, width, 50))

    shadow = Surface((width, 50), SRCALPHA)
    drawText(shadow, desc, "#484868", Rect(0, 0, width, 50))

    y += 30 - (ySize // 2)
    screen.blit(textA, (x+70, y))
    screen.blit(shadow, (x+71, y+yOffset+1))
    screen.blit(textB, (x+70, y+yOffset))


# pygame setup
pygame.init()
pygame.display.set_icon(pygame.image.load(asset("icon.png")))
pygame.display.set_caption("Mania Achievements")
screen = pygame.display.set_mode((848, 480))
clock = pygame.time.Clock()
running = True
bgColors = ["#F0C800", "#F08C18", "#80A0B0"]
eggColors = ["#4ad29c", "#f79219", "#3ab2ce"]
timer = 0

header = pygame.image.load(asset("header.png")).convert_alpha()
font = pygame.font.Font(asset("mania.ttf"), 14)

achLocked = pygame.image.load(asset("LOCKED.jpg")).convert()
for ach in achievements:
    ach.image = pygame.image.load(asset(ach.id + ".jpg")).convert()
checkAch()

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.load(asset("MainMenu.ogg"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.set_endevent(MUSIC_END)
pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            pygame.mixer.music.play(0, 202752 / 44100)
        if event.type == pygame.QUIT:
            running = False

    timer += 1
    if timer % (60*10) == 0:
        checkAch()

    if pygame.key.get_focused():
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

    bg = Surface(Vector2(screen.get_size()) / 2)
    renderBG(bg)
    bg.blit(header, ((bg.get_width() - header.get_width()) / 2, 2))  # 12
    bg = pygame.transform.scale_by(bg, 2)
    screen.blit(bg, (0, 0))

    for i in range(1, 19):
        x = 10 + ((i - 1) // 6) * 280
        y = 93 + ((i - 1) % 6) * 64
        drawAchievement(achievements[i - 1], x, y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
