import random



class Hero:
	def __init__(self, name):
		self.name = name
		self.abilities = list()

	def add_ability(self, ability):
		self.abilities.append(ability)

	def attack(self):
		total = 0
		for item in self.abilities:
			total += Ability.attack(item)
		return total



class Ability:
	def __init__(self, name, attack_strength):
		self.name = name
		self.strength = attack_strength

	def attack(self):
		damage_max = self.strength
		damage_min = self.strength // 2
		damage = random.randint(damage_min, damage_max)
		return damage

	def update_attack(self, attack_strength):
		strength = attack_strength



class Weapon(Ability):
	def attack(self):
		damage_max = self.strength
		damage_min = 0
		damage = random.randint(damage_min, damage_max)
		return damage



class Team(Hero):
	def __init__(self, team_name):
		self.name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		self.heroes.append(Hero)

	def remove_hero(self, name): # NEEDS REFACTORED
		found_hero = False
		for hero in self.heroes:
			print("this hero: " + str(hero.name))
			if(hero.name == name):
				index = self.heroes.index(hero)
				self.heroes.pop(index)
		return 0

	def find_hero(self, name):
		for hero in self.heroes:
			if(hero.name == name):
				print(hero.name)
				return hero
		return 0

	def view_all_heroes(self):
		for hero in self.heroes:
			print(hero.name)


if __name__ == "__main__":
	hero = Hero("Wonder Woman")
	print("HERO ATTACK: " + str(hero.attack()))

	ability = Ability("Divine Speed", 300)
	hero.add_ability(ability)
	print("HERO ATTACK: " + str(hero.attack()))

	new_ability = Ability("Super Human Strength", 800)
	hero.add_ability(new_ability)
	print("HERO ATTACK: " + str(hero.attack()))
	print("""== nice job ==

""")