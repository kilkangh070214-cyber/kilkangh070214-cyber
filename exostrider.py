
import turtle
import random
import math

# ==========================================
# ASTRALIS : CYBER CELESTIAL
# Futuristic Geometric Art
# ==========================================

screen = turtle.Screen()
screen.setup(1200, 800)
screen.bgcolor("#030817")
screen.title("ASTRALIS - Cyber Celestial")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

random.seed(42)

# --------------------------
# 기본 도형 함수
# --------------------------

def polygon(points, color, outline=None, width=1):
    t.penup()
    t.goto(points[0])
    t.pensize(width)
    t.pencolor(outline if outline else color)
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()

    for p in points[1:]:
        t.goto(p)

    t.goto(points[0])
    t.end_fill()
    t.penup()


def line(points, color, width=1):
    t.penup()
    t.goto(points[0])
    t.pencolor(color)
    t.pensize(width)
    t.pendown()

    for p in points[1:]:
        t.goto(p)

    t.penup()


def circle(x, y, radius, color, width=1):
    t.penup()
    t.goto(x, y-radius)
    t.pencolor(color)
    t.pensize(width)
    t.setheading(0)
    t.pendown()
    t.circle(radius)
    t.penup()


def star(x, y, size, color):
    points = []

    for i in range(10):
        angle = math.radians(i * 36 - 90)
        r = size if i % 2 == 0 else size * 0.4
        points.append((
            x + math.cos(angle)*r,
            y + math.sin(angle)*r
        ))

    polygon(points, color)


def glow(x, y, size, color):
    circle(x, y, size, color, 1)
    circle(x, y, size*0.65, color, 2)

    line([
        (x-size*1.5, y),
        (x+size*1.5, y)
    ], color, 1)

    line([
        (x, y-size*1.5),
        (x, y+size*1.5)
    ], color, 1)


def mirror(points, direction):
    return [(x*direction, y) for x, y in points]


# --------------------------
# 1. 우주 배경
# --------------------------

for i in range(180):
    x = random.randint(-580, 580)
    y = random.randint(-370, 370)
    size = random.uniform(1, 2.5)

    color = random.choice([
        "#426B91", "#729BBE",
        "#B5DFFF", "#254A70"
    ])

    t.penup()
    t.goto(x, y)
    t.dot(size, color)

# 별자리
for i in range(12):
    x = random.randint(-520, 520)
    y = random.randint(-320, 320)

    star(x, y, random.randint(3, 7), "#A9EFFF")

# --------------------------
# 2. 우주 마법진
# --------------------------

for r in [75, 90, 115, 145, 165, 190, 220]:
    circle(0, 0, r, "#14516D", 1)

for i in range(36):
    angle = math.radians(i*10)

    x1 = math.cos(angle)*165
    y1 = math.sin(angle)*165

    x2 = math.cos(angle)*190
    y2 = math.sin(angle)*190

    line([(x1, y1), (x2, y2)], "#38BBD0", 1)

for i in range(12):
    angle = math.radians(i*30)

    x = math.cos(angle)*220
    y = math.sin(angle)*220

    star(x, y, 8, "#52DFFF")

# 중앙 마법진 기하학
polygon([
    (0, 190), (165, 0),
    (0, -190), (-165, 0)
], "#09283D", "#37B9D6", 2)

polygon([
    (0, 140), (120, 0),
    (0, -140), (-120, 0)
], "#061A30", "#55E5F5", 2)

# --------------------------
# 3. 에너지 날개
# --------------------------

wing = [
    (35, 100),
    (110, 175),
    (245, 255),
    (350, 280),
    (295, 210),
    (390, 220),
    (315, 150),
    (430, 145),
    (330, 90),
    (390, 30),
    (255, 65),
    (170, 35),
    (70, 45)
]

for direction in [-1, 1]:
    points = mirror(wing, direction)

    polygon(points, "#102D48", "#42D8F1", 2)

    # 날개 내부의 기계 구조
    feather = [
        (45, 105), (120, 170),
        (255, 240), (175, 125),
        (75, 55)
    ]

    polygon(
        mirror(feather, direction),
        "#174B67",
        "#68E8FF",
        1
    )

    for i in range(5):
        x = 90 + i*48
        y = 105 + i*23

        line(
            mirror([
                (x, y),
                (x+65, y+45)
            ], direction),
            "#7CEBFF",
            2
        )

    # 날개 끝 장식
    glow(direction*350, 220, 12, "#43E9FF")

# --------------------------
# 4. 날개 에너지 라인
# --------------------------

for direction in [-1, 1]:
    for i in range(8):
        y = 45 + i*24

        line(
            mirror([
                (45, y),
                (130, y+35),
                (230, y+65),
                (330, y+75)
            ], direction),
            "#39AFCF",
            1
        )

# --------------------------
# 5. 중앙 갑옷 - 다리
# --------------------------

