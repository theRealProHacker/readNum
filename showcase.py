import readNum
import decimal

for value in [
    [],
    float("NaN"),
    3+5j,
    3+0j,
    "3",
    0,
    decimal.Decimal("3"),
    decimal.Decimal("3.450"),
    3.1034394123,
    10*10**210,
    1*10**23,
    0.00000051,
    {1:[1,2,3],2:(9,4),6:{3:[2,5,6],9:[23,89]}}
]:
    print(value)
    print(readNum.readNum(value))
    print()

print("Finished successfully")

