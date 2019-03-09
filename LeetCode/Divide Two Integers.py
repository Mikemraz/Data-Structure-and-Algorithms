
"""
This implementation has runtime O(logN). The idea is to add divisor to itself
continuously and accelerate computing.
"""
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # determine the sign of final quotient.
        positive = True
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            positive = True
        else:
            positive = False
        dividend, divisor = abs(dividend), abs(divisor)
        # key part of proposed algorithm
        count = 0
        base = 1
        divisor_new = divisor
        while dividend-divisor_new>=0 or base>1:
            if dividend-divisor_new>=0:
                count += base
                dividend = dividend-divisor_new
                divisor_new = divisor_new + divisor_new
                base = base + base
            else:
                divisor_new = divisor
                base = 1
        # check overflow
        if count>2147483647 and positive:
            count = 2147483647
        elif count>2147483648 and not positive:
            count = 2147483648
        return count if positive else -count
