from collections import defaultdict as ddict

class Trigger:
  events = ddict(str)
  def __init__(self, key, event, mus, *args):
    self.key = key
    self.event = event
    self.mus = mus
    self.args = args
  def update(self):
    if self.events[self.key] == self.event:
      self.mus.play(*self.args)
