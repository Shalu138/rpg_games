 # here we will define
import random

 class Bcolors:

     HEADER = '\033[95m'
     OKBLUE = '\033[94m'
     OKGREEN = '\033[92m'
     WARNING = '\033[93m'
     FAIL = '\033[91m'
     ENDC = '\033[0m'
     BOLD = "\033[1m"
     UNDERLINE = "\033[4m"


 class Person:

     def __init__(self, name, hp, mp, atk, df, magic, items):
         self.maxhp = hp
         self.hp = hp
         self.maxmp = mp
         self.mp = mp
         self.atkl = atk - 10
         self.atkh = atk + 10
         self.df = df
         self.magic = magic
         self.items = items
         self.actions = ["Attack", "Magic", "Items"]
         self.name = name

      # for generating damage we will import random

     def generate_damage(self):
         return random.randrange(self.atkl, self.atkh)

     def take_damage(self, dmg):
         self.hp -= dmg
         if self.hp < 0:
             self.hp = 0
         return self.hp

     def heal(self, dmg):
         self.hp += dmg
         if self.hp > self.maxhp:
             self.hp = self.maxhp

     # Utility Classes

     def get_hp(self):
         return self.hp

     def get_max_hp(self):
         return self.maxhp

     def get_mp(self):
         return self.mp

     def get_max_mp(self):
         return self.maxmp

     def reduced_mp(self, cost):
         self.mp -= cost

     ''' def get_actions_name(self, i):
         return self.actions[i][i] '''


     def choose_actions(self):
         i = 1
         print("\n", Bcolors.BOLD + "    " + self.name + Bcolors.ENDC)
         print(Bcolors.OKBLUE + Bcolors.BOLD + "     ACTIONS:" + Bcolors.ENDC)
         for item in self.actions:
             print("        ", str(i), ":", item)
             i += 1

     def choose_magic(self):
         i = 1

         print(Bcolors.OKBLUE + Bcolors.BOLD + "\n" + "     MAGIC:" + Bcolors.ENDC)
         for spell in self.magic:
             print("        ", str(i), ":", spell.name, "(Cost:", str(spell.cost) + ")")
             i += 1

     def choose_items(self):
         i = 1
         print(Bcolors.OKGREEN + Bcolors.BOLD + "\n" + "     ITEMS:" + Bcolors.ENDC)
         for item in self.items:
             print("        ", str(i), item["item"].name, ":", item["item"].description,
                   "(x" + str(item["quantity"]) +")")
             i += 1

     def choose_target(self, enemies):
         i = 1
         print("\n" + Bcolors.BOLD + Bcolors.FAIL + "    TARGET:" + Bcolors.ENDC)
         for enemy in enemies:
             if enemy.get_hp() != 0:
                 print("        ", str(i), ".", enemy.name)
                 i += 1

         choice = int(input("    Choose target:")) - 1
         return choice                           # so enemy is choice

     def get_enemy_stats(self):
         hp_bar = ""
         bar_ticks = (self.hp / self.maxhp) * 100 / 2

         while bar_ticks > 0:
             hp_bar += "█"
             bar_ticks -= 1

         while len(hp_bar) < 50:
              hp_bar += " "

         hp_string = str(self.hp) + "/" + str(self.maxhp)
         current_hp = ""

         if len(hp_string) < 11:
             decreased = 11 - len(hp_string)

             while decreased > 0:
                 current_hp += " "
                 decreased -= 1

             current_hp += hp_string
         else:
             current_hp = hp_string

         print("                                ___________________________________________________"
               "____________________________")
         print(Bcolors.BOLD + self.name + "               " + current_hp +
               "|" + Bcolors.FAIL + hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|" + Bcolors.ENDC)

     def get_stats(self):
         hp_bar = ""
         bar_ticks = (self.hp / self.maxhp) * 100 / 4

         while bar_ticks > 0:
             hp_bar += "█"
             bar_ticks -= 1

         while len(hp_bar) < 25:
             hp_bar += " "

         mp_bar = ""
         mp_ticks = (self.hp / self.maxhp) * 100 / 10

         while mp_ticks > 0:

             mp_bar += "█"
             mp_ticks -= 1

         while len(mp_bar) < 10:
             mp_bar += " "

         hp_string = str(self.hp) + "/" + str(self.maxhp)
         current_hp = ""

         if len(hp_string) < 9:
             decreased = 9 - len(hp_string)

             while decreased > 0:
                 current_hp += " "
                 decreased -= 1

             current_hp += hp_string
         else:
             current_hp = hp_string

         mp_string = str(self.mp) + "/" + str(self.maxmp)
         current_mp = ""

         if len(mp_string) < 7:
             decreased = 7 - len(mp_string)

             while decreased > 0:
                 current_mp += " "
                 decreased -= 1
             current_mp += mp_string
         else:
             current_mp = mp_string

         print("                               _________________________                             __________")
         print(Bcolors.BOLD + self.name + "               " + current_hp +
               "|" + Bcolors.OKGREEN + hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|" + Bcolors.ENDC
               + "      " + current_mp + "|" + Bcolors.OKBLUE + mp_bar + Bcolors.ENDC +
               Bcolors.BOLD + "|" + Bcolors.ENDC)

     def choose_enemy_spell(self):
         magic_choice = random.randrange(0, len(self.magic))
         spell = self.magic[magic_choice]
         magic_dmg = spell.generate_damage()
         print("Enemy Magic dmg:", magic_dmg)

         pct = self.mp / self.maxmp * 100
         # Mp < Cost, gonna check again if any spell is available at that cost
         if self.mp < spell.cost or spell.type == "white" and pct > 50:
             self.choose_enemy_spell()
         else:
             return spell






















