from dataclasses import dataclass

@dataclass
class EnemyStats:
    health: int
    damage: int
    speed: int
    fat: int = 100

@dataclass
class Enemy:
    stats: EnemyStats
    weapons: list[str]
    name: str

class UgaBugaFactory:
    def __init__(self, name):
        self.name = name

    def build(self):
        stats = EnemyStats(100, 80, 2, 4_000)
        enem = Enemy(stats, ['sword', 'lauchstange'], self.name)

        return enem

