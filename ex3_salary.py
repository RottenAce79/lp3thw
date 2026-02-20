print("If bruto is 3000 then neto will be", 3000 - 3000 * 0.105 - ((3000 - 3000 * 0.105) - 550) * 0.255)

# 3000 is bruto from which taxes are deducted

# 3000 * 0.105 calculates 10.5% from 3000 (social security)
# social security is 315.0

# ((3000 - 3000 * 0.105) - 550) * 0.255 calculates 25.5% from bruto after social security and tax-free minimum (550) is deducted from it (income tax)
# income tax is 544.425

# neto salary should be 2140.575
