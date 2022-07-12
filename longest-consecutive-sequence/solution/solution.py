class LongestConsecutiveSequence():
  def __init__(self):
    pass

  def solution(self, nums):
    # [100, 4, 200, 1, 2, 3]
    if nums == []:
      raise ValueError("List must contain at least one numeric value")

    greatest = 1
    for item in nums:
      current = 1 
      while (item + 1) in nums:
        current += 1
        item += 1

      if current > greatest:
        greatest = current
    
    return greatest

