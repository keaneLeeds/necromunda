class Fighter(object):
    def __init__(self, stats):
        self.name = stats.get('name')
        self.gangerType = stats.get('gangerType')
        self.m = stats.get('m')
        self.ws = stats.get('ws')
        self.bs = stats.get('bs')
        self.s = stats.get('s')
        self.t = stats.get('t')
        self.w = stats.get('w')
        self.i = stats.get('i')
        self.a = stats.get('a')
        self.ld = stats.get('ld')
        self.weapons = []
        self.weapons.append(stats.get('weapons'))
        self.cost = stats.get('cost')
        self.mainHand = self.weapons[0]
        self.offHand = None
        self.thirdHand = None
        self.equipped = [self.mainHand]

    def getStrength(self):
        mainStr = self.mainHand.strength
        #offStr = self.offHand.strength
        #thirdStr = self.thirdHand.strength

        if mainStr == 'fighter':
            mainStr = self.s + self.mainHand.bonusStrength

        #if offStr == 'fighter':
        #    offStr = self.s + self.offHand.strengthBonus
        #if thirdStr == 'fighter':
        #    thirdStr = self.s + self.thirdHand.strenghtBonus

        return mainStr

    def equipWeapon(self, weap, hand):
        if hand == 'mainHand':
            self.mainHand = weap
            self.equipped[0] = weap
        if hand == 'offHand':
            self.offHand = weap
            if len(self.equipped) >= 2:
                self.equipped[1] = weap
            else:
                self.equipped.append(weap)
        if hand == 'thirdHand':
            self.thirdHand = weap
            self.equipped[2] = weap

    def addWeapon(self, weap):
        self.weapons.append(weap)
    
    def setWeapon(self, weap):
        self.weapons = []
        self.addWeapon(weap)

    def numberOfParries(self):
        weaps = [weapon.parry for weapon in self.equipped]
        return weaps.count(True)

    def getWeaponNames(self):
        weaps = [weapon.weaponId for weapon in self.weapons]
        return weaps

    def hasParry(self):
        weaps = self.getWeaponNames()
        if 'sword' in weaps:
            return True
        else:
            return False

    def hasNullifications(self):
        weaps = self.getWeaponNames()
        if 'chain' in weaps:
            return True
        else:
            return False

    def numberOfChains(self):
        weaps = self.getWeaponNames()
        return weaps.count('chain')

    def numberOfNullifications(self):
        weaps = [weapon.nullify for weapon in self.equipped]
        return weaps.count(True)

class MeleeWeapon(object):
    def __init__(self, stats):
        self.weaponId = stats.get('weaponId')
        self.strength = stats.get('strength')
        self.bonusStrength = stats.get('bonusStrength')
        self.damage = stats.get('damage')
        self.saveMod = stats.get('saveMod')

        self.parry = stats.get('parry')
        self.nullify = stats.get('nullify')
        self.clumsy = stats.get('clumsy')
        self.outOfAction = stats.get('outOfAction')
        self.injury = stats.get('injury')
        self.noisy = stats.get('noisy')
        self.twoHanded = stats.get('twoHanded')
        self.dualHanded = stats.get('dualHanded')
        self.draws = stats.get('draws')
        self.mightyBlows = stats.get('mightyBlows')
        self.cost = stats.get('cost')

class ShootyWeapon(object):
    def __init__(self, stats):
        self.weaponId = stats.get('weaponId')
        self.weaponClass = stats.get('weaponClass') #pistol, basic, special, heavy, scaly, primitive,
        self.shortRange = stats.get('shortRange')
        self.longRange = stats.get('longRange')
        self.shortToHit = stats.get('shortToHit')
        self.longToHit = stats.get('longToHit')
        self.strength = stats.get('strength')
        self.damage = stats.get('damage')
        self.saveMod = stats.get('saveMod')
        self.ammoRoll = stats.get('ammoRoll')
        self.cost = stats.get('cost')

        self.alwaysAmmoRoll = stats.get('alwaysAmmoRoll')
        self.flamer = stats.get('flamer')
        self.catchFire = stats.get('catchFire')
        self.getHot = stats.get('getHot')
        self.toxicDart = stats.get('toxicDart')
        self.silent = stats.get('silent')
        self.injuries = stats.get('injuries')
        self.webbedTargets = stats.get('webbedTargets')
        self.solvent = stats.get('solvent')
        self.capture = stats.get('capture')
        self.knockBack = stats.get('knockBack')
        self.pellets = stats.get('pellets')
        self.headShot = stats.get('headShot')
        self.sustainedFire = stats.get('sustainedFire')
        self.ammo = stats.get('ammo')
        self.highImpact = stats.get('highImpact')
        self.moveAndFire = stats.get('moveAndFire')
        self.gasCloud = stats.get('gasCloud')
        self.blast = stats.get('blast')
        self.smoke = stats.get('smoke')
        self.choke = stats.get('choke')
        self.scare = stats.get('scare')
        self.blind = stats.get('blind')
        self.plasmaBall = stats.get('plasmaBall')
        self.demolition = stats.get('demolition')
        self.hallucenation = stats.get('hallucenation')
        self.hitPenalty = stats.get('hitPenalty')

class Armor(object):
    def __init__(self, stats):
        self.armorId = stats.get('armorId')
        self.save = stats.get('save')
        self.cost = stats.get('cost')

        self.flakSave = stats.get('flakSave')
        self.initiativePenalty = stats.get('initiativePenalty')
        self.shootOnly = stats.get('shootOnly')
        self.forceProtection = stats.get('forceProtection')

class MungVase(object):
    def __init__(self):
        self.cost = d6()
        self.value = self.getValue()
        
    def getValue(self):
        roll = d6()
        if roll == 1:
            return d6() #1-6, average=3.5
        if roll == 2:
            return 2*d6() #2-12, average=7
        if roll == 3:
            return (6*d6())+30 #36-66, average=51
        if roll == 4:
            return (6*d6())+30 #36-66, average=51
        if roll == 5:
            return (2*d6())*10 #20-120, average=70
        if roll == 6:
            return (3*d6()*10) #30-180, average=105
