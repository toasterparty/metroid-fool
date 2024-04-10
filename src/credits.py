text = '''
&push;&font=C29C51F1;&main-color=#89D6FF;Item Progression&pop;

&push;&font=C29C51F1;&main-color=#33ffd6;Morph Ball&pop;
Chozo Ruins - Ruined Shrine (Beetle Battle)

&push;&font=C29C51F1;&main-color=#33ffd6;Missile Launcher&pop;
Chozo Ruins - Water Pool

&push;&font=C29C51F1;&main-color=#33ffd6;Morph Ball Bomb&pop;
Chozo Ruins - Dynamo (Lower)

&push;&font=C29C51F1;&main-color=#33ffd6;Varia Suit&pop;
Chozo Ruins - Sunchamber

&push;&font=C29C51F1;&main-color=#33ffd6;Charge Beam&pop;
Phendrana Drifts - Phendrana Canyon

&push;&font=C29C51F1;&main-color=#33ffd6;Boost Ball&pop;
Phendrana Drifts - Chapel of the Elders

&push;&font=C29C51F1;&main-color=#33ffd6;WAVE BEAM!&pop;
Magmoor Caverns - Geothermal Core

&push;&font=C29C51F1;&main-color=#33ffd6;Super Missiles&pop;
Chozo Ruins - Training Chamber Access

&push;&font=C29C51F1;&main-color=#33ffd6;Spider Ball&pop;
Phendrana Drifts - Quarantine Cave

&push;&font=C29C51F1;&main-color=#33ffd6;Ice Beam&pop;
Chozo Ruins - Ruined Shrine (Spider Track)

&push;&font=C29C51F1;&main-color=#33ffd6;Power Bomb&pop;
Phazon Mines - Central Dynamo

&push;&font=C29C51F1;&main-color=#33ffd6;Plasma Beam&pop;
Magmoor Caverns - Plasma Processing

&push;&font=C29C51F1;&main-color=#33ffd6;Flamethrower&pop;
Chozo Ruins - Burn Dome

&push;&font=C29C51F1;&main-color=#33ffd6;Gravity Suit&pop;
Tallon Overworld - Gully

&push;&font=C29C51F1;&main-color=#33ffd6;X-Ray Visor&pop;
Phendrana Drifts - Ice Ruins East

&push;&font=C29C51F1;&main-color=#33ffd6;Thermal Visor&pop;
Phazon Mines - Missile Station Mines

&push;&font=C29C51F1;&main-color=#33ffd6;Space Jump Boots&pop;
Phazon Mines - Elite Quarters

&push;&font=C29C51F1;&main-color=#33ffd6;Wavebuster&pop;
Chozo Ruins - Tower of Light

&push;&font=C29C51F1;&main-color=#33ffd6;Ice Spreader&pop;
Tallon Overworld - Life Grove

&push;&font=C29C51F1;&main-color=#33ffd6;Glorgie's Keyring&pop;
Tallon Overworld - Reactor Core

&push;&font=C29C51F1;&main-color=#33ffd6;Phazon Suit&pop;
Tallon Overworld - Artifact Temple

&push;&font=C29C51F1;&main-color=#33ffd6;Chozo Artifacts&pop;
The real Artifacts were the friends we made along the way

&push;&font=C29C51F1;&main-color=#33ffd6;Energy Tanks&pop;
       Location           Intended Collection    
   Frigate Crash Site         1st Pass           
       Hive Mecha             1st Pass           
 Magmoor Workstation    2nd Pass needs boost     
       Frozen Pike           1st Pass DBJ        
    Gravity Chamber        2nd Pass Plasma       
       Main Quarry        1st Pass Crane Meme    
Metroid Quarantine A     1st Pass Hidden Wall    
    Parasite Queen    2nd Pass SJ/1st Pass UBJ   
    Monitor Station         2nd Pass SJ          
   Frigate Crash Site       3rd Pass GSJ         
     Arbor Chamber          2nd Pass SJ          
   Great Tree Hall    1st Pass From Spider Track 
     Ice Ruins West         2nd Pass SW          
     Watery Hall SW         2nd Pass SJ          

&push;&font=C29C51F1;&main-color=#33ffd6;Missile Expansions&pop;
You could have had 172, but you chose to support diversity and local business instead

&push;&font=C29C51F1;&main-color=#33ffd6;Shiny Missiles&pop;
T#3lo! Ov*!?$r)d - ???
Ma)*2or C^v3!rs - ???
Ph8!d@an(>a $r1f7s - ???

&push;&font=C29C51F1;&main-color=#89D6FF;Fanhack Credits&pop;

&push;&font=C29C51F1;&main-color=#33ffd6;Fanhack Tool Development&pop;
toasterparty
randomprime contributors

&push;&font=C29C51F1;&main-color=#33ffd6;Route&pop;
toasterparty

&push;&font=C29C51F1;&main-color=#33ffd6;Level Design&pop;
toasterparty

&push;&font=C29C51F1;&main-color=#33ffd6;Level Implementation&pop;
toasterparty

&push;&font=C29C51F1;&main-color=#33ffd6;Water Pool Morph Ball Track&pop;
UncleReggie

&push;&font=C29C51F1;&main-color=#33ffd6;Geothermal Core Morph Ball Track&pop;
UncleReggie

&push;&font=C29C51F1;&main-color=#33ffd6;Playtesters&pop;
BajaBlood
Lokir
UncleReggie

&push;&font=C29C51F1;&main-color=#89D6FF;Fun Facts&pop;

&push;&font=C29C51F1;&main-color=#33ffd6;Inspiration&pop;
Mario Maker troll level community

&push;&font=C29C51F1;&main-color=#33ffd6;Development Time&pop;
5 months

&push;&font=C29C51F1;&main-color=#33ffd6;toaster's Personal Bests&pop;
any% - 7:11 IGT
Phazon Frigate - 9 Energy Tanks
Escape Sequence - 3:00 remaining
























The Artifact Temple Statue lore text is from the Wikipedia Statue article (2024, March 17) by Wikipedia contributors. https://en.wikipedia.org/wiki/Statue
It is available under the Creative Commons Attribution-ShareAlike License 4.0
(CC BY-SA 4.0) https://creativecommons.org/licenses/by-sa/4.0/
additional terms may apply




















(this page is intentionally left blank)























Thanks for Playing!
'''

text = text.replace('\n', '\\n')

with open('credits.json', 'w') as file:
    file.write(f'"creditsString": "{text}"\n')
