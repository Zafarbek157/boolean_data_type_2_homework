def main(a):
    """
    Given integer is less of 10000 . Check if the sum of digits is odd .
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    s=0
    s+=a%10
    s//=10

    s+=a%10
    s//=10

    s+=a%10
    s//=10

    s+=a%10
    s//=10
    return s%2==1
print(main(4))