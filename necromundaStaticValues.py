from NecromundaModel import *

empty = MeleeWeapon({
        'weaponId':'empty'
    })
knife = MeleeWeapon({
        'weaponId':'knife',
        'strength':'fighter', 'bonusStrength':0, 'damage':1, 'saveMod':'fighter',
        'cost':5
    })
club = MeleeWeapon({
        'weaponId':'club',
        'strength':'fighter', 'bonusStrength':1, 'damage':1, 'saveMod':'fighter',
        'cost':10
    })
chain = MeleeWeapon({
        'weaponId':'chain',
        'strength':'fighter', 'bonusStrength':1, 'damage':1, 'saveMod':'fighter',
        'cost':10,
        'nullify':True, 'clumsy':True
    })
massiveClub = MeleeWeapon({
        'weaponId':'massiveClub',
        'strength':'fighter', 'bonusStrength':2, 'damage':1, 'saveMod':'fighter',
        'cost':15,
        'twoHanded':True, 'draws':True, 'mightyBlows':True
    })
sword = MeleeWeapon({
        'weaponId':'sword',
        'strength':'fighter', 'bonusStrength':0, 'damage':1, 'saveMod':'fighter',
        'cost':15,
        'parry':True
    })
chainSword = MeleeWeapon({
        'weaponId':'chainSword',
        'strength':4, 'bonusStrength':0, 'damage':1, 'saveMod':-2,
        'cost':25,
        'noisy':True, 'parry':True
    })
powerSword = MeleeWeapon({
        'weaponId':'powerSword',
        'strength':'fighter', 'bonusStrength':2, 'damage':1, 'saveMod':'fighter',
        'cost':40, 'variableCost':'3d6',
        'parry':True
    })
powerAxe = MeleeWeapon({
        'weaponId':'powerAxe',
        'strength':'fighter', 'bonusStrength':3, 'damage':1, 'saveMod':'fighter',
        'cost':35, 'variableCost':'3d6',
        'dualHanded':True
    })
powerFist = MeleeWeapon({
        'weaponId':'powerFist',
        'strength':'fighter', 'bonusStrength':5, 'damage':'d3', 'saveMod':'fighter',
        'cost':85, 'variableCost':'3d6'
    })
shockMaul = MeleeWeapon({
        'weaponId':'shockMaul',
        'strength':5, 'damage':1, 'saveMod':-2,
        'cost':35, 'variableCost':'3d6',
        'outOfAction':True, 'injury':True
    })

autopistol = ShootyWeapon({
        'weaponId':'autopistol', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':2, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':15,
    })
boltpistol = ShootyWeapon({
        'weaponId':'boltpistol', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':2, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-1, 'ammoRoll':6,
        'cost':25,
    })
stubgun = ShootyWeapon({
        'weaponId':'stubgun', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':1, 'longToHit':-1, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':10,
    })
laspistol = ShootyWeapon({
        'weaponId':'laspistol', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':2,
        'cost':15,
    })
needlepistol = ShootyWeapon({
        'weaponId':'needlepistol', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':2, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':-1, 'ammoRoll':6,
        'cost':80, 'variableCost':'4d6',
        'toxicDart':True, 'injuries':True, 'silent':True
    })
plasmapistol = ShootyWeapon({
        'weaponId':'plasmapistol', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':1, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-1, 'ammoRoll':4,
        'cost':30,
        'energyLevels':True
    })
plasmapistolHigh = ShootyWeapon({
        'weaponId':'plasmapistolHigh', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':16, 'shortToHit':2, 'longToHit':0, 'strength':5, 'damage':1, 'saveMod':-2, 'ammoRoll':6,
        'cost':0,
        'energyLevels':True
    })
webpistol = ShootyWeapon({
        'weaponId':'webpistol', 'weaponClass':'pistol',
        'shortRange':6, 'longRange':9, 'shortToHit':0, 'longToHit':-1, 'strength':0, 'damage':0, 'saveMod':0, 'ammoRoll':6,
        'cost':120, 'variableCost':'4d6',
        'webbedTargets':True, 'capture':True, 'webSolvent':True
    })
handFlamer = ShootyWeapon({
        'weaponId':'handFlamer', 'weaponClass':'pistol',
        'shortRange':8, 'longRange':8, 'shortToHit':0, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':-1, 'ammoRoll':5,
        'cost':25,
        'template':True, 'flamer':True, 'ammoRoll':True, 'catchFire':5
    })

autogun = ShootyWeapon({
        'weaponId':'autogun', 'weaponClass':'basic',
        'shortRange':12, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':20
    })
