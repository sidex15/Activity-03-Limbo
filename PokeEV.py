from math import ceil


class PokeEV():

    def atkev(pokeStat,pokeModif,pokeBase,pokeLVL,pokeIV,pokeEV):
        nature = 1.0
        if pokeModif == 1 or pokeModif == 2 or pokeModif == 3 or pokeModif == 4:
            nature=1.1
        elif pokeModif == 5 or pokeModif == 10 or pokeModif == 15 or pokeModif == 20:
            nature=0.9
        else: 
            nature=1.0
        d = ((2 * pokeBase + pokeIV +(pokeEV/4))*pokeLVL/100)
        ev = ceil((((((pokeStat/nature)-d)*400)/pokeLVL)/4))*4
        return ev
    
    def defev(pokeStat,pokeModif,pokeBase,pokeLVL,pokeIV,pokeEV):
        nature=1.0
        if pokeModif == 5 or pokeModif == 7 or pokeModif == 8 or pokeModif == 9:
            nature=1.1
        elif pokeModif == 1 or pokeModif == 11 or pokeModif == 16 or pokeModif == 21:
            nature=0.9
        else: 
            nature=1.0
        d = ((2 * pokeBase + pokeIV +(pokeEV/4))*pokeLVL/100)
        ev = ceil((((((pokeStat/nature)-d)*400)/pokeLVL)/4))*4
        return ev

    def spatkev(pokeStat,pokeModif,pokeBase,pokeLVL,pokeIV,pokeEV):
        nature=1.0
        if pokeModif == 15 or pokeModif == 16 or pokeModif == 17 or pokeModif == 19:
            nature=1.1
        elif pokeModif == 3 or pokeModif == 8 or pokeModif == 13 or pokeModif == 23:
            nature=0.9
        else: 
            nature=1.0
        d = ((2 * pokeBase + pokeIV +(pokeEV/4))*pokeLVL/100)
        ev = ceil((((((pokeStat/nature)-d)*400)/pokeLVL)/4))*4
        return ev

    def spdefev(pokeStat,pokeModif,pokeBase,pokeLVL,pokeIV,pokeEV):
        nature=1.0
        if pokeModif == 20 or pokeModif == 21 or pokeModif == 22 or pokeModif == 23:
            nature=1.1
        elif pokeModif == 4 or pokeModif == 9 or pokeModif == 14 or pokeModif == 19:
            nature=0.9
        else: 
            nature=1.0
        d = ((2 * pokeBase + pokeIV +(pokeEV/4))*pokeLVL/100)
        ev = ceil((((((pokeStat/nature)-d)*400)/pokeLVL)/4))*4
        return ev

    def spdev(pokeStat,pokeModif,pokeBase,pokeLVL,pokeIV,pokeEV):
        nature=1.0
        if pokeModif == 10 or pokeModif == 11 or pokeModif == 13 or pokeModif == 14:
            nature=1.1
        elif pokeModif == 2 or pokeModif == 7 or pokeModif == 17 or pokeModif == 22:
            nature=0.9
        else: 
            nature=1.0
        d = ((2 * pokeBase + pokeIV + (pokeEV/4))*pokeLVL/100)
        ev = ceil((((((pokeStat/nature)-d)*400)/pokeLVL)/4))*4
        return ev