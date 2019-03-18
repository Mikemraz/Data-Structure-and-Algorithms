"""
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
Note:
bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
"""

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        bottom = [[char] for char in bottom]
        allowed_dict = {}
        for sequence in allowed:
            key = sequence[0] + sequence[1]
            if key in allowed_dict:
                allowed_dict[key] += sequence[2]
            else:
                allowed_dict[key] = sequence[2]

        while len(bottom)>1:
            feasible, upper = self.get_upper_level(bottom, allowed_dict)
            if not feasible:
                return False
            bottom = upper
        return True

    def get_upper_level(self, bottom, allowed_dict):
        upper = []
        feasible = True
        for i in range(len(bottom)-1):
            node_candidates = []
            for m in range(len(bottom[i])):
                for n in range(len(bottom[i+1])):
                    node_candidate = self.find_node(
                        bottom[i][m],bottom[i+1][n],allowed_dict)
                    node_candidates += node_candidate
            node_candidates = list(set(node_candidates))
            if len(node_candidates)==0:
                feasible = False
            upper.append(node_candidates)
        return feasible, upper

    def find_node(self, left, right, allowed_dict):
        node_candidate = []
        key = left + right
        if key in allowed_dict:
            node_candidate = allowed_dict[key]
        else:
            node_candidate = ''
        return node_candidate

if __name__=="__main__":
    solution = Solution()
    result = solution.pyramidTransition("BDBBAA",
["ACB","ACA","AAA","ACD","BCD","BAA","BCB","BCC","BAD","BAB","BAC","CAB","CCD",
"CAA","CCA","CCC","CAD","DAD","DAA","DAC","DCD","DCC","DCA","DDD","BDD","ABB",
"ABC","ABD","BDB","BBD","BBC","BBA","ADD","ADC","ADA","DDC","DDB","DDA","CDA",
"CDD","CBA","CDB","CBD","DBA","DBC","DBD","BDA"])
    print(result)
