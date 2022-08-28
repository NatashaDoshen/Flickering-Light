
class Light:

  def __init__(self, sync=None): # new - tuple
    super().__init__()
    self.on = False
    self.sync = sync

  def is_on(self):
    return self.on

  def toggle(self):
    self.on = not self.on
    if self.sync is not None:
      self.sync.toggle()


light1 = Light()
light2 = Light(sync=light1)

print(light1.is_on())
light2.toggle()
print(light1.is_on())
class Light:

  def __init__(self, sync=None): # new - tuple
    self.on = False
    self.sync = sync

  def is_on(self):
    return self.on

  def toggle(self):
    self.on = not self.on
    if self.sync is not None:
      self.sync.toggle()


light1 = Light()
light2 = Light(sync=light1)

print(light1.is_on())
light2.toggle()
print(light1.is_on())

class OldLight(Light):

  def __init__(self, sync = None):
    super().__init__(sync = sync)
    self.on = False
    self.sync = sync
    self.flicker = False
      
  def toggle(self):
    super().toggle()
    if self.on:
      self.flicker = not self.flicker
