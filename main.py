import PokeStat as stats
import PokeEV as EV
import os

def Calstat():
    #Stat= [Base,IV,EV]
    hpstat = [0,0,0]
    atkstat = [0,0,0]
    defstat = [0,0,0]
    spatkstat = [0,0,0]
    spdefstat = [0,0,0]
    spdstat = [0,0,0]

    #Base Stats
    hpstat[0] = int(input("Base HP: "))
    atkstat[0] = int(input("Base Atk: "))
    defstat[0] = int(input("Base Def: "))
    spatkstat[0] = int(input("Base Sp.Atk: "))
    spdefstat[0] = int(input("Base Sp.Def: "))
    spdstat[0] = int(input("Base spd: "))

    #IV Stats
    hpstat[1] = int(input("\nHP Individual Value (0-31): "))
    if hpstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    atkstat[1] = int(input("Atk Individual Value (0-31): "))
    if atkstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    defstat[1] = int(input("Def Individual Value (0-31): "))
    if defstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    spatkstat[1] = int(input("Sp.Atk Individual Value (0-31): "))
    if spatkstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    spdefstat[1] = int(input("Sp.def Individual Value (0-31): "))
    if spdefstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()
    spdstat[1] = int(input("Spd Individual Value (0-31): "))
    if spdstat[1] > 31:
        print("Just Select 0-31...\nExitting...")   
        exit()

    #EV Stats
    hpstat[2] = int(input("\nHP Effort Value (0-255): "))
    if hpstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    atkstat[2] = int(input("Atk Effort Value (0-255): "))
    if atkstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    defstat[2] = int(input("Def Effort Value (0-255): "))
    if defstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spatkstat[2] = int(input("Sp.Atk Effort Value (0-255): "))
    if spatkstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spdefstat[2] = int(input("Sp.Def Effort Value (0-255): "))
    if spdefstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    spdstat[2] = int(input("Spd Effort Value (0-255): "))
    if spdstat[2] > 255:
        print("Just Select 0-255...\nExitting...")   
        exit()
    evlim = atkstat[2]+defstat[2]+spatkstat[2]+spdefstat[2]+spdstat[2]
    if evlim > 510:
        print("total EV limit reached...\nshould not exeed 510...\nexitting...")
        exit()

    #Pokemon Level
    hplvl = int(input("Pokemon Level: "))

    #Nature
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

    #Stats Computation
    stathp = stats.PokeStat.hpstat(hpstat[0], hpstat[1], hpstat[2], hplvl)
    statatk = stats.PokeStat.atkstat(atkstat[0], atkstat[1], atkstat[2], hplvl, oNtr)
    statdef = stats.PokeStat.defstat(defstat[0], defstat[1], defstat[2], hplvl, oNtr)
    statspatk = stats.PokeStat.spatkstat(spatkstat[0], spatkstat[1], spatkstat[2], hplvl, oNtr)
    statspdef = stats.PokeStat.spdefstat(spdefstat[0], spdefstat[1], spdefstat[2], hplvl, oNtr)
    statspd = stats.PokeStat.spdstat(spdstat[0], spdstat[1], spdstat[2], hplvl, oNtr)

    #Stats Result
    print("HP: ", stathp)
    print("Atk: ", statatk)
    print("Def: ", statdef)
    print("Sp.Atk: ", statspatk)
    print("Sp.Def: ", statspdef)
    print("Spd: ", statspd)

