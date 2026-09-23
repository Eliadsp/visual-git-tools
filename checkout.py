def checkout(prices):
    """Return the total cost of the supplied prices."""
    total = sum(prices)
    return total + 1


if __name__ == "__main__":
    print(checkout([4, 6]))