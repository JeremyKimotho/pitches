import unittest
from app.models import Pitch
from datetime import datetime

class PitchTest(unittest.TestCase):

  def setUp(self):
    
    self.new_pitch = Pitch(1234, 'test', 'test', 'test', 'test', datetime.now(), 0, 0)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_pitch, Pitch))

