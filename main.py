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
    hpEV = int(input("HP Effort Value (0-255): "))
    if hpEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    atkEV = int(input("Atk Effort Value (0-255): "))
    if atkEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    defEV = int(input("Def Effort Value (0-255): "))
    if defEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spatkEV = int(input("Sp.Atk Effort Value (0-255): "))
    if spatkEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spdefEV = int(input("Sp.Def Effort Value (0-255): "))
    if spdefEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spdEV = int(input("Spd Effort Value (0-255): "))
    if spdEV > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    evlim = atkEV+defEV+spatkEV+spdefEV+spdEV
    if evlim > 510:
        print("total EV limit reached...\nshould not exeed 510...\nexitting...")
        exit()
    hplvl = int(input("Pokemon Level: "))

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
    statatk = stats.PokeStat.atkstat(hpbase, hpIV, atkEV, hplvl, oNtr)
    statdef = stats.PokeStat.defstat(hpbase, hpIV, defEV, hplvl, oNtr)
    statspatk = stats.PokeStat.spatkstat(hpbase, hpIV, spatkEV, hplvl, oNtr)
    statspdef = stats.PokeStat.spdefstat(hpbase, hpIV, spdefEV, hplvl, oNtr)
    statspd = stats.PokeStat.spdstat(hpbase, hpIV, spdEV, hplvl, oNtr)

    print("HP: ", stathp)
    print("Atk: ", statatk)
    print("Def: ", statdef)
    print("Sp.Atk: ", statspatk)
    print("Sp.Def: ", statspdef)
    print("Spd: ", statspd)

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
    if evinp == 1:
        stEV = int(input("Effort Value (0-255): "))
        if stEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
    else:
        atkEV = int(input("Atk Effort Value (0-255): "))
        if atkEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        defEV = int(input("Def Effort Value (0-255): "))
        if defEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spatkEV = int(input("Sp.Atk Effort Value (0-255): "))
        if spatkEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spdefEV = int(input("Sp.Def Effort Value (0-255): "))
        if spdefEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spdEV = int(input("Spd Effort Value (0-255): "))
        if spdEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        evlim = atkEV+defEV+spatkEV+spdefEV+spdEV
        if evlim > 510:
            print("total EV limit reached...\nshould not exeed 510...\nexitting...")
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
    
    if evinp == 1:
        stStatatk = stats.PokeStat.atkstat(stbase, stIV, stEV, stlvl, stNtr)
        stStatdef = stats.PokeStat.defstat(stbase, stIV, stEV, stlvl, stNtr)
        stStatspatk = stats.PokeStat.spatkstat(stbase, stIV, stEV, stlvl, stNtr)
        stStatspdef = stats.PokeStat.spdefstat(stbase, stIV, stEV, stlvl, stNtr)
        stStatspd = stats.PokeStat.spdstat(stbase, stIV, stEV, stlvl, stNtr)
    else:
        stStatatk = stats.PokeStat.atkstat(stbase, stIV, atkEV, stlvl, stNtr)
        stStatdef = stats.PokeStat.defstat(stbase, stIV, defEV, stlvl, stNtr)
        stStatspatk = stats.PokeStat.spatkstat(stbase, stIV, spatkEV, stlvl, stNtr)
        stStatspdef = stats.PokeStat.spdefstat(stbase, stIV, spdefEV, stlvl, stNtr)
        stStatspd = stats.PokeStat.spdstat(stbase, stIV, spdEV, stlvl, stNtr)

    if evinp == 1:
        evatk = EV.PokeEV.atkev(stStatatk, stNtr, stbase, stlvl, stIV, stEV)
        evdef = EV.PokeEV.defev(stStatdef, stNtr, stbase, stlvl, stIV, stEV)
        evspatk = EV.PokeEV.spatkev(stStatspatk, stNtr, stbase, stlvl, stIV, stEV)
        evspdef = EV.PokeEV.spdefev(stStatspdef, stNtr, stbase, stlvl, stIV, stEV)
        evspd = EV.PokeEV.spdev(stStatspd, stNtr, stbase, stlvl, stIV, stEV)
    else:
        evatk = EV.PokeEV.atkev(stStatatk, stNtr, stbase, stlvl, stIV, atkEV)
        evdef = EV.PokeEV.defev(stStatdef, stNtr, stbase, stlvl, stIV, defEV)
        evspatk = EV.PokeEV.spatkev(stStatspatk, stNtr, stbase, stlvl, stIV, spatkEV)
        evspdef = EV.PokeEV.spdefev(stStatspdef, stNtr, stbase, stlvl, stIV, spdefEV)
        evspd = EV.PokeEV.spdev(stStatspd, stNtr, stbase, stlvl, stIV, spdEV)

    if evinp == 2:
        print("\nAtk: ", evatk)
        print("Def: ", evdef)
        print("Sp.Atk: ", evspatk)
        print("Sp.Def: ", evspdef)
        print("Spd: ", evspd)
    elif evinp == 1:
        if evinp1 == 1:
            print("\nAtk: ", evatk)
        elif evinp1 == 2:
            print("\nDef: ", evdef)
        elif evinp1 == 3:
            print("\nSp.Atk: ", evspatk)
        elif evinp1 == 4:
            print("\nSp.Def: ", evspdef)
        elif evinp1 == 5:
            print("\nSpd: ", evspd)
            
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