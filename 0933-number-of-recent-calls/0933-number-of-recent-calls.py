class RecentCounter(object):

    def __init__(self):
        self.request = [] # an empty list
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.request.append(t)

        while self.request[0] < t - 3000:
            self.request.pop(0)

        return len(self.request)





        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)