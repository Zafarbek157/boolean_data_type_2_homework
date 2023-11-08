def main(a):
    """
    Check if a given year is a leap year and the square of the year is greater than 10000.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a**2>=10000 and (a%4==0 and a%100!=0) or (a%100==0 and a%400==0)
print(main())