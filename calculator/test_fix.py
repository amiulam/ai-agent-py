from pkg.calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 7 * 2")
print(f"3 + 7 * 2 = {result}")

if result == 17:
    print("Success: 3 + 7 * 2 is 17")
else:
    print(f"Failure: 3 + 7 * 2 is {result}, expected 17")
