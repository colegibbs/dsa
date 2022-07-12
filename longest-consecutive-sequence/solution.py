class longest_consecutive_sequence():
  def __init__(self):
    pass

  def solution(self, nums):
    current = 1 
    greatest = 1

    for item in nums:
      while (item + 1) in nums:
        current += 1
        item += 1

      if current > greatest:
        greatest = current
    
    return greatest

