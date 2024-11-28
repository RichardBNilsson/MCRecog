import speech_recognition

import mc_socket
from mc_socket import MCSocket
import speech_recognition as sr
import argparse


"""
https://github.com/ketan-ryan/MCRecog/wiki
"""
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--Microphone", help="Manually select microphone", action='store_true')
arguments = parser.parse_args()

r = sr.Recognizer()
r.energy_threshold = 300

mic_idx = None
if arguments.Microphone:
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone with name {name} found for `Microphone(device_index={index})`")

    mic_idx = int(input("Please input the device index of your primary microphone: "))

mic = sr.Microphone(mic_idx)
mc = MCSocket(7777)
print("Ready to begin speech recognition!")


def get_response(response):
    res = response
    response = str(resp).replace(" ", "").lower()
    print(response)

    ret = []
    if "clay" in response:
        ret.append("Explode and die")
    if "dirt" in response:
        ret.append("Explode and die")
    if "grass" in response:
        ret.append("Explode and die")
    if "gravel" in response:
        ret.append("Explode and die")
    if "sand" in response:
        ret.append("Explode and die")
    if "soul" in response:
        ret.append("Explode and die")
    if "andesite" in response:
        ret.append("Explode and die")
    if "basalt" in response:
        ret.append("Explode and die")
    if "bedrock" in response:
        ret.append("Explode and die")
    if "blackstone" in response:
        ret.append("Explode and die")
    if "calcite" in response:
        ret.append("Explode and die")
    if "deepslate" in response:
        ret.append("Explode and die")
    if "diorite" in response:
        ret.append("Explode and die")
    if "dripstone" in response:
        ret.append("Explode and die")
    if "end" in response:
        ret.append("Explode and die")
    if "glowstone" in response:
        ret.append("Explode and die")
    if "granite" in response:
        ret.append("Explode and die")
    if "magma" in response:
        ret.append("Explode and die")
    if "netherrack" in response:
        ret.append("Explode and die")
    if "obsidian" in response:
        ret.append("Explode and die")
    if "sandstone" in response:
        ret.append("Explode and die")
    if "stone" in response:
        ret.append("Explode and die")
    if "terracotta" in response:
        ret.append("Explode and die")
    if "tuff" in response:
        ret.append("Explode and die")
    if "amethyst" in response:
        ret.append("Explode and die")
    if "ancient debris" in response:
        ret.append("Explode and die")
    if "budding amethyst" in response:
        ret.append("Explode and die")
    if "coal" in response:
        ret.append("Explode and die")
    if "copper" in response:
        ret.append("Explode and die")
    if "diamond" in response:
        ret.append("Explode and die")
    if "gold" in response:
        ret.append("Explode and die")
    if "emerald" in response:
        ret.append("Explode and die")
    if "gilded" in response:
        ret.append("Explode and die")
    if "gold" in response:
        ret.append("Explode and die")
    if "iron" in response:
        ret.append("Explode and die")
    if "lapis lazuli" in response:
        ret.append("Explode and die")
    if "nether quartz" in response:
        ret.append("Explode and die")
    if "redstone" in response:
        ret.append("Explode and die")
    if "ice" in response:
        ret.append("Explode and die")
    if "lava" in response:
        ret.append("Explode and die")
    if "snow" in response:
        ret.append("Explode and die")
    if "water" in response:
        ret.append("Explode and die")
    if "crow" in response:
        ret.append("Explode and die")
    if "wood" in response:
        ret.append("Explode and die")
    if "logs" in response:
        ret.append("Explode and die")
    if "chest" in response:
        ret.append("Explode and die")
    if "crafting table" in response:
        ret.append("Explode and die")
    if "furnace" in response:
        ret.append("Explode and die")
    if "ladder" in response:
        ret.append("Explode and die")
    

    print(response, ret)

    ret.append(res)
    return ret


while 1:
    try:
        with mic as src:
            r.adjust_for_ambient_noise(src)
            audio = r.listen(src)
            resp = r.recognize_google(audio)
            cmd = get_response(resp)

            mc.stream(cmd)

    except speech_recognition.UnknownValueError:
        pass
