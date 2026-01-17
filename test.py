#
#

import pyxel

class App:
  _grid   = 8
  _miss_m = 10
  _cw     = 16
  _width  = 300
  _height = 200

  turn = 0

  player_c = 0
  player_x = 40
  player_y = 80

  miss_max = 6
  miss_f   = []
  miss_x   = []
  miss_y   = []

  def __init__(self):
    for i in range(0, self.miss_max):
      self.miss_f.append(False)
      self.miss_x.append(0)
      self.miss_y.append(0)

    pyxel.init(self._width, self._height, title="test", fps=15)
    pyxel.load("assets/test.pyxres")

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()

    if pyxel.btnp(pyxel.KEY_UP):
      if self.player_y >= self._grid:
        self.player_y -= self._grid
    
    if pyxel.btnp(pyxel.KEY_DOWN):
      if self.player_y <= self._height - self._grid * 2:
        self.player_y += self._grid
    
    if pyxel.btnp(pyxel.KEY_LEFT):
      if self.player_x >= self._grid:
        self.player_x -= self._grid
    
    if pyxel.btnp(pyxel.KEY_RIGHT):
      if self.player_x <= self._width - self._grid * 2:
        self.player_x += self._grid

    # move missile
    for i in range(0, self.miss_max):
      if self.miss_x[i] > self._width:
        self.miss_f[i] = False
      else:
        self.miss_x[i] += self._miss_m

    # Z : fire
    if pyxel.btnp(pyxel.KEY_Z):
      nm = -1
      for i in range(0, self.miss_max):
        if not self.miss_f[i]:
          nm = i
          break
      if nm != -1:
        self.miss_f[nm] = True
        self.miss_x[nm] = self.player_x + self._cw
        self.miss_y[nm] = self.player_y

    # player
    if self.turn % 5 == 0:
      self.player_c = self.player_c ^ 1
    
    self.turn += 1

  def draw(self):
    pyxel.cls(12)

    pyxel.blt(
      self.player_x,
      self.player_y,
      0,
      0 if self.player_c == 0 else 16,
      0,
      16,
      16,
      12,
    )

    for i in range(0, self.miss_max):
      if self.miss_f[i]:
        pyxel.blt(
          self.miss_x[i],
          self.miss_y[i] + 7,
          0,
          38,  #32
          7,   #0
          4,   #16
          2,   #16
          12,
        )
    

App()

