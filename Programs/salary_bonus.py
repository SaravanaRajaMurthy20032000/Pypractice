salary = float(input("Enter your salary: "))
service = int(input("year of service: "))

if service > 5:
    bonus = salary * .05
    net_bonus = salary + bonus

    print(f"your bonus amount is {bonus}")
    print(f"your net salary (including bonus) is: {net_bonus}")

else:
    print("Sorry you don't qualify for the bonus.")