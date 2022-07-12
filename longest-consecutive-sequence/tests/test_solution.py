import pytest
from solution.solution import LongestConsecutiveSequence

def test_list():
  list = [100, 4, 200, 1, 2, 3]
  expected = 4
  instantiate = LongestConsecutiveSequence()
  actual = instantiate.solution(list)
  assert expected == actual


def test_list_negatives():
  list = [-100, -4, -200, -1, -2, -3]
  expected = 4
  instantiate = LongestConsecutiveSequence()
  actual = instantiate.solution(list)
  assert expected == actual
