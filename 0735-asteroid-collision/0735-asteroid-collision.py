class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [] # store the remaining ones after collision

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]: # they are moving towards each other
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack

        

                

            









        