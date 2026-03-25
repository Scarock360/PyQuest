ITEM_INDEX={
    # region ------ CONSUMABLES
    "Lesser Potion":{
        "tags":["battle","map","restorative","one-use"],
        "restorative":"3d4",
        "Description":"A small bottle of opaque, red liquid.\nDrinking this restores 3d4 hit points."
    },
    "Potion":{
        "tags":["battle","map","restorative","one-use"],
        "restorative":"6d4",
        "Description":"A bottle of opaque, red liquid.\nDrinking this restores 6d4 hit points."
    },
    "Greater Potion":{
        "tags":["battle","map","restorative","one-use"],
        "restorative":"12d4",
        "Description":"A large bottle of opaque, red liquid.\nDrinking this restores 12d4 hit points."
    },
    "Bedroll":{
        "tags":["map","rest","one-use"],
        "rest":"50",
        "Description":"A comfortable bed that is impossible to pack way after use.\nThis allows resting away from a rest point at 50% efficacy."
    },
    "Molotov":{
        "tags":["battle","grenade","one-use"],
        "grenade":{"amount":"3d4","type":"Fire"},
        "Description":"A bottle of clear, yellow liquid with a rag.\nThrowing this at an enemy deals 3d4 fire damage."
    },
    # endregion
    # region  ------ WEAPONS
    "Caduceus": {
        "tags":["2h_weapon","battle","map","restorative"],
        "weapon": {"damage":"3d6","accuracy": 100,"damage_type":"Magic"},
        "restorative":"2d6",
        "Description": "A wooden staff, infused with latent restorative magic.\nAs a weapon it deals 3d6 magic damage."
    },
    "War axe":{
        "tags":["1h_weapon"],
        "weapon": {"damage":"1d6","accuracy": 80,"damage_type":"Slash"},
        "Description": "This axe, while simple, is still capable of killing.\nAs a weapon it deals 1d6 slashing damage."
    },
    "Dagger":{
        "tags":["1h_weapon"],
        "weapon": {"damage":"1d4","accuracy": 110,"damage_type":"Stab"},
        "Description": "A simple dagger.\nAs a weapon it deals 1d4 slashing damage."
    },
    "Rusty lance":{
        "tags":["2h_weapon"],
        "weapon": {"damage":"2d6","accuracy": 90,"damage_type":"Stab"},
        "Description": "A rusted lance dredged from the sewer.\nAs a weapon it deals 2d6 stabbing damage."
    },
    "Battle axe":{
        "tags":["2h_weapon"],
        "weapon": {"damage":"1d12","accuracy": 90,"damage_type":"Slash"},
        "Description": "A Battle axe forged for war.\nAs a weapon it deals 2d6 slashing damage."
    },
    # endregion
    # region  ------ ARMOUR
    "Simple shield":{
        "tags":["shield"],
        "resilience": 5,
        "Description": "This shield makes you more resilient\nthough it costs you your ability to wield great weapons."
    },
    "Pocket lint":{
        "tags":[],
        "Description": "There is always some lint in your pocket\nyou can never escape it."
    },
    "Leather helm":{
        "tags":["head","armour"],
        "resilience":2,
        "Description": "A simple leather helm.\nProvides additional resilience when equipped."
    },
    "Leather cuirass":{
        "tags":["body","armour"],
        "resilience":2,
        "Description": "A simple leather cuirass.\nProvides additional resilience when equipped."
    },
    "Simple ring 1":{
        "tags":["ring","armour"],
        "agility":2,
        "Description": "A simple ring.\nProvides additional agility when equipped."
    },
    "Simple ring 2":{
        "tags":["ring","armour"],
        "agility":2,
        "Description": "A simple ring.\nProvides additional agility when equipped."
    },
    "Simple amulet":{
        "tags":["amulet","armour"],
        "power":2,
        "Description": "A simple amulet.\nProvides additional power when equipped."
    },
    # endregion
}