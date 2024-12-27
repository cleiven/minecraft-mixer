#!/usr/bin/env python3
from serverlib import *

# A gimmicky tool that creates a random Minecraft server with as many degrees of freedom as possible
# TODO: 
# - settings class
# - port
# - world map (get some custom maps?)
# - datapack (put a bunch of random commands in it lmfao, also world settings)


class Settings:
    server_path = "server_mixer"
    random_port = True
    random_version = True
    random_world = True
    random_datapack = True
    
def main():
     Vanilla.create_server(Settings.server_path,"random")
     with open(f"server_path/server.properties","r+") as f:
        server_properties = f.read()
        # make changes etc
        f.write(server_properties)
if __name__ == "__main__":
    main()
