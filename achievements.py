from typing import List, Dict, NamedTuple, Optional
from pygame import Surface


class Achievement:
    def __init__(self, id: str, name: str, desc: str, desc2: Optional[str] = None, unlocked: bool = False, image: Optional[Surface] = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.desc2 = desc2 or desc
        self.unlocked = unlocked
        self.image = image


achievements: List[Achievement] = [
    Achievement(
        id="ACH_GOLD_MEDAL",
        name="No Way? No Way!",
        desc="Collect gold medallions in Blue Spheres Bonus stage",
        desc2="Collected all gold medallions in Bonus stage"
    ),
    Achievement(
        id="ACH_SILVER_MEDAL",
        name="Full Medal Jacket",
        desc="Collect silver medallions in Blue Spheres Bonus stage",
        desc2="Collected all silver medallions in Bonus stage"
    ),
    Achievement(
        id="ACH_EMERALDS",
        name="Magnificent Seven",
        desc="Collect all seven Chaos Emeralds",
        desc2="Collected all seven Chaos Emeralds"
    ),
    Achievement(
        id="ACH_GAME_CLEARED",
        name="See You Next Game",
        desc="Achieve any ending",
        desc2="Beat the game (any ending)"
    ),
    Achievement(
        id="ACH_STARPOST",
        name="Superstar",
        desc="Spin the Star Post!",
        desc2="Spun a Star Post 10 times by going fast"
    ),
    Achievement(
        id="ACH_SIGNPOST",
        name="That's a Two-fer",
        desc="Find the hidden item boxes at the end of the Zone",
        desc2="Uncovered two item boxes with a single Goal Plate"
    ),
    Achievement(
        id="ACH_GHZ",
        name="Now It Can't Hurt You Anymore",
        desc="What would happen if you cross a bridge with a fire shield?",
        desc2="Burnt a log bridge in Green Hill Zone"
    ),
    Achievement(
        id="ACH_CPZ",
        name="Triple Trouble",
        desc="Try for a 3 chain combo!",
        desc2="Got a 3 chain combo in Chemical Plant Act 2 or in Mean Bean mode"
    ),
    Achievement(
        id="ACH_SPZ",
        name="The Most Famous Hedgehog in the World",
        desc="Have your photos taken in Studiopolis Zone",
        desc2="Had Shutterbug take 10 photos"
    ),
    Achievement(
        id="ACH_FBZ",
        name="Window Shopping",
        desc="Let the wind take you through",
        desc2="Flown through a ship window in Flying Battery Zone Act 2"
    ),
    Achievement(
        id="ACH_PGZ",
        name="Crate Expectations",
        desc="Wreak havoc at the propaganda factory",
        desc2="Found the hidden room in Press Garden Zone and destroyed all breakable crates as Sonic"
    ),
    Achievement(
        id="ACH_SSZ",
        name="King of Speed",
        desc="Get through Stardust Speedway Zone as quickly as possible",
        desc2="Got to the Stardust Speedway Zone Act 2 tower in under a minute"
    ),
    Achievement(
        id="ACH_HCZ",
        name="Boat Enthusiast",
        desc="We really like boats",
        desc2="Found and rode all the boats in Hydrocity Zone Act 1"
    ),
    Achievement(
        id="ACH_MSZ",
        name='The Password is "Special Stage"',
        desc="Try pushing a barrel to see how far it goes",
        desc2="Found the barrel that leads to a Special Ring in Mirage Saloon Zone Act 2"
    ),
    Achievement(
        id="ACH_OOZ",
        name="Secret Sub",
        desc="You might have to submerge to find it",
        desc2="Found the secret submarine in Oil Ocean Zone Act 2"
    ),
    Achievement(
        id="ACH_LRZ",
        name="Without a Trace",
        desc="Barrel through the lava, don't let anything stop you",
        desc2="Defeated a Rexon with the Walker Legs in Lava Reef Zone"
    ),
    Achievement(
        id="ACH_MMZ",
        name="Collect 'Em All",
        desc="Gotta gacha 'em all",
        desc2="Activated and destroyed eight simultaneous Eggmins during Metallic Madness Zone Act 2"
    ),
    Achievement(
        id="ACH_TMZ",
        name="Professional Hedgehog",
        desc="That elusive perfect run, only a professional can achieve",
        desc2="Beat Titanic Monarch Zone Act 1 without taking a single hit"
    )
]