boltgun = ShootyWeapon({
        'weaponId':'boltgun', 'weaponClass':'basic',
        'shortRange':12, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-1, 'ammoRoll':6,
        'cost':35
    })
lasgun = ShootyWeapon({
        'weaponId':'lasgun', 'weaponClass':'basic',
        'shortRange':8, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':2,
        'cost':25
    })
huntingRifle = ShootyWeapon({
        'weaponId':'huntingRifle', 'weaponClass':'basic',
        'shortRange':8, 'longRange':32, 'shortToHit':-1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':25,
        'headShot':True
    })
shotgun = ShootyWeapon({
        'weaponId':'shotgun', 'weaponClass':'basic',
        'shortRange':4, 'longRange':18, 'shortToHit':1, 'longToHit':-1, 'strength':4, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':20,
        'knockBack':True, 'ammo':True
    })

flamer = ShootyWeapon({
        'weaponId':'flamer', 'weaponClass':'special',
        'shortRange':8, 'longRange':8, 'shortToHit':0, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-2, 'ammoRoll':4,
        'cost':40,
        'template':True, 'flamer':True, 'ammoRoll':True, 'catchFire':4
    })
autoslugger = ShootyWeapon({
        'weaponId':'autoslugger', 'weaponClass':'special',
        'shortRange':12, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':5,
        'cost':45,
        'sustainedFire':1
    })
grenadeLauncher = ShootyWeapon({
        'weaponId':'grenadeLauncher', 'weaponClass':'special',
        'shortRange':14, 'longRange':28, 'shortToHit':0, 'longToHit':-1, 'strength':0, 'damage':0, 'saveMod':0, 'ammoRoll':6,
        'cost':60,
        'grenadeAmmo':True
    })
meltagun = ShootyWeapon({
        'weaponId':'meltagun', 'weaponClass':'special',
        'shortRange':6, 'longRange':12, 'shortToHit':1, 'longToHit':0, 'strength':8, 'damage':6, 'saveMod':-5, 'ammoRoll':4,
        'cost':95
    })
needleRifle = ShootyWeapon({
        'weaponId':'needleRilfe', 'weaponClass':'special',
        'shortRange':16, 'longRange':32, 'shortToHit':1, 'longToHit':0, 'strength':3, 'damage':1, 'saveMod':-1, 'ammoRoll':6,
        'cost':180, 'variableCost':'4d6',
        'toxicDart':True, 'injuries':True, 'silent':True
    })
plasmagun = ShootyWeapon({
        'weaponId':'plasmagun', 'weaponClass':'special',
        'shortRange':8, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':5, 'damage':1, 'saveMod':-2, 'ammoRoll':4,
        'cost':80, 
        'energyLevels':True
    })
plasmagunHigh = ShootyWeapon({
        'weaponId':'plasmagunHigh', 'weaponClass':'special',
        'shortRange':12, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':6, 'damage':1, 'saveMod':-3, 'ammoRoll':6,
        'cost':0,
        'sustainedFire':1, 'energyLevels':True
    })

autocannon = ShootyWeapon({
        'weaponId':'autocannon', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':72, 'shortToHit':0, 'longToHit':0, 'strength':8, 'damage':'d6', 'saveMod':-5, 'ammoRoll':4,
        'cost':260,
        'sustainedFire':1
    })
heavyBolter = ShootyWeapon({
        'weaponId':'heavyBolter', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':40, 'shortToHit':0, 'longToHit':0, 'strength':5, 'damage':'d3', 'saveMod':-2, 'ammoRoll':6,
        'cost':180,
        'sustainedFire':2
    })
heavyPlasmagun = ShootyWeapon({
        'weaponId':'heavyPlasmagun', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':40, 'shortToHit':0, 'longToHit':0, 'strength':7, 'damage':'d3', 'saveMod':-4, 'ammoRoll':4,
        'cost':240,
        'energyLevels':True, 'template':True, 'blastCloud':True, 'plasmaBlast':True
    })
heavyPlasmagunHigh = ShootyWeapon({
        'weaponId':'heavyPlasmagunHigh', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':72, 'shortToHit':0, 'longToHit':0, 'strength':8, 'damage':'d6', 'saveMod':-5, 'ammoRoll':6,
        'cost':0,
        'energyLevels':True, 'template':True, 'gasCloud':False, 'plasmaBlast':True
    })
lascannon = ShootyWeapon({
        'weaponId':'lascannon', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':60, 'shortToHit':0, 'longToHit':0, 'strength':9, 'damage':'2d6', 'saveMod':-6, 'ammoRoll':2,
        'cost':300,
        'terrifyingForce':True
    })