def EVstat():
    #Stat= [Base,value,IV,EV]
    atkstat = [0,0,0,0]
    defstat = [0,0,0,0]
    spatkstat = [0,0,0,0]
    spdefstat = [0,0,0,0]
    spdstat = [0,0,0,0]

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
    
    
    if evinp == 1:
        stbase = int(input("Base Stat: "))
        stinc = int(input("Desired increase Stat: "))
        stIV = int(input("Individual Value (0-31): "))
        if stIV > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()
        stEV = int(input("Effort Value (0-255): "))
        if stEV > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
    else:
        #Base Stats
        atkstat[0] = int(input("Base Atk: "))
        defstat[0] = int(input("Base Def: "))
        spatkstat[0] = int(input("Base Sp.Atk: "))
        spdefstat[0] = int(input("Base Sp.Def: "))
        spdstat[0] = int(input("Base spd: "))

        #Desired increase Stats
        atkstat[1] = int(input("\nDesired increase Atk: "))
        defstat[1] = int(input("Desired increasee Def: "))
        spatkstat[1] = int(input("Desired increase Sp.Atk: "))
        spdefstat[1] = int(input("Desired increase Sp.Def: "))
        spdstat[1] = int(input("Desired increase spd: "))

        #IV Stats
        atkstat[2] = int(input("\nAtk Individual Value (0-31): "))
        if atkstat[2] > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()
        defstat[2] = int(input("Def Individual Value (0-31): "))
        if defstat[2] > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()
        spatkstat[2] = int(input("Sp.Atk Individual Value (0-31): "))
        if spatkstat[2] > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()
        spdefstat[2] = int(input("Sp.def Individual Value (0-31): "))
        if spdefstat[2] > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()
        spdstat[2] = int(input("Spd Individual Value (0-31): "))
        if spdstat[2] > 31:
            print("Just Select 0-31...\nExitting...")   
            exit()

        #EV Stats
        atkstat[3] = int(input("\nAtk Effort Value (0-255): "))
        if atkstat[3] > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        defstat[3] = int(input("Def Effort Value (0-255): "))
        if defstat[3] > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spatkstat[3] = int(input("Sp.Atk Effort Value (0-255): "))
        if spatkstat[3] > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spdefstat[3] = int(input("Sp.Def Effort Value (0-255): "))
        if spdefstat[3] > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        spdstat[3] = int(input("Spd Effort Value (0-255): "))
        if spdstat[3] > 255:
            print("Just Select 0-255...\nExitting...")   
            exit()
        evlim = atkstat[3]+defstat[3]+spatkstat[3]+spdefstat[3]+spdstat[3]
        if evlim > 510:
            print("total EV limit reached...\nshould not exeed 510...\nexitting...")
            exit()

    #Level
    stlvl = int(input("Pokemon Level: "))

    #Nature
    pntr = """
    0 - Hardy       5 - Bold        10 - Timid      15 - Modest     20 - Calm
    1 - Lonely      6 - Docile      11 - Hasty      16 - Mild       21 - Gentle
    2 - Brave       7 - Relaxed     12 - Serious    17 - Quiet      22 - Sassy
    3 - Adamant     8 - Impish      13 - Jolly      18 - Bashful    23 - Careful
    4 - Naughty     9 - Lax         14 - Naive      19 - Rash       24 - Quirky
    """
    print (pntr)
    stNtr = int(input("Modifier (Nature): "))
    
    #This Part should Calculate the desired increase stats first
    #using the Stats Calculator to prevent negative result in EVs
    if evinp == 1:
        stStatatk = stats.PokeStat.atkstat(stinc, stIV, stEV, stlvl, stNtr)
        stStatdef = stats.PokeStat.defstat(stinc, stIV, stEV, stlvl, stNtr)
        stStatspatk = stats.PokeStat.spatkstat(stinc, stIV, stEV, stlvl, stNtr)
        stStatspdef = stats.PokeStat.spdefstat(stinc, stIV, stEV, stlvl, stNtr)
        stStatspd = stats.PokeStat.spdstat(stinc, stIV, stEV, stlvl, stNtr)
    else:
        stStatatk = stats.PokeStat.atkstat(atkstat[1], atkstat[2], atkstat[3], stlvl, stNtr)
        stStatdef = stats.PokeStat.defstat(defstat[1], defstat[2], defstat[3], stlvl, stNtr)
        stStatspatk = stats.PokeStat.spatkstat(spatkstat[1], spatkstat[2], spatkstat[3], stlvl, stNtr)
        stStatspdef = stats.PokeStat.spdefstat(spdefstat[1], spdefstat[2], spdefstat[3], stlvl, stNtr)
        stStatspd = stats.PokeStat.spdstat(spdstat[1], spdstat[2], spdstat[3], stlvl, stNtr)

    #After Calculating the desired increase stats now for the EV calculation
    if evinp == 1:
        evatk = EV.PokeEV.atkev(stStatatk, stNtr, stbase, stlvl, stIV, stEV)
        evdef = EV.PokeEV.defev(stStatdef, stNtr, stbase, stlvl, stIV, stEV)
        evspatk = EV.PokeEV.spatkev(stStatspatk, stNtr, stbase, stlvl, stIV, stEV)
        evspdef = EV.PokeEV.spdefev(stStatspdef, stNtr, stbase, stlvl, stIV, stEV)
        evspd = EV.PokeEV.spdev(stStatspd, stNtr, stbase, stlvl, stIV, stEV)
    else:
        evatk = EV.PokeEV.atkev(stStatatk, stNtr, atkstat[0], stlvl, atkstat[2], atkstat[3])
        evdef = EV.PokeEV.defev(stStatdef, stNtr, defstat[0], stlvl, defstat[2], defstat[3])
        evspatk = EV.PokeEV.spatkev(stStatspatk, stNtr, spatkstat[0], stlvl, spatkstat[2], spatkstat[3])
        evspdef = EV.PokeEV.spdefev(stStatspdef, stNtr, spdefstat[0], stlvl, spdefstat[2], spdefstat[3])
        evspd = EV.PokeEV.spdev(stStatspd, stNtr, spdstat[0], stlvl, spdstat[2], spdstat[3])

    #EV Result
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