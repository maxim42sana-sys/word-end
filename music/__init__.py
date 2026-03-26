class Trigger:
  def __init__(self, event, mus):
    self.event = event
    self.mus = mus
  def update(self):
    if self.event():
      self.mus.play()