heavyFlamer = ShootyWeapon({
        'weaponId':'heavyFlamer', 'weaponClass':'heavy',
        'shortRange':8, 'longRange':8, 'shortToHit':0, 'longToHit':0, 'strength':5, 'damage':'d3', 'saveMod':-3, 'ammoRoll':3,
        'cost':80,
        'template':True, 'flamer':True, 'ammoRoll':True, 'catchFire':3
    })
heavyStubber = ShootyWeapon({
        'weaponId':'heavyStubber', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':40, 'shortToHit':0, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-1, 'ammoRoll':4,
        'cost':120,
        'sustainedFire':2
    })
missileLauncher = ShootyWeapon({
        'weaponId':'missileLauncher', 'weaponClass':'heavy',
        'shortRange':20, 'longRange':72, 'shortToHit':0, 'longToHit':0, 'strength':0, 'damage':0, 'saveMod':0, 'ammoRoll':6,
        'cost':140,
        'missileAmmo':True
    })

dumDumBullets = ShootyWeapon({
        'weaponId':'dumDumBullets', 'weaponClass':'ammo',
        'shortRange':8, 'longRange':16, 'shortToHit':1, 'longToHit':-1, 'strength':4, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':5,
        'ammo':True, 'dumDumBullets':True
    })

solidSlug = ShootyWeapon({
        'weaponId':'solidslug', 'weaponClass':'shell',
        'shortRange':4, 'longRange':18, 'shortToHit':1, 'longToHit':-1, 'strength':4, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':0,
        'knockBack':True, 'ammo':True, 'solidSlug':True
    })
scatterShot = ShootyWeapon({
        'weaponId':'scatterShot', 'weaponClass':'shell',
        'shortRange':4, 'longRange':18, 'shortToHit':1, 'longToHit':-1, 'strength':3, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':0,
        'knockBack':False, 'ammo':True, 'scatterShot':True
    })
manstopperShell = ShootyWeapon({
        'weaponId':'manstopperShell', 'weaponClass':'shell',
        'shortRange':4, 'longRange':18, 'shortToHit':1, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':0, 'ammoRoll':4,
        'cost':5,
        'knockBack':True, 'ammo':True, 'manstopperShells':True
    })
hotShotShell = ShootyWeapon({
        'weaponId':'hotShotShell', 'weaponClass':'shell',
        'shortRange':4, 'longRange':18, 'shortToHit':1, 'longToHit':-1, 'strength':4, 'damage':1, 'saveMod':0, 'ammoRoll':6,
        'cost':5,
        'knockBack':True, 'ammo':True, 'hotShotShells':True, 'catchFire':5
    })
boltShell = ShootyWeapon({
        'weaponId':'boltShell', 'weaponClass':'shell',
        'shortRange':4, 'longRange':24, 'shortToHit':1, 'longToHit':0, 'strength':4, 'damage':1, 'saveMod':-1, 'ammoRoll':6,
        'cost':15,
        'knockBack':True, 'ammo':True, 'boltShells':True
    })

superKrakMissile = ShootyWeapon({
        'weaponId':'superKrakMissile', 'weaponClass':'missile',
        'strength':8, 'damage':'d6', 'saveMod':-5,
        'cost':50,
        'highImpact':True
    })
fragMissile = ShootyWeapon({
        'weaponId':'fragMissile', 'weaponClass':'missile',
        'strength':4, 'damage':'1', 'saveMod':-2,
        'cost':35,
        'template':True, 'gasCloud':True
    })

krakGrenade = ShootyWeapon({
        'weaponId':'krakGrenade', 'weaponClass':'grenade',
        'strength':6, 'damage':'d6', 'saveMod':-3,
        'cost':40,
        'template':False, 'demolition':True, 'toHitPenalty':True
    })
fragGrenade = ShootyWeapon({
        'weaponId':'gragGrenade', 'weaponClass':'grenade',
        'strength':5, 'damage':'1', 'saveMod':-1,
        'cost':25,
        'template':True, 'gasCloud':True
    })
meltabomb = ShootyWeapon({
        'weaponId':'meltabomb', 'weaponClass':'grenade',
        'strength':8, 'damage':'2d6', 'saveMod':-5,
        'cost':40, 'variableCost':'4d6',
        'template':False, 'demolition':True, 'demolitionOnly':True
    })
chokeGrenade = ShootyWeapon({
        'weaponId':'chokeGrenade', 'weaponClass':'grenade',
        'cost':15, 'variableCost':'2d6',
        'choke':True, 'template':True, 'gasTemplate':True
    })
