import PokeStat as stats
import PokeEV as EV
import math
import sys
import os

def Calstat():
    #print ("HP stat")
    hpbase = int(input("Base HP/Stat: "))
    hpIV = int(input("Individual Value (0-31): "))
    if hpIV > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    hpEV = int(input("Effor Value (0-255): "))
    if hpEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    hplvl = int(input("Pokemon Level: "))

    #print ("\nOther stats (Atk,Def,Sp.Atk,Sp.Def,Spd)")
    #obase = int(input("Base HP: "))
    #oIV = int(input("Individual Value (0-31): "))
    #oEV = int(input("Effor Value (0-255): "))
    #olvl = int(input("Pokemon Level: "))
    pntr = """
    0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
    1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
    2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
    3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
    4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky
    """
    print (pntr)
    oNtr = int(input("Nature : "))
    if oNtr > 24:
        print("Just Select 0-24...\nExitting...")   
        exit()

    stathp = stats.PokeStat.hpstat(hpbase, hpIV, hpEV, hplvl)
    statatk = stats.PokeStat.atkstat(hpbase, hpIV, hpEV, hplvl, oNtr)
    statdef = stats.PokeStat.defstat(hpbase, hpIV, hpEV, hplvl, oNtr)
    statspatk = stats.PokeStat.spatkstat(hpbase, hpIV, hpEV, hplvl, oNtr)
    statspdef = stats.PokeStat.spdefstat(hpbase, hpIV, hpEV, hplvl, oNtr)
    statspd = stats.PokeStat.spdstat(hpbase, hpIV, hpEV, hplvl, oNtr)

    print("HP: ", round(stathp,2))
    print("Atk: ", round(statatk,2))
    print("Def: ", round(statdef,2))
    print("Sp.Atk: ", round(statspatk,2))
    print("Sp.Def: ", round(statspdef,2))
    print("Spd: ", round(statspd,2))

def EVstat():
    print("1 - Single Stat\n2 - All Stats")
    evinp = int(input("select (1-2): "))
    if evinp >=3:
        print("Just Select 1-2...\nExitting...")   
        exit()
    elif evinp == 1:
        pstats = """
    1 - Atk
    2 - Def
    3 - Sp.Atk
    4 - Sp.Def
    5 - Spd
    """
        print(pstats)
        evinp1 = int(input("select (1-5): "))
        if evinp1 >=3:
            print("Just Select 1-5...\nExitting...")   
            exit()
    

    stbase = int(input("Base Stat: "))
    stIV = int(input("Individual Value (0-31): "))
    if stIV > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    stEV = int(input("Effor Value (0-255): "))
    if stEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    stlvl = int(input("Pokemon Level: "))
    pntr = """
    0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
    1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
    2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
    3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
    4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky
    """
    print (pntr)
    stNtr = int(input("Modifier (Nature): "))
    
    stStatatk = stats.PokeStat.atkstat(stbase, stIV, stEV, stlvl, stNtr)
    stStatdef = stats.PokeStat.defstat(stbase, stIV, stEV, stlvl, stNtr)
    stStatspatk = stats.PokeStat.spatkstat(stbase, stIV, stEV, stlvl, stNtr)
    stStatspdef = stats.PokeStat.spdefstat(stbase, stIV, stEV, stlvl, stNtr)
    stStatspd = stats.PokeStat.spdstat(stbase, stIV, stEV, stlvl, stNtr)

    evatk = EV.PokeEV.atkev(stStatatk, stNtr, stbase, stlvl, stIV, stEV)
    evdef = EV.PokeEV.defev(stStatdef, stNtr, stbase, stlvl, stIV, stEV)
    evspatk = EV.PokeEV.spatkev(stStatspatk, stNtr, stbase, stlvl, stIV, stEV)
    evspdef = EV.PokeEV.spdefev(stStatspdef, stNtr, stbase, stlvl, stIV, stEV)
    evspd = EV.PokeEV.spdev(stStatspd, stNtr, stbase, stlvl, stIV, stEV)

    if evinp == 2:
        print("\nAtk: ", round(evatk,2))
        print("Def: ", round(evdef,2))
        print("Sp.Atk: ", round(evspatk,2))
        print("Sp.Def: ", round(evspdef,2))
        print("Spd: ", round(evspd,2))
    elif evinp == 1:
        if evinp1 == 1:
            print("\nAtk: ", round(evatk,2))
        elif evinp1 == 2:
            print("\nDef: ", round(evdef,2))
        elif evinp1 == 3:
            print("\nSp.Atk: ", round(evspatk,2))
        elif evinp1 == 4:
            print("\nSp.Def: ", round(evspdef,2))
        elif evinp1 == 5:
            print("\nSpd: ", round(evspd,2))
            
def pokemenu():
    print("Pokemon Stat/EV Calculator")
    print("1. Stat Calculator\n2. EV Calculator")
    inp1 = int(input ("Select (1-2): "))
    if inp1 == 1:
        Calstat()
    elif inp1 ==2:
        EVstat()
    else:
        print("Just Select 1-2...\nExitting...")   
        exit()

pokemenu()
print ("\nDo you want to Run Again?")
yn = input("Y/N: ")
if yn == 'Y' or yn == 'y':
    os.system("cls")
    pokemenu()
else:
     print("Exitting...")   
     exit()    