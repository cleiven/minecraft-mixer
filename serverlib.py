import requests as r
import json
import os
import sys
import random


class Server:
    @staticmethod
    def create_standard_files(directory: str, version: str):
        if not (os.path.isdir(directory)):            
            os.mkdir(directory)
        # by using this script you agree to the eula
        with open(f"{directory}/eula.txt","w") as f:
            f.write("eula=true")
        with open(f"{directory}/server.properties","w") as f:
            # if anyone wants to backdoor my server, just acquire server.properties and enable rcon
            # currently uses a magic number only relevant to me, should be changed (make port a parameter)
            f.write(r.get("https://server.properties").text.replace("server-port=25565","server-port=54392"))
        with open(f"{directory}/run.sh","w") as f:
            f.write(f"java -Xmx5000M -jar {version}.jar -nogui")


class Vanilla:
    @staticmethod
    def get_version_manifest(version: str = "latest") -> str:
        #TODO: make it download the latest release instead of latest snapshot
        versions = json.loads(r.get("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json").text)["versions"]        
        choice = ""    
        print("point 1")    
        if (version == "latest"):
            print("point 2")
            choice = versions[0]["url"]
        elif (version == "random"):
            choice = random.choice(versions)["url"]
        else:
            for item in versions:
                if item["id"] == version:
                    choice = item["url"]
        # can get rid of get_version_package manifest with this but worry about it later
        #if choice.split(".")[-1] == "json":
            #choice = json.loads(r.get(choice).text)["downloads"]["server"]["url"]
        print(f"point 3: {choice}")
        return choice
        raise Exception(f"Fatal error: version {version} not found!")

        
    
    @staticmethod
    def get_version_package_manifest(version: str = "latest"):
        return json.loads(r.get(Vanilla.get_version_manifest(version)).text)["downloads"]["server"]
    
    @staticmethod
    def download_server(directory: str, version: str = "latest"):
        manifest = Vanilla.get_version_package_manifest(version)
        print(f"point 4: {manifest}")
        with r.get(manifest["url"], stream=True) as stream:
            with open(f"{directory}/{version}.jar","wb") as f:        
                i = 0
                for chunk in stream.iter_content(chunk_size=8192):
                    # TODO: make the progress bar not suck
                    print(f"Downloading Server: {(int)(100*(i*8192)/manifest['size'])}%")                
                    f.write(chunk)
                    i += 1   
    @staticmethod
    def create_server(directory: str, version: str = "latest"):
        Server.create_standard_files(directory,version)
        Vanilla.download_server(directory,version)


