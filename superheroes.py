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
		print("")
		print("ATTACKING!!!")
		print(str(self.name) + ": " + str(damage))
		return damage



	def update_attack(self, attack_strength):
		strength = attack_strength





class Weapon(Ability):
	def attack(self):
		damage_max = self.strength
		damage_min = 0
		damage = random.randint(damage_min, damage_max)
		print("")
		print("WEAPON ATTACK!!")
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
		print("")
		print("DEFENDING!!")
		print(str(self.name) + ": " + str(shield))
		return shield





class Team(Hero):
	def __init__(self, team_name):
		self.name = team_name
		self.heroes = list()



	def add_hero(self, hero):
		self.heroes.append(hero)



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
				defense += armor.defend()
		damage = damage_amt - defense
		damage = max(0, damage)
		killstreak = self.deal_damage(damage)
		return killstreak



	def attack(self, other_team):
		offense = 0
		for hero in self.heroes:
			for ability in hero.abilities:
				offense += ability.attack()
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





class Arena:
	def __init__(self):
		self.team_one = None
		self.team_two = None

	def rematch(self):
		while True:
			try:
				rematch = input("CONTINUE? Y/N: ")
				if (rematch == "Y"):
					print("reviving team members...")
					self.team_one.revive_heroes()
					self.team_two.revive_heroes()
					return True
				elif (rematch == "N"):
					return False
				else:
					print("Invalid Input!")
					pass
			except:
				print("Invalid Input!")
				pass

	def showdown(self):
		self.build_team_two()
		self.build_team_one()
		self.team_battle()
		self.show_stats()

	def build_team_one(self):
		print('''
====================================
~ CREATE A SUPERVILLAIN DREAM TEAM ~
====================================
''')
		self.team_one = Team("new_team")
		self.create_heroes()
		print("Name your new team!")
		self.team_one.name = input("Input Team Name: ")



	def build_team_two(self):
		print('''
=================================
~ CREATE A SUPERHERO DREAM TEAM ~
=================================
''')
		self.team_one = Team("new_team")
		self.create_heroes()
		print("Name your new team!")
		self.team_two = self.team_one # the functions overwrite team1... which is bad... but if i do team2 first its all good
		self.team_two.name = input("Input Team Name: ")


	def team_battle(self):
		fight_text = '''
=================
~ TIME TO FIGHT ~
=================
'''
		tie_text = '''
o=o=o=o=o=o=o=o=o=o=o
     IT'S A TIE!
o=o=o=o=o=o=o=o=o=o=o
'''
		win_text = f'''
o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o
     {self.team_one.name} won!
o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o
'''
		lose_text = f'''
o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o
     {self.team_two.name} won!
o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o
'''
		while True:
			team1_hp = 0
			team2_hp = 0
			for hero in self.team_one.heroes:
				team1_hp += int(hero.health)
			for hero in self.team_two.heroes:
				team2_hp += int(hero.health)
			if team1_hp == 0 and team2_hp == 0:
				print(tie_text)
				if self.rematch():
					pass
				else:
					print("= GAME OVER =")
					return False
			elif team1_hp == 0:
				print(lose_text)
				if self.rematch():
					pass
				else:
					print("= GAME OVER =")
					return False
			elif team2_hp == 0:
				print(win_text)
				if self.rematch():
					pass
				else:
					print("= GAME OVER =")
					return False
			else:
				print("")
				print("################")
				print(self.team_one.name)
				for hero in self.team_one.heroes:
					print("==> " + hero.name + ": " + str(hero.health) + " HP")
				print("")
				print("################")
				print(self.team_two.name)
				for hero in self.team_two.heroes:
					print("==> " + hero.name + ": " + str(hero.health) + " HP")
				print("")
				print("ANOTHER ROUND?!?")
				self.fight()


	def fight(self):
		rand = random.randint(0,1)
		print(rand)
		if rand == 0:
			self.team_one.attack(self.team_two)
			self.team_two.attack(self.team_one)
		else:
			self.team_two.attack(self.team_one)
			self.team_one.attack(self.team_two)

	def show_stats(self):
		print("...")
		print("displaying stats")
		print("")
		print("################")
		print(self.team_one.name)
		for hero in self.team_one.heroes:
			print("==> " + hero.name + ": K/D " + str(hero.kills) + "/" + str(hero.deaths) + " = " + str(hero.kills/(hero.deaths + 1)))
		print("")
		print("################")
		print(self.team_two.name)
		for hero in self.team_two.heroes:
			print("==> " + hero.name + ": K/D " + str(hero.kills) + "/" + str(hero.deaths) + " = " + str(hero.kills/(hero.deaths + 1)))
		print("")




	def create_heroes(self):
		persist = True
		while persist:
			print(f"{len(self.team_one.heroes)} heroes are signed up on this team...")
			for hero in self.team_one.heroes: # This is difficult because I want to use this for team_two as well... 
			                                  # Imma do something funky so hold on to your seats. See build_team_two()
				print("==> " + hero.name)
			print("")

			validator = True # validator turns off when valid data is entered
			while validator:
				hero_input = input("Add a new Hero? (Y/N): ")

				if hero_input == "Y":
					validator = False
					print('''
+ - - - - - - - - - - +
| CREATING A NEW HERO |
+ - - - - - - - - - - +
''')
					hero_name = input("Input a new hero name: ")
					validator2 = True
					while validator2:
						try:
							hero_health = int(input(f"Input {hero_name}'s HP: "))
							validator2 = not(isinstance(hero_health, int))
						except:
							print("Invalid Input!")
							pass
					print("")
					hero = Hero(hero_name, hero_health)
					self.team_one.add_hero(hero)
					self.create_abilities(hero)
					self.create_weapons(hero)
					self.create_armor(hero)

				elif hero_input == "N":
					validator = False
					persist = False

				else:
					print("Invalid Input!")



	def create_abilities(self,hero):
		persist = True
		while persist:
			print(f"{hero.name} currently has {len(hero.abilities)} super-powers...")
			for ability in hero.abilities:
				print("==> " + ability.name + ": " + str(ability.strength))
			print("")

			validator = True # validator turns off when valid data is entered
			while validator:
				ability_input = input("Add a new super-power? (Y/N): ")
				if ability_input == "Y":
					print('''
+ - - - - - - - - - - - - - -+
| CREATING A NEW SUPER-POWER |
+- - - - - - - - - - - - - - +
''')
					validator = False
					ability_name = input("Input a new super-power: ")
					validator2 = True
					while validator2:
						try:
							ability_power = int(input(f"Input {ability_name}'s power: "))
							validator2 = not(isinstance(ability_power, int))
						except:
							print("Invalid Input!")
							pass
					print("")
					ability = Ability(ability_name, ability_power)
					hero.add_ability(ability)

				elif ability_input == "N":
					validator = False
					persist = False

				else:
					print("Invalid Input!")



	def create_weapons(self,hero):
		persist = True
		while persist:
			print(f"{hero.name} currently has {len(hero.abilities)} mega-weapons...")
			for weapon in hero.abilities:
				print("==> " + weapon.name + ": " + str(weapon.strength))
			print("")

			validator = True # validator turns off when valid data is entered
			while validator:
				weapon_input = input("Add more weapons? (Y/N): ")
				if weapon_input == "Y":
					print('''
+ - - - - - - - - - - - - - -+
| CREATING A NEW MEGA-WEAPON |
+- - - - - - - - - - - - - - +
''')
					validator = False
					weapon_name = input("Input a new mega-weapon: ")
					validator2 = True
					while validator2:
						try:
							weapon_power = int(input(f"Input {weapon_name}'s power: "))
							validator2 = not(isinstance(weapon_power, int))
						except:
							print("Invalid Input!")
							pass

					print("")
					weapon = Weapon(weapon_name, weapon_power)
					hero.add_ability(weapon)

				elif weapon_input == "N":
					validator = False
					persist = False

				else:
					print("Invalid Input!")


	def create_armor(self,hero):
		persist = True
		while persist:
			print(f"{hero.name} currently has {len(hero.armors)} armor pieces...")
			for armor in hero.armors:
				print("==> " + armor.name + ": " + str(armor.defense))
			print("")

			validator = True # validator turns off when valid data is entered
			while validator:
				armor_input = input("Add a new set of armor? (Y/N): ")
				if armor_input == "Y":
					print('''
+ - - - - - - - - - - - - - - +
| CREATING A NEW SET OF ARMOR |
+ - - - - - - - - - - - - - - +
''')
					validator = False
					armor_name = input("Input a new piece of armor: ")
					validator2 = True
					while validator2:
						try:
							armor_strength = int(input(f"Input {armor_name}'s strength: "))
							validator2 = not(isinstance(armor_strength, int))
						except:
							print("Invalid Input!")
							pass

					print("")
					armor = Armor(armor_name, armor_strength)
					hero.add_armor(armor)

				elif armor_input == "N":
					validator = False
					persist = False

				else:
					print("Invalid Input!")



if __name__ == "__main__":
	Arena().showdown()