scareGrenade = ShootyWeapon({
        'weaponId':'scareGrenade', 'weaponClass':'grenade',
        'cost':20, 'variableCost':'2d6',
        'scare':True, 'template':True, 'gasTemplate':True
    })
hallucinogenGrenade = ShootyWeapon({
        'weaponId':'hallucinogenGrenade', 'weaponClass':'grenade',
        'cost':40, 'variableCost':'4d6',
        'hallucinogen':True, 'template':True, 'gasTemplate':True
    })
plasmaGrenade = ShootyWeapon({
        'weaponId':'plasmaGrenade', 'weaponClass':'grenade',
        'strength':5, 'damage':'1', 'saveMod':-2,
        'cost':35, 'variableCost':'3d6',
        'template':True, 'blastTemplate':True, 'plasmaBlast':True
    })
photonFlashFlare = ShootyWeapon({
        'weaponId':'photonFlashFlare', 'weaponClass':'grenade',
        'cost':20, 'variableCost':'2d6',
        'template':True, 'blastTemplate':True, 'blinding':True
    })
smokeBomb = ShootyWeapon({
        'weaponId':'smokeBomb', 'weaponClass':'grenade',
        'cost':10, 'variableCost':'3d6',
        'template':True, 'gasTemplate':True, 'smoke':True
    })

meshArmor = Armor({
        'armorId':'mesh',
        'save':5,
        'cost':25, 'variableCost':'2d6',
    })
flakArmor = Armor({
        'armorId':'flak',
        'save':6,
        'cost':10, 'variableCost':'2d6',
        'flakSave':5
    })
carapace = Armor({
        'armorId':'carapace',
        'save':4,
        'cost':60, 'variableCost':'3d6',
        'initiativePenalty':1
    })
forceField = Armor({
        'armorId':'forceField',
        'save':0,
        'cost':100, 'variableCost':'4d6',
        'shootyOnly':True, 'forceProtection':True
    })

juve = {
    'gangerType':'juve',
    'm':4, 'ws':2, 'bs':2, 's':3, 't':3, 'w':1, 'i':3, 'a':1, 'ld':6,
    'weapons':knife,
    'cost':25
}
ganger = {
    'gangerType':'ganger',
    'm':4, 'ws':3, 'bs':3, 's':3, 't':3, 'w':1, 'i':3, 'a':1, 'ld':7,
    'weapons':knife,
    'cost':50
}
heavy = {
    'gangerType':'heavy',
     'm':4, 'ws':3, 'bs':3, 's':3, 't':3, 'w':1, 'i':3, 'a':1, 'ld':7,
     'weapons':knife,
     'cost':60
}
gangLeader = {
    'gangerType':'gangLeader',
    'm':4, 'ws':4, 'bs':4, 's':3, 't':3, 'w':1, 'i':4, 'a':1, 'ld':8,
    'weapons':knife,
    'cost':120
}
scaly = {
    'gangerType':'scaly',
    'm':4, 'ws':4, 'bs':3, 's':5, 't':4, 'w':2, 'i':2, 'a':2, 'ld':6,
    'weapons':knife,
    'cost':140
}
scavvy = {
    'gangerType':'scavvy',
    'm':4, 'ws':3, 'bs':2, 's':3, 't':3, 'w':1, 'i':3, 'a':1,
    'weapons':knife,
    'cost':25,
}

pitFighter = {
    'gangerType':'pitFighter',
    'm':4, 'ws':4, 'bs':0, 's':3, 't':3, 'w':1, 'i':4, 'a':1, 'ld':7,
    'weapons':knife,
    'cost':60
}
phases = ['movement', 'shooting', 'hand-to-hand', 'recovery']
movementPhase = ['charges', 'compulsoryMoves', 'normalMoves']
handToHandPhase = ['throwAttackDice', 'calculateCombatScore', 'determineWinner', 'numberOfHits', 'throwToWound', 'savingThrow', 'resolveInjuries']
h2HModifiers = ['opponentFumbles', 'criticalHits', 'charging', 'higherUp', 'encumbered', 'obstacle']
turns = ['player1', 'player2']
status = {'ran':False, 'hiding':False, 'overwatch':False, 'wounded':False, 'pinned':False, 'outOfAction':False, 'onFire':False, 'frenzy':False, 'stupid':False, 'broken':False, 'partialCover':False, 'cover':False, 'charging':False, 'rapidMove':False, 'smallTarget':False, 'largeTarget':False, 'wounded':False, 'down':False}

