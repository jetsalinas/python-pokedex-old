import pyglet as p
from pyglet.window import key

#initial stuff
p.resource.path = ['Assets']
p.resource.reindex()
#w = p.window.Window(caption='PK')
w = p.window.Window(caption='PK', width=800, height=600)
c = {"red"   : (255, 0, 0),   
     "green" : (0, 255, 0),
     "blue"  : (0, 0, 255),
     "yellow": (255, 255, 0),
     "purple": (255, 0, 255),
     "orange": (255, 165, 0),
     "white" : (255, 255, 255),
     "black" : (0, 0, 0),
     "brown" : (153, 76, 0),
     "grey"  : (100, 100, 100)}
f = '8bitwondernominal'
k = {key.LEFT:False, key.RIGHT:False, key.UP:False, key.DOWN:False}

l = (1, 151)                                   #m max value
m = 1                                          #current pkmn
o = [4, 0, 0, 0, 0]                            #0tab, 1bg, 2skin, 3menu
n = [(1, len(o)-1), (0, 15), (0, 3), (0, 3)]   #o max values
ls = p.graphics.Batch()  #left of screen
rs = p.graphics.Batch()  #right of screen


test = {  1: ['Bulbasaur',  False],
          2: ['Ivysaur',    False],
          3: ['Venusaur',   False],
          4: ['Charmander', False],
          5: ['Charmeleon', False],
          6: ['Charizard',  False],
          7: ['Squirtle',   False],
          8: ['Wartortle',  False],
          9: ['Blastoise',  False],
        147: ['Dratini',    False],
        148: ['Dragonair',  False],
        149: ['Dragonite',  False],
        150: ['Mewtwo',     False],
        151: ['Mew',        False]}

#shortcut functions
def i_img(x, y): return p.image.load('Assets\\{}\\{}.png'.format(x, str(y)))
def i_key(x, y=l):
    if y[0]==0:
        if   x>y[1]: return x-y[1]-1
        elif x<y[0]: return x+y[1]+1
        else:        return x
    else:
        if   x>y[1]: return x-y[1]
        elif x<y[0]: return x+y[1]
        else:        return x
def i_lab(t, x, y, bt=ls): return p.text.Label(text=t, x=x, y=y, batch=bt)
def i_num(x):
    if len(str(x))<3: return '0'*(3-len(str(x)))+str(x)
    else: return str(x)
def i_sel(x): return '{}     {}'.format(i_num(i_key(x)), test[i_key(x)][0])
def i_spr(x, y, bt=ls): return p.sprite.Sprite(i_img(x, y), batch=bt)

#assets
bk = i_spr('BK', o[1])
#sk = i_spr('SK\\{}'.format(o[2]))
#mk = i_spr('MK\\{}'.format(o[3]))
pk = i_spr('PK', i_num(m), rs)
p0 = i_lab(i_sel(m-2), 300, 280, rs)
p1 = i_lab(i_sel(m-1), 300, 260, rs)
p2 = i_lab(i_sel(m),   300, 240, rs)
p3 = i_lab(i_sel(m+1), 300, 220, rs)
p4 = i_lab(i_sel(m+2), 300, 200, rs)
temp = p.text.Label(text=str(o[0]), x=20, y=20)
ak = [bk]#, sk, mk]

#sprite settings
for i in ak: i.scale = w.width/i.width  #if yes, all images must be w.wxw.h res
pk.x, pk.y = w.width/2, w.height/2

#pyglet functions
def update(dt):
    bk.image = i_img('BK', o[1])
    #mk.image = i_img('MK', o[2])
    #sk.image = i_img('SK', o[3])
    pk.image = i_img('PK', i_num(m))
    p0.text = i_sel(m-2)
    p1.text = i_sel(m-1)
    p2.text = i_sel(m)
    p3.text = i_sel(m+1)
    p4.text = i_sel(m+2)
    temp.text = str(o[0])
@w.event
def on_key_press(t, mod):
    global m
    if   t==key.UP   : m = i_key(m-1)
    elif t==key.DOWN : m = i_key(m+1)
    if   t==key.TAB  : o[0] = i_key(o[0]+1, n[0])
    if   t==key.RIGHT and o[0]!=4: o[o[0]] = i_key(o[o[0]]+1, n[o[0]])
    elif t==key.LEFT  and o[0]!=4: o[o[0]] = i_key(o[o[0]]-1, n[o[0]])
@w.event
def on_mouse_scroll(x, y, s_x, s_y):
    global m
    m = i_key(m-int(s_y))
@w.event
def on_draw():
    w.clear()
    ls.draw()
    rs.draw()
    temp.draw()
    
if __name__ == '__main__':
    p.clock.schedule_interval(update, 1/120.0)
    p.app.run()
