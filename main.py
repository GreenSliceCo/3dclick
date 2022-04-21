from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
money = 0
add = 2
upCost = 100
app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
    def __init__(self, position = (0,0,0), scale = 1, color = color.color(0,0,random.uniform(0.9,1))):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            scale = scale,
            color = color
        )

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            color = color.blue,
            scale = 150,
            double_sided = True)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))

class rig(Button):
    def __init__(self, position = (17, -0.1, 0.3)):
        super().__init__(
            parent = scene,
            position = position,
            origin_y = 0.5,
            model = 'assets/oil.obj',
            color = color.gold,
            scale = 0.03,
            rotation_y = 270,
            rotation_x = 270,
        )
        self.add = 5
    def update(self):
        global money
        money += self.add*time.dt


class clicker(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            position = (8, 1.5, 8),
            scale = 3,
            color = color.gold,
            origin_y = 0.5,
            model = 'cube',
            texture = 'assets/doge.jpg',
        )
    def input(self, key):
        global money,add,level,upCost
        if self.hovered:
            if key == 'left mouse down':
                money += add
            if key == 'u' and money >= upCost:
                money -= upCost
                upCost = int(upCost*1.5)
                add = int(add*1.5)
        if money >= upCost:
            levelText.color = color.green
        else:
            levelText.color = color.red
player = FirstPersonController()
screenMoney = Text(text = f"${money}", x = -0.85, y = 0.47)
levelText = Text(text = f"Money/click: {add}", x = -0.85, y = 0.42)
def update():
    screenMoney.text = f"${format(money, ',.2f')}"
    levelText.text = f"Money/click: {add}"
sky = Sky()
dollars = clicker()
test = rig()
app.run()