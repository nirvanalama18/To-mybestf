"""
Project: SisterForever v1.0
Author: Loving Younger Sibling
Description: A tribute system dedicated to my elder sister.
"""

from datetime import datetime
from typing import Final


class ElderSister:
    """
    Represents the most important human in my life.
    """

    ROLE: Final[str] = "Mentor | Protector | Best Friend | Forever Hero"

    def __init__(self, name: str):
        self.name = name
        self.missed_days = 0
        self.memories = []
        self.gratitude_level = float("inf")

    def miss_you(self):
        self.missed_days += 1
        return f"Day {self.missed_days}: I miss you more than words can compile."

    def add_memory(self, memory: str):
        self.memories.append(memory)

    def express_gratitude(self):
        return (
            f"Dear {self.name},\n"
            "Thank you for being my strength when I was weak,\n"
            "my guide when I was lost,\n"
            "and my light when everything felt dark.\n"
            "Your love is my lifetime dependency.\n"
        )

    def unconditional_love(self):
        return "LoveStatus: CONSTANT\nBond: UNBREAKABLE\nDistance: IRRELEVANT"


if __name__ == "__main__":
    sister = ElderSister("My Amazing Sister")

    sister.add_memory("Late night talks and endless laughter.")
    sister.add_memory("Your advice that changed my life.")
    sister.add_memory("Every sacrifice you made silently.")

    print(sister.miss_you())
    print()
    print(sister.express_gratitude())
    print(sister.unconditional_love())

    print("\nSystem Status:")
    print(f"Memories Stored: {len(sister.memories)}")
    print("Gratitude Level:", sister.gratitude_level)
    print("Last Updated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
