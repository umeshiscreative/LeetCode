class Solution(object):
    def binaryToDecimal(self, num):
        i = 0
        decimal = 0

        while num != 0:
            rem = num % 10

            num = int(num / 10)

            decimal += rem * pow(2, i)

            i += 1
        return decimal

    def decimalToBinary(self, binary):
        op = 0
        i = 1
        while binary != 0:
            rem = binary % 2

            binary = int(binary / 2)

            op += rem * i

            i *= 10
        return op

    def addBinary(self, a, b):
        # Convert Binary to Decimal
        x = self.binaryToDecimal(int(a))
        y = self.binaryToDecimal(int(b))

        res = self.decimalToBinary(x+y)

        return str(res)
