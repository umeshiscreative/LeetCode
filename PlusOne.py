class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        op = ''
        for i in digits:
            op += str(i)
        
        res = int(op) + 1
    
        back = []
        for i in str(res):
            back.append(int(i))
        
        return back
