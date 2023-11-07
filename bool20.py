def main(a):
    """
    Given integer is less of 10000 . Check if the sum of digits is odd .
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a<1000, a//10000
c=a//100 # 3 xonali son uchun
d=(a%100)//10
e=((a%100)//10)%10

print(main(343))
