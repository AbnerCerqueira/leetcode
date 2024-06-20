# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    # minha primeira solução
    def reverse(self, x) :
        x = list(str(x))
        if len(x) == 1:
            return int(x[0])
        
        res = []
        menos = ''

        for i in range(len(x) - 1, -1, -1): # loop da direita para esquerda
            if x[i] != '-':
                res.append(x[i])
            if x[i] == '-':
                menos = x[i]

        if '-' in menos: # adicionar no inicio
            res.append('')
            for i in range(len(res)- 1, -1, -1):
                res[i] = res[i - 1]
            res[0] = menos

        res = int(''.join((map(str, res))))
        return 0 if res < -2 ** 31 or res > 2 ** 31 - 1 else res
    # segunda solução
    def reverse2(self, x) :
        x = list(str(x))

        if len(x) == 1:
            return int(x[0])
        
        res = x[::-1] # slicing

        if res[-1] == '-':
            for i in range(len(res)- 1, -1, -1):
                res[i] = res[i - 1]
            res[0] = '-'

        res = int(''.join((map(str, res))))
        return 0 if res < -2 ** 31 or res > 2 ** 31 - 1 else res
    
if __name__ == "__main__":
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(901000))
