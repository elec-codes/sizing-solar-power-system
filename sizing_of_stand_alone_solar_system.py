###
#SOLARE POWER PLANT, STAND-ALONE#
###

#get data
panel_efficiency = float(input("Panel  efficiency: "))
i_max = float(input("Max current flow[I]: "))
v_max = float(input("Max voltage[v]: "))
p_max_panel = float(input("Max panel power[KW]: "))
a_panel = float(input("Panel surface[m^2]: "))
g = float(input("G (irradiation)[KWh/m^2]: "))

#user's energy needs

user_powers = []
power_hours = []
quantity_of_loads =[]

#get all daily used power and for how much time
while True:
        p = input("Insert value of user power[KW]: ")
        user_powers.append(p) 
        h = input("Insert hours: ")
        power_hours.append(h)
        qta = int(input("Insert quantity of loads with this power: "))
        quantity_of_loads.append(qta)
        new_power = input("Insert a new power? ")
        if new_power != "yes":
            break

print(f"user powers[kw]: {user_powers}, hours of powers {power_hours}")

#calculate user's max power
pmax =0
h=0
for p in user_powers:
      pmax= pmax+float(p)*quantity_of_loads[h]
      h+=1

print("potenza massima[KW]", pmax)

#calculate powers in KWh
powers_kwh = []
h = 0
for p in user_powers:
      p_h = float(p)*float(power_hours[h])*float(quantity_of_loads[h])
      powers_kwh.append(p_h)
      h =+ 1

print("Powers [KWh]", powers_kwh)

#calculate daily total daily energy (sum of powers in KWh)
e_gtot = 0
for v in powers_kwh:
      e_gtot = e_gtot + float(v)
    
print("Egtot", e_gtot, "KWh")

#total energy needs (considering the batteries to charge)
daily_energy_needs_tot = 1.3 * float(e_gtot)

print("Daily energy need: (Ec) [KWh]", daily_energy_needs_tot)

#calculate total yield
tot_efficiency = (panel_efficiency/100)* 0.84 * 0.92 * 0.99
print("Total efficiency: ", tot_efficiency)

#calculate the total area needed of solar panel(s) 
area_tot = daily_energy_needs_tot/(tot_efficiency*g)

print("Total surface ", area_tot, "m^2")

#number of panels
n_panels = area_tot/a_panel
print("Number of panels", n_panels, "Aproximed at:", int(n_panels)+1)

#pmax pannels
p_max_panels = n_panels * p_max_panel
print("Max power panels[Kw]", p_max_panels)


if p_max_panels > pmax:
      print("ok")
else:
      print("Power too small")

#some advice on inverters
print("The minimum voltage of the inverter must be less than", n_panels*v_max, "V")
print("The maximum flow of current of the inverter must be more than", i_max, "A" )