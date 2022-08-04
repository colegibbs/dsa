class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        odd = bool(total_length % 2)
        total_array = []
        i = j = 0
        while len(total_array) - 1 != total_length - 1:
            if nums1 == []:
                total_array = nums2
                break
            elif nums2 == []:
                total_array = nums1
                break
            
            if nums1[i] > nums2[j]:
                total_array.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                total_array.append(nums1[i])
                i += 1
            elif nums1[i] == nums2 [j]:
                total_array.extend([nums1[i], nums2[j]])
                j += 1
                i += 1
                
            if i > len(nums1) - 1:
                total_array = total_array + nums2[j:]
                break
            elif j > len(nums2) - 1:
                total_array = total_array + nums1[i:]
                break
        print("total array", total_array)
        if odd:
            median = total_array[(len(total_array) - 1) / 2]
        else:
            mid1 = total_array[(len(total_array) - 1) // 2]
            mid2 = total_array[(len(total_array)) // 2]
            x = float(mid1 + mid2)
            median = (x / 2)
        return median
        