import random



class Hero:
	def __init__(self, name):
		self.name = name
		self.abilities = list()

	def add_ability(self, ability):
		self.abilities.append(ability) ### CRITICAL POINT

	def attack(self):
		total = 0
		for item in self.abilities:
			total += Ability.attack(item)
		return total



class Ability:
	def __init__(self, name, attack_strength):
		self.ability = name
		self.strength = attack_strength

	def attack(self):
		damage_max = self.strength
		damage_min = self.strength // 2
		damage = random.randint(damage_min, damage_max)
		return damage

	def update_attack(self, attack_strength):
		strength = attack_strength



if __name__ == "__main__":
	hero = Hero("Wonder Woman")
	print("HERO ATTACK: " + str(hero.attack()))

	ability = Ability("Divine Speed", 300)
	hero.add_ability(ability)
	print("HERO ATTACK: " + str(hero.attack()))

	new_ability = Ability("Super Human Strength", 800)
	hero.add_ability(new_ability)
	print("HERO ATTACK: " + str(hero.attack()))
