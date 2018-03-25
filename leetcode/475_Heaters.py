class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        # each house should be heated by the closest heater, for which there are 2 candidates
        # i is idx of closest heater on the left; i+1 is closest heater on the right
        radius = -1
        i = 0

        houses.sort()
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]

        for house in houses:
            while house > heaters[i + 1]:
                i += 1
            reqd_radius = min(house - heaters[i], heaters[i+1] - house)
            radius = max(radius, reqd_radius)
        return radius

