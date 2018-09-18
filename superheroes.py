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
		print("")
		print("")
		print("===============================")
		print("ADDING ABILITY: " + str(ability.name))
		self.abilities.append(ability)

	def add_armor(self, armor):
		print("")
		print("")
		print("==============================")
		print("ADDING ARMOR: " + str(armor.name))
		self.armors.append(armor)

	def attack(self):
		print("")
		print("")
		print("=================")
		print("HERO IS ATTACKING")
		total = 0	
		if self.health == 0:
			return total
			print("total: " + str(total))
		else:
			for item in self.abilities:
				total += Ability.attack(item)
			print("total: " + str(total))
			return total


	def defend(self):
		print("")
		print("")
		print("=================")
		print("HERO IS DEFENDING")
		total = 0	
		if self.health == 0:
			return total
		else:
			for item in self.armors:
				total += Armor.defend(item)
			return total

	def take_damage(self, damage_amt):
		print("")
		print("")
		print("===================")
		print("HERO TAKING DAMAGE!")
		damage_amt -= defend()
		self.health -= damage_amt
		self.health = max(0, self.health)
		if self.health == 0:
			self.deaths += 1
		return health

	def add_kill(self, num_kills):
		print("")
		print("")
		print("================")
		print("HERO ADDS A KILL")
		self.kills += num_kills



class Ability:
	def __init__(self, name, attack_strength):
		self.name = name
		self.strength = attack_strength

	def attack(self):
		print("- - - - - - -")
		print("Using Ability")
		damage_max = self.strength
		damage_min = self.strength // 2
		damage = random.randint(damage_min, damage_max)
		print(str(self.name) + ": " + str(damage))
		return damage

	def update_attack(self, attack_strength):
		strength = attack_strength



class Weapon(Ability):
	def attack(self):
		print("- - - - - - -")
		print("Using Weapons")
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
		print("- - - - - -")
		print("Using Armor")
		shield_max = self.defense
		shield_min = 0
		shield = random.randint(shield_min, shield_max)
		print(str(self.name) + ": " + str(shield))
		return shield



class Team(Hero):
	def __init__(self, team_name):
		self.name = team_name
		self.heroes = list()

	def add_hero(self, Hero):
		print("")
		print("")
		print("===========")
		print("ADDING HERO")
		self.heroes.append(Hero)
		print("added heroes: "+str(self.heroes))

	def remove_hero(self, name): # NEEDS REFACTORED
		print("")
		print("")
		print("=============")
		print("REMOVING HERO")
		found_hero = False
		for hero in self.heroes:
			if(hero.name == name):
				print("this hero: " + str(hero.name))
				index = self.heroes.index(hero)
				self.heroes.pop(index)
		print("None Found :(")
		return 0

	def find_hero(self, name):
		print("")
		print("")
		print("===================")
		print("FINDING TEAM HEROES")
		for hero in self.heroes:
			if(hero.name == name):
				print(hero.name)
				return hero
		print("None Found :(")
		return 0

	def view_all_heroes(self):
		print("")
		print("")
		print("===================")
		print("VIEW HEROES IN TEAM")
		for hero in self.heroes:
			print(hero)

	def deal_damage(self, damage_amt):
		print("")
		print("")
		print("==========================")
		print("HEROES DOLLING THE DAMAGE!")
		killstreak = 0
		print(self.heroes)
		if len(self.heroes) != 0:
			damage = damage_amt // len(self.heroes)
			print("damage: " + str(damage))
		for hero in self.heroes:
			hero.health -= damage
			hero.health = max(0, hero.health)
			if hero.health == 0:
				killstreak += 1
		return killstreak

	def defend(self, damage_amt, other_team):
		print("")
		print("")
		print("=================")
		print("TEAM IS DEFENDING")
		print("DAMAGE: "+str(damage_amt)) ###TESTING
		defense = 0
		for hero in self.heroes:
			for armor in hero.armors:
				defense += Armor.defend(armor)
		damage = damage_amt - defense
		damage = max(0, damage)
		killstreak = other_team.deal_damage(damage)
		print("KILLS: "+str(killstreak)) ###TESTING
		return killstreak

	def attack(self, other_team):
		print("")
		print("")
		print("=================")
		print("TEAM IS ATTACKING")
		offense = 0
		for hero in self.heroes:
			for ability in hero.abilities:
				offense += Ability.attack(ability)
		print("- - - - - - -")
		print(" OUR TEAM:  "+str(self.name))
		print("THEIR TEAM: "+str(other_team.name))
		killstreak = other_team.defend(offense, other_team) ### HOW TO GET OTHER TEAM TO DEFEND?
		killstreak_counter = killstreak
		while killstreak_counter > 0:
			self.update_kills()
			killstreak_counter -= 1
		return killstreak

		"""
		This method should total our teams attack strength 
		and call the defend() method on the rival team that 
		is passed in.

		It should call update_kills() on each hero with the number
		of kills made.
		"""

	def revive_heroes(self, health=100):
		for hero in self.heroes:
			hero.health = health

	def stats(self):

		"""
		This method should print the ratio of kills/deaths
		for each member of the team to the screen. 

		This data must be output to the terminal.
		"""

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

