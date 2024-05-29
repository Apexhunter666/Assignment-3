class EuclideanAlgorithm:
    @staticmethod
    def gcd(a, b):
        """
        Calculate the Greatest Common Divisor (GCD) of two positive integers using the Euclidean Algorithm.

        :param a: The first positive integer.
        :param b: The second positive integer.
        :return: The GCD of a and b.
        """
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


if __name__ == "__main__":
    # Example usage
    num1 = int(input("Enter the integer number:"))
    num2 = int(input("Enter the integer number:"))
    print(f"The greatest common divisor of {num1} and {num2} is: {EuclideanAlgorithm.gcd(num1, num2)}")
