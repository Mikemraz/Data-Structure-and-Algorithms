class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if len(L)==0:
            return 0
        length_start = 1
        length_end = max(L)
        final_length = 0
        while length_end-length_start>1:
            length_mid = (length_end-length_start)//2 + length_start
            pieces = self.get_pieces(length_mid, L)
            if pieces==k:
                length_start = length_mid
                final_length = length_mid
            elif pieces<k:
                length_end = length_mid
            else:
                length_start = length_mid
        if self.get_pieces(length_start, L)>=k:
            final_length = length_start
        if self.get_pieces(length_end, L)>=k:
            final_length = length_end
        return final_length

    def get_pieces(self, length, L):
        pieces = 0
        for wood in L:
            pieces += wood//length
        return pieces
