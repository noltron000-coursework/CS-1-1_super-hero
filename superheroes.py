import random



class Hero:
	def __init__(self, name, health=100):
		self.name = name
		self.abilities = list()
		self.armors = list()
		self.start_health = health
		self.health = health
		self.deaths = 0
		self.kills = 0

	def add_ability(self, ability):
		self.abilities.append(ability)

	def add_armor(self, armor):
		self.armors.append(armor)

	def attack(self):
		total = 0	
		if self.health == 0:
			return total
		else:
			for item in self.abilities:
				total += Ability.attack(item)
			return total

	def defend(self):
		total = 0	
		if self.health == 0:
			return total
		else:
			for item in self.armors:
				total += Armor.defend(item)
			return total

	def take_damage(self, damage_amt):
		damage_amt -= defend()
		self.health -= damage_amt
		self.health = max(0, self.health)
		if self.health == 0:
			self.deaths += 1
		return health

	def add_kill(self, num_kills):
		self.kills += num_kills



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



class Armor(Ability):
	def __init__(self, name, defense):
		self.name = name
		self.defense = defense

	def defend(self):
		shield_max = self.defense
		shield_min = 0
		shield = random.randint(shield_min, shield_max)
		return shield



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
			print(hero)

	def attack(self, other_team):
		"""
		This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

		It should call add_kill() on each hero with the number of kills made.
		"""

	def defend(self, damage_amt):
		"""
		This method should calculate our team's total defense.
		Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

		Return number of heroes killed in attack.
		"""

	def deal_damage(self, damage):
		"""
		Divide the total damage amongst all heroes.
		Return the number of heros that died in attack.
		"""

	def revive_heroes(self, health=100):
		"""
		This method should reset all heroes health to their
		original starting value.
		"""

	def stats(self):
		"""
		This method should print the ratio of kills/deaths for each member of the team to the screen. 

		This data must be output to the terminal.
		"""

	def update_kills(self):
		"""
		This method should update each hero when there is a team kill.
		"""

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