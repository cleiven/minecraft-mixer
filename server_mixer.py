#!/usr/bin/env python3
from serverlib import *
import random

# A gimmicky tool that creates a random Minecraft server with as many degrees of freedom as possible
# TODO: 
# - make the settings class actually do something
# - rcon password generator
# - more advanced motd generator
# - curated seeds
# - some manually built premade maps
# - resource pack randomizer 
# - datapack randomizer (maybe someone else has made one?)
# - daemon for automatically rerolling and deploying the server on set interavals

class Settings:
    server_path = "server_mixer2"
    random_port = True
    random_version = True
    random_world = True
    random_datapack = True
class PropertiesTemplate:
    def select_curated_seed_or_dont():
        ## TODO: actually curate them
        # in principle there should only be a few seeds.
        # that way players will encounter familiar worlds 
        # under different condition throughout iterations
        curated_seeds = [
            1234, 2025, 7920, 370

        ]
        if (random.choice([True,False])):
            return random.choice(curated_seeds)
        return ''
    
    def generate_interesting_motd():
        ## TODO: these are random currently. 
        # in the future they should depend on the other properties
        # and give clues about the server
        interesting_motds = \
        [
            'the rcon password is probably really insecure',
            '*drum break plays*',
            'A Minceraft Server',
            'A Minecraft Sfderv',
            'A Minecraft Server',
            'this is normal for gnomes',
            'ba... ba ba... baaa...',
            'no swearing allowed',
            '*laughs manaically*',
            'perkele siihen et koske saatana vie',
            'ii bII7 bVImaj7 i',
            'ii V7 bVImaj7 i',
            'definitely not safe for work',
            'safe for work! :)',
            'what we have here is a failure to communicate'
        ]
        
        return random.choice(interesting_motds)
    def generate_rcon_password():
        return 'placeholder_asffdfo'

    # list of tuples giving the property name (0), lambda for assigning the value (1), and boolean indicating whether it should be modified
    # lambdas should take no arguments
    properties_list = [
        #accepts-transfers=false
        ('accepts-transfers',lambda: random.choice(['true','false']), True),
        #allow-flight=false
        ('allow-flight',lambda: random.choice(['true','false']), True),
        #allow-nether=true
        ('allow-nether',lambda: random.choice(['true','false']), True),
        #broadcast-console-to-ops=true
        ('broadcast-console-to-ops',lambda: random.choice(['true','false']), True),
        #broadcast-rcon-to-ops=true
        ('broadcast-rcon-to-ops',lambda: random.choice(['true','false']), True),
        #bug-report-link=
        #debug=false
        ('debug',lambda: random.choice(['true','false']), False),
        #difficulty=easy
        ('difficulty',lambda: random.choice(['peaceful','easy','normal','hard']), True),
        #enable-command-block=false
        ('enable-command-block',lambda: random.choice(['true','false']), True),
        #enable-jmx-monitoring=false
        #enable-query=false
        #enable-rcon=false
        ('enable-rcon',lambda: random.choice(['true','false']), True),
        #enable-status=true
        ('enable-status',lambda: random.choice(['true','false']), True),
        #enforce-secure-profile=true
        ('enforce-secure-profile',lambda: 'false', True),
        #enforce-whitelist=false
        #entity-broadcast-range-percentage=100
        #force-gamemode=false
        ('force-gamemode',lambda: random.choice(['true','false']), True),
        #function-permission-level=2
        #gamemode=survival
        ('gamemode',lambda: random.choice(['creative','survival','hardcore','adventure']), True),
        #generate-structures=true
        #generator-settings={}
        #hardcore=false
        ('hardcore',lambda: random.choice(['true','false']), True),
        #hide-online-players=false
        ('hide-online-players',lambda: random.choice(['true','false']), True),
        #initial-disabled-packs=
        #initial-enabled-packs=vanilla
        #level-name=world
        #level-seed=
        ('level-seed',lambda: PropertiesTemplate.select_curated_seed_or_dont(), True),
        #level-type=minecraft\:normal
        ('level-type',lambda: random.choice(['normal','flat','large_biomes','amplified','single_biome_surface']), True),
        #log-ips=true
        #max-chained-neighbor-updates=1000000
        #max-players=20
        ('max-players',lambda: random.randint(1,250), True),
        #max-tick-time=60000
        #max-world-size=29999984
        ('max-world-size',lambda: random.randint(1,29999984), True),
        #motd=A Minecraft Server
        ('motd',lambda: PropertiesTemplate.generate_interesting_motd(), True),
        #network-compression-threshold=256
        #online-mode=true
        ('online-mode',lambda: random.choice(['true','false']), True),
        #op-permission-level=4
        #player-idle-timeout=0
        #prevent-proxy-connections=false
        #pvp=true
        ('pvp',lambda: random.choice(['true','false']), True),
        #query.port=25565
        #rate-limit=0
        #rcon.password=
        ('rcon.password',lambda: PropertiesTemplate.generate_rcon_password(), True),
        #rcon.port=25575
        #region-file-compression=deflate
        #require-resource-pack=false
        #resource-pack=
        #resource-pack-id=
        #resource-pack-prompt=
        #resource-pack-sha1=
        #server-ip=
        #server-port=25565
        ## TODO: if it interferes with another service then too bad lmfao :skull: :skull: :skull:
        ('server-port',lambda: random.randint(25565,50000), True),
        #simulation-distance=10
        ('simulation-distance',lambda: random.randint(1,32), True),
        #spawn-animals=true
        #spawn-monsters=true
        #spawn-npcs=true
        #spawn-protection=16
        #sync-chunk-writes=true
        #text-filtering-config=
        #use-native-transport=true
        #view-distance=10
        ('view-distance',lambda: random.randint(1,32), True)
        #white-list=false
    ]

def main():
     Vanilla.create_server(Settings.server_path,"random")
     with open(f"{Settings.server_path}/server.properties","w") as f:
        for setting_tuple in PropertiesTemplate.properties_list:
            if (setting_tuple[2]):
                f.write(f"{setting_tuple[0]}={setting_tuple[1]()}\n")
if __name__ == "__main__":
    main()
