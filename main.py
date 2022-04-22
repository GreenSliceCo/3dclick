from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
money = 0
app = Ursina()
monitor = ["polygon", "dogecoin", "NEAR Protocol", "Cronos", "Cosmos", "Leo",
           "Algorand", "Decentraland", "Stellar", "PancakeSwap",
           "WEMIX TOKEN", "SENSO", "The Sandbox", "Magic Internet Money"]
site = "https://coinranking.com/"
window.fps_counter.enabled = False
window.exit_button.visible = False


class Voxel(Button):
    def __init__(self, position = (0,0,0), scale = 1, base = color.color(0,0,random.uniform(0.9,1))):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            highlight_color = color.lime,
            scale = scale,
            color = base
        )
    def input(self, key):
        if self.hovered:
            global factory, money
            if key == 'left mouse down' and money >= 5_000:
                factory = rig(position = self.position)
                money -= 5_000

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
            color = color.grey,
            scale = 0.03,
            rotation_y = 270,
            rotation_x = 270,
        )
        self.add = 5
    def update(self):
        global money
        money += self.add*time.dt


class clicker(Button):
    def __init__(self, position = (8, 1.5, 8), add = 0.14, color = color.gold):
        super().__init__(
            parent = scene,
            position = position,
            scale = 3,
            color = color,
            origin_y = 0.5,
            model = 'cube',
            texture = 'assets/doge.jpg',
        )
        self.add = add
    def input(self, key):
        global money
        add = self.add
        if self.hovered:
            if key == 'left mouse down':
                money += add
            if key == 'u' and money >= 10:
                pass
        # if money >= upCost:
        #     levelText.color = color.green
        # else:
        #     levelText.color = color.red
displayDollars = Text(text = f"${money}", x = -0.85, y = 0.47)
# levelText = Text(text = f"Money/click: {dollars.add}", x = -0.85, y = 0.42)
def update():
    displayDollars.text = f"${format(money, ',.2f')}"
#     levelText.text = f"Money/click: {dollars.add}"
player = FirstPersonController()
dollars = clicker()
sky = Sky()
app.run()