mileage = float(input())
gas_cost = float(input())

gas_cost20 = (gas_cost / mileage) * 20
gas_cost75 = (gas_cost / mileage) * 75
gas_cost500 = (gas_cost / mileage) * 500

print(f"{gas_cost20:.2f} {gas_cost75:.2f} {gas_cost500:.2f}")