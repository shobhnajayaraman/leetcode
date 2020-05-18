    def reverse(self, x: int) -> int:
        result = 0
        absofx = abs(x)
        while absofx != 0 :
            remainder = absofx % 10 
            absofx = absofx //10
            temp = result * 10 + remainder
            result = temp
        if x < 0 :
            result = -1 * result
        if result < - 2**31 or result > 2**31 -1:
            result = 0    
        return result