for direction in [-1, 1]:

    leg = [
        (direction*15, -55),
        (direction*65, -100),
        (direction*95, -195),
        (direction*65, -245),
        (direction*35, -220),
        (direction*25, -145)
    ]

    polygon(leg, "#A9C7D8", "#E6F7FF", 2)

    knee = [
        (direction*25, -125),
        (direction*75, -115),
        (direction*90, -155),
        (direction*40, -170)
    ]

    polygon(knee, "#365B78", "#8BEAFF", 2)

    boot = [
        (direction*35, -215),
        (direction*75, -225),
        (direction*110, -270),
        (direction*30, -255)
    ]

    polygon(boot, "#D5E6ED", "#65DFFF", 2)

    line(
        mirror([(40, -230), (80, -245), (100, -260)], direction),
        "#45D8F3",
        3
    )

# --------------------------
# 6. 몸통 갑옷
# --------------------------

torso = [
    (-65, 100),
    (-35, 135),
    (0, 150),
    (35, 135),
    (65, 100),
    (48, 20),
    (0, -65),
    (-48, 20)
]

polygon(torso, "#B7D1E0", "#EAFBFF", 3)

# 갑옷 외부 패널
for direction in [-1, 1]:

    armor = [
        (direction*40, 100),
        (direction*75, 75),
        (direction*60, 15),
        (direction*15, -35),
        (direction*25, 45)
    ]

    polygon(armor, "#557D99", "#A7F0FF", 2)

    line(
        mirror([
            (40, 95),
            (55, 60),
            (45, 25)
        ], direction),
        "#E4FFFF",
        3
    )

# --------------------------
# 7. 가슴 코어
# --------------------------

polygon([
    (0, 115),
    (35, 75),
    (0, 20),
    (-35, 75)
], "#123F5D", "#5CEAFF", 3)

polygon([
    (0, 105),
    (20, 75),
    (0, 45),
    (-20, 75)
], "#66EDFF", "#D7FFFF", 2)

glow(0, 75, 17, "#70F6FF")

# 가슴 장식
for direction in [-1, 1]:
    line(
        mirror([
            (25, 70),
            (50, 40),
            (25, 10)
        ], direction),
        "#45D8FF",
        2
    )

# --------------------------
# 8. 어깨 갑옷
# --------------------------

for direction in [-1, 1]:

    shoulder = [
        (direction*45, 105),
        (direction*90, 145),
        (direction*145, 120),
        (direction*110, 65),
        (direction*60, 55)
    ]

    polygon(shoulder, "#D1E5EF", "#F1FFFF", 2)

    polygon(
        mirror([
            (75, 115),
            (100, 125),
            (115, 90),
            (80, 75)
        ], direction),
        "#39708D",
        "#6BE6FF",
        2
    )

    glow(direction*105, 100, 9, "#4FEAFF")

# --------------------------
# 9. 머리와 투구
# --------------------------

polygon([
    (-35, 145),
    (-28, 190),
    (0, 225),
    (28, 190),
    (35, 145),
    (0, 125)
], "#C9E3EF", "#F3FFFF", 3)

# 투구의 중앙 장식
polygon([
    (0, 235),
    (15, 190),
    (0, 155),
    (-15, 190)
], "#426D91", "#9CF4FF", 2)

# 눈 부분
polygon([
    (-25, 180),
    (-5, 172),
    (0, 180),
    (-15, 185)
], "#32EFFF")

polygon([
    (25, 180),
    (5, 172),
    (0, 180),
    (15, 185)
], "#32EFFF")

# 머리 장식
polygon([
    (0, 225),
    (-12, 270),
    (0, 250),
    (12, 270)
], "#E5F7FF", "#65E7FF", 2)

# --------------------------
# 10. 에너지 검
# --------------------------

blade = [
    (-40, -20),
    (-270, -230),
    (-315, -285),
    (-290, -220),
    (-25, 5)
]

polygon(blade, "#62E9FF", "#C5FFFF", 2)

line([
    (-40, -20),
    (-290, -260)
], "#FFFFFF", 3)

# 검 손잡이
line([
    (-25, 5),
    (5, 35)
], "#D8F8FF", 7)

line([
    (-40, -5),
    (-5, 30)
], "#38DFFF", 3)

# 검 에너지 파동
for i in range(5):
    offset = i*12

    line([
        (-50-offset, -30),
        (-170-offset, -150),
        (-270-offset, -220)
    ], "#36C9FF", 1)

# --------------------------
# 11. 주변 에너지 파티클
# --------------------------

for i in range(40):
    x = random.randint(-500, 500)
    y = random.randint(-330, 330)

    if abs(x) > 220 or abs(y) > 250:
        size = random.randint(2, 6)
        t.penup()
        t.goto(x, y)
        t.dot(size, "#4AC9F5")

# --------------------------
# 12. 최종 장식
# --------------------------

for direction in [-1, 1]:

    # 좌우 외곽 장식
    line(
        mirror([
            (180, -100),
            (260, -180),
            (350, -200)
        ], direction),
        "#35CBEF",
        2
    )

    star(direction*400, -180, 13, "#67E9FF")
    star(direction*280, 300, 10, "#A7F7FF")

# 하단 타이틀
t.penup()
t.goto(0, -345)
t.pencolor("#8DEEFF")
t.write(
    "A S T R A L I S",
    align="center",
    font=("Arial", 25, "bold")
)

t.goto(0, -375)
t.pencolor("#477EAA")
t.write(
    "CYBER CELESTIAL  /  GEOMETRIC ART",
    align="center",
    font=("Arial", 10, "normal")
)

# 완료
screen.update()
turtle.done()
