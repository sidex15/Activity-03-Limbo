class PokeStat():
    
    def hpstat(pokeBase,pokeIV,pokeEV,pokeLVL):
        hp = (((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+pokeLVL+10
        return hp

    def atkstat(pokeBase,pokeIV,pokeEV,pokeLVL,pokeNature):
        nature=0
        if pokeNature == 1 or pokeNature == 2 or pokeNature == 3 or pokeNature == 4:
            nature=1.1
        elif pokeNature == 5 or pokeNature == 10 or pokeNature == 15 or pokeNature == 20:
            nature=0.9
        else: 
            nature=1.0
        atk = ((((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+5)*nature
        return atk

    def defstat(pokeBase,pokeIV,pokeEV,pokeLVL,pokeNature):
        nature=0
        if pokeNature == 5 or pokeNature == 7 or pokeNature == 8 or pokeNature == 9:
            nature=1.1
        elif pokeNature == 1 or pokeNature == 11 or pokeNature == 16 or pokeNature == 21:
            nature=0.9
        else: 
            nature=1.0
        defe = ((((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+5)*nature
        return defe

    def spatkstat(pokeBase,pokeIV,pokeEV,pokeLVL,pokeNature):
        nature=0
        if pokeNature == 15 or pokeNature == 16 or pokeNature == 17 or pokeNature == 19:
            nature=1.1
        elif pokeNature == 3 or pokeNature == 8 or pokeNature == 13 or pokeNature == 23:
            nature=0.9
        else: 
            nature=1.0
        spatk = ((((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+5)*nature
        return spatk

    def spdefstat(pokeBase,pokeIV,pokeEV,pokeLVL,pokeNature):
        nature=0
        if pokeNature == 20 or pokeNature == 21 or pokeNature == 22 or pokeNature == 23:
            nature=1.1
        elif pokeNature == 4 or pokeNature == 9 or pokeNature == 14 or pokeNature == 19:
            nature=0.9
        else: 
            nature=1.0
        spdef = ((((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+5)*nature
        return spdef
    
    def spdstat(pokeBase,pokeIV,pokeEV,pokeLVL,pokeNature):
        nature=0
        if pokeNature == 10 or pokeNature == 11 or pokeNature == 13 or pokeNature == 14:
            nature=1.1
        elif pokeNature == 2 or pokeNature == 7 or pokeNature == 17 or pokeNature == 22:
            nature=0.9
        else: 
            nature=1.0
        spd = ((((2*pokeBase+pokeIV+(pokeEV/4))*pokeLVL)/100)+5)*nature
        return spd