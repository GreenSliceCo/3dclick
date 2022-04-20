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

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position = self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)

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
    screenMoney.text = f"${money}"
    levelText.text = f"Money/click: {add}"
sky = Sky()
dollars = clicker()
app.run()