# Input Persen
input_massa_persen = float(input("Masukan Persen Massanya: "))
input_massa_H2SO4 = float(input("Masukan Massa H2SO4: "))
input_jenis_H2O = float(input("Masukan Jenis H2O: "))

# Define constants
massa_persen = input_massa_persen  # %
massa_H2SO4 = input_massa_H2SO4  # g/mL
massa_jenis_H2O = input_jenis_H2O  # g/mL

massa_molar_H2SO4 = 98  # g/mol
massa_molar_H2O = 18  # g/mol

massa_pelarut_H2O = 4  # g
valensi = 2


# Calculate Molarity
molarity = (10 * massa_H2SO4 * massa_persen) / massa_molar_H2SO4

# Calculate Normality
normality = molarity * valensi

# Calculate %v/V
# Volume Zat Larutan
volume_zat_larutan = (
    massa_persen / massa_H2SO4 + massa_pelarut_H2O / massa_jenis_H2O
)  # 57,33

persen_volume = (massa_persen / massa_H2SO4) / volume_zat_larutan * 100

# Calculate %b/V
bobot_volume = massa_persen / volume_zat_larutan * 100

# Calculate Molality
molality = (massa_persen / massa_molar_H2SO4) * (1000 / massa_pelarut_H2O)

# Calculate PPM
# g to mg & ml to L
massa_persen_mg = massa_persen * 1000  # 96000 mg
volume_zat_larutan_L = volume_zat_larutan / 1000
ppm = massa_persen_mg / volume_zat_larutan_L

# Calculate Fraksi Mol
# Nt & Np
nt = massa_persen / massa_molar_H2SO4
np = massa_pelarut_H2O / massa_molar_H2O

xt = nt / (nt + np)
xp = np / (nt + np)


# Output results
print("Initial concentration % Massa:", massa_persen, "%")

print("Molarity:" "{:.2f}".format(molarity), "M")
print("Normality:" "{:.2f}".format(normality), "N")
print("%v/V:", "{:.2f}".format(persen_volume), "%")
print("%w/V:", "{:.2f}".format(bobot_volume), "%")
print("Molality:", "{:.2f}".format(molality), "M")
print("PPM:", "{:.2f}".format(ppm), "PPM")
print("Mole Fraction:", "{:.2f}".format(xt), "&", "{:.2f}".format(xp))
