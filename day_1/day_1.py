with open("day_1.txt") as f:
    data = f.readlines()


def required_fuel(module_mass: int) -> int:
    return int(module_mass/3) - 2


def fuel_needed_for_fuel(fuel: int) -> int:
    fuel_needed = 0
    while True:
        fuel = required_fuel(fuel)
        if fuel < 0:
            break
        fuel_needed += fuel
    return fuel_needed


total_fuel = 0
for i in data:
    required_fuel_for_module_mass = required_fuel(int(i))
    total_fuel += required_fuel_for_module_mass + fuel_needed_for_fuel(required_fuel_for_module_mass)

print(total_fuel)
