def main(L,R):
    """
    Check that given L is the length of a circle of radius R.
    Args:
        L: float
        R: float
    Returns:
        bool
    """
    # Write your code here
    R=float(input(" "))
    return L==2*3.14*R
print(main())