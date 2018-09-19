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

	def take_damage(self, damage_amt): ## Check if alive at beginning
		if self.health > 0:
			is_alive = True
		else:
			is_alive = False

		damage = damage_amt - self.defend()
		self.health -= damage
		self.health = max(0, self.health)

		if self.health == 0 and is_alive:
			self.deaths += 1
			print(str(self.name) + " died!!")
			return 1
		else:
			return 0

	def add_kill(self, num_kills):
		self.kills += num_kills

	def display(self):
		print(self.name)



class Ability:
	def __init__(self, name, attack_strength):
		self.name = name
		self.strength = attack_strength

	def attack(self):
		damage_max = self.strength
		damage_min = self.strength // 2
		damage = random.randint(damage_min, damage_max)
		print(str(self.name) + ": " + str(damage))
		return damage

	def update_attack(self, attack_strength):
		strength = attack_strength



class Weapon(Ability):
	def attack(self):
		damage_max = self.strength
		damage_min = 0
		damage = random.randint(damage_min, damage_max)
		print(str(self.name) + ": " + str(damage))
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
		print("REMOVING TEAM HEROES")
		found_hero = False
		for hero in self.heroes:
			if(hero.name == name):
				print("this hero: " + str(hero.name))
				index = self.heroes.index(hero)
				self.heroes.pop(index)
		print("None Found :(")
		return 0

	def find_hero(self, name):
		print("FINDING TEAM HEROES")
		for hero in self.heroes:
			if(hero.name == name):
				print(hero.name)
				return hero
		print("None Found :(")
		return 0

	def view_all_heroes(self):
		print("VIEW HEROES IN TEAM")
		for hero in self.heroes:
			hero.display()

	def deal_damage(self, damage_amt):
		killstreak = 0
		if len(self.heroes) != 0:
			team_size = 0
			for hero in self.heroes:
				if hero.health != 0:
					team_size += 1
			damage = damage_amt // team_size
		for hero in self.heroes:
			killstreak += hero.take_damage(damage) #RECURSIVE
			# hero.health -= damage
			# hero.health = max(0, hero.health)
			# if hero.health == 0:
			#   killstreak += 1
		return killstreak

	def defend(self, damage_amt):
		defense = 0
		for hero in self.heroes:
			for armor in hero.armors:
				defense += Armor.defend(armor)
		damage = damage_amt - defense
		damage = max(0, damage)
		killstreak = self.deal_damage(damage) #RECURSIVE
		return killstreak

	def attack(self, other_team):
		offense = 0
		for hero in self.heroes:
			for ability in hero.abilities:
				offense += Ability.attack(ability)
		killstreak = other_team.defend(offense) ### HOW TO GET OTHER TEAM TO DEFEND?
		killstreak_counter = killstreak
		while killstreak_counter > 0:
			self.update_kills()
			killstreak_counter -= 1
		return killstreak

	def revive_heroes(self):
		for hero in self.heroes:
			hero.health = hero.start_health

	def stats(self):
		for hero in self.heroes:
			print(str(hero.name)+": "+ str(hero.kills/hero.deaths))

	def update_kills(self):
		for hero in self.heroes:
			if hero.health > 0:
				hero.kills += 1

if __name__ == "__main__":
	hero = Hero("Wonder Woman")
	ability = Ability("Divine Speed", 300)
	hero.add_ability(ability)
	new_ability = Ability("Super Human Strength", 800)
	hero.add_ability(new_ability)

	team_one = Team("One")
	team_two = Team("Two")

	jodie = Hero("Jodie Foster")
	athena = Hero("Athena")

	team_one.add_hero(jodie)
	team_one.add_hero(hero)
	team_two.add_hero(athena)
	team_one.remove_hero("jodie")
	socks = Armor("Socks", 10)
	aliens = Ability("Alien Friends", 10000)

	jodie.add_ability(aliens)
	athena.add_armor(socks)

	print("team 1: " + str(Team("One").name))
	print("team 2: " + str(Team("Two").name))
	team_one.attack(team_two)
	print("STATS")
	Team("Two").stats()
	team_one.view_all_heroes()

