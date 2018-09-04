 from classes.game import Bcolors, Person
 from classes.magic import Spell
 from classes.inventory import items
 import random


 # Black Magic Spells
 fire = Spell("Fire", 25, 600, "black")
 thunder = Spell("Thunder", 25, 600, "black")
 blizzard = Spell("Blizzard", 25, 600, "black")
 meteor = Spell("Meteor", 40, 1200, "black")
 quake = Spell("Quake", 14, 140, "black")

 # White Magic
 cure = Spell("Cure", 25, 620, "white")
 cura = Spell("Cura", 32, 1500, "white")
 curaga = Spell("Curaga", 50, 6000, "white")


 # Inventory Items
 potion = items("Potion", "potion", "Heals 50 HP.", 50)
 hipotion = items("Hi-potion", "potion", "Heals 100 HP.", 100)
 superpotion = items("Super Potion", "potion", "Heals 1000 HP.", 1000)
 elixir = items("Elixir", "elixir", "Fully restores HP/MP of one party member.", 9999)
 hielixir = items("MegaElixir", "elixir", "Fully restores party's HP/MP.", 9999)

 # Item that cause damage
 grenade = items("Grenade", "attack", "Deals 500 damage.", 500)

 # list of player's spell and items.
 player_spells = [fire, thunder, blizzard, meteor, cure, cura]
 enemy_spells = [fire, meteor, curaga]
 player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                 {"item": superpotion, "quantity": 5}, {"item": elixir, "quantity": 5},
                 {"item": hielixir, "quantity": 5}, {"item": grenade, "quantity": 5}]

 # Instantiate People
 player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
 player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
 player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)

 enemy1 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
 enemy2 = Person("Magus", 18200, 701, 525, 25, enemy_spells, [])
 enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])


 players = [player1, player2, player3]
 enemies = [enemy1, enemy2, enemy3]

 running = True
 i = 0

 print(Bcolors.FAIL + Bcolors.BOLD + "\nAN ENEMY ATTACKS!!" + Bcolors.ENDC)

 while running:
     print("===============================")
     print("\n\n")
     print("NAME                           HP                                     MP")
     for player in players:
         player.get_stats()

     print("\n")
     for enemy in enemies:
         enemy.get_enemy_stats()

     for player in players:
         player.choose_actions()

         choice = input("     Choose Actions:")
         index = int(choice) - 1

         if index == 0:                              # it means to attack
             dmg = player.generate_damage()
             enemy = player.choose_target(enemies)            # determine who the person is attacking & will pass enemies
             enemies[enemy].take_damage(dmg)

             print("You attacked", enemies[enemy].name.replace(" ", ""), "for", dmg, "points of damage.")
             if enemies[enemy].get_hp == 0:
                 print(enemies[enemy].name.replace(" ", ""), "has died.")
                 del enemies[enemy]

         elif index == 1:
             player.choose_magic()
             magic_choice = int(input("     Choose magic:"))-1

             spell = player.magic[magic_choice]

             magic_dmg = spell.generate_damage()
             print("Magic dmg:", magic_dmg)

             if magic_choice == -1:
                 continue
             # So if we want to go back to actions or we don't want to select magic, we can press 0 to go back.

             current_mp = player.get_mp()

             if spell.cost > current_mp:
                 print(Bcolors.FAIL + "\nNot enough MP.\n" + Bcolors.ENDC)
                 continue

             player.reduced_mp(spell.cost)

             if spell.type == "white":
                 player.heal(magic_dmg)
                 print("Player heal:", player.heal(magic_dmg))
                 print(Bcolors.OKBLUE + spell.name, "heals for", str(magic_dmg), "HP.", Bcolors.ENDC)

             elif spell.type == "black":
                 enemy = player.choose_target(enemies)
                 enemies[enemy].take_damage(magic_dmg)

                 print(Bcolors.OKBLUE + spell.name, "deals", str(magic_dmg), "points of damage to",
                       enemies[enemy].name.replace(" ", ""), Bcolors.ENDC)

                 if enemies[enemy].get_hp == 0:
                     print(enemies[enemy].name.replace(" ", ""), "has died.")
                     del enemies[enemy]

         elif index == 2:
             player.choose_items()
             items_choice = int(input("     Choose item:"))-1

             if items_choice == -1:
                 continue
         # So if we want to go back to actions or we don't want to select items, we can press 0 to go back.


         # If player wanna choose item, let's just start off first i.e potion

             item = player.items[items_choice]["item"]

             if player.items[items_choice]["quantity"] == 0:
                 print(Bcolors.FAIL, "\n None left...", Bcolors.ENDC)
                 continue

             player.items[items_choice]["quantity"] -= 1

             if player.items[items_choice]["quantity"] == -1:
                 print(Bcolors.FAIL, "\n Not enough items.", Bcolors.ENDC)
                 continue

             if item.type == "potion":
                 player.heal(item.prop)
                 print(Bcolors.OKGREEN, "\n", item.name, "heals for", str(item.prop), "HP.",  Bcolors.ENDC)
             elif item.type == "elixir":

                 if item.name == "MegaElixir":
                     for i in players:
                         i.hp = i.maxhp
                         i.mp = i.maxmp
                 else:
                     player.hp = player.maxhp
                     player.mp = player.maxmp
                 print(Bcolors.OKGREEN, "\n", item.name, "fully restores HP/MP.", Bcolors.ENDC)
             elif item.type == "attack":
                 enemy = player.choose_target(enemies)
                 enemies[enemy].take_damage(item.prop)

                 print(Bcolors.FAIL, "\n", item.name, "deals for", str(item.prop), "points of damage to",
                       enemies[enemy].name.replace(" ", ""), Bcolors.ENDC)

                 if enemies[enemy].get_hp == 0:
                     print(enemies[enemy].name.replace(" ", ""), "has died.")
                     del enemies[enemy]

     # Check if battle is over
     defeated_enemy = 0
     defeated_player = 0
     for enemy in enemies:
         if enemy.get_hp() == 0:
             defeated_enemy += 1

     for player in players:
         if player.get_hp() == 0:
             defeated_player += 1

         # Check if player won
         if defeated_enemy == len(enemies):
             print(Bcolors.OKGREEN, "You win!", Bcolors.ENDC)

         # Check if enemy won
         if defeated_player == len(players):
             print(Bcolors.FAIL, "Your enemies have defeated you.", Bcolors.ENDC)

     # Enemy attack phase
     for enemy in enemies:
         enemy_choice = random.randrange(0, 2)

         if enemy_choice == 0:
             # Enemy is going to be attack
             target = random.randrange(0, 3)
             enemy_dmg = enemy.generate_damage()
             players[target].take_damage(enemy_dmg)
             print("\n" + enemy.name.replace(" ", ""), "attacked", players[target].name.replace(" ", ""), "for",
                   enemy_dmg, "points of damage.")

         elif enemy_choice == 1:
             spell, magic_dmg = enemy.choose_enemy_spell()

             enemy.reduced_mp(spell.cost)

             if spell.type == "white":
                 enemy.heal(magic_dmg)
                 print("Enemy heal:", enemy.heal(magic_dmg))
                 print(Bcolors.OKBLUE + spell.name, "heals " + enemy.name.replace(" ", "") + "for",
                       str(magic_dmg), "HP.", Bcolors.ENDC)

             elif spell.type == "black":
                 target = random.randrange(0, 3)
                 players[target].take_damage(magic_dmg)

                 print(Bcolors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name, "deals",
                       str(magic_dmg), "points of damage to",
                       players[target].name.replace(" ", ""), Bcolors.ENDC)

                 if players[target].get_hp == 0:
                     print(players[target].name.replace(" ", ""), "has died.")
                     del players[player]

                 # print("Enemy choose", spell, "damage is", magic_dmg)







