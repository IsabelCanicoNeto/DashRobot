from robot import *
from constants import *
from dashbehaviour import *
import asyncio
import struct
from bleak import BleakScanner
from bleak import BleakClient



def DashSoundTest (dash, sound = "ALL"  ):

    # play the sound , recorded in the robot as requested in sound or all of them

    sounds = {
        "elephant",
        "tiresqueal",
        "hi",
        "bragging",
        "ohno",
        "ayayay",
        "confused2",
        "confused3",
        "confused5",
        "confused8",
        "brrp",
        "charge",
        "huh",
        "okay",
        "yawn",
        "tada",
        "wee",
        "bye",
        "horse",
        "cat",
        "dog",
        "dino",
        "lion",
        "goat",
        "croc",
        "siren",
        "horn",
        "engine",
        "tires",
        "helicopter",
        "jet",
        "boat",
        "train",
        "beep",
        "laser",
        "gobble",
        "buzz",
        "squeek",
        "my1",
        "my2",
        "my3",
        "my4",
        "my5",
        "my6",
        "my7",
        "my8",
        "my9",
        "my10",
    }

    if sound == "ALL":

        for k in sounds:
            print (k)
            dash.say(k)
            time.sleep(0.5)
    else:
        print(sound)
        dash.say(sound)
        time.sleep(0.5)

def SimpleBehavior (dash):

    dash.name()

    print("reset")
    dash.reset(4)
    time.sleep(2)

    dash.eye(0b1010101010101)

    dash.say("hi")
    dash.say("ayayay")
    dash.say("huh")
    dash.say("okay")
    dash.neck_color("yellow")
    time.sleep(2)

    dash.move(100)
    time.sleep(2)
    dash.turn(45)

    time.sleep(2)
    dash.ear_color("red")
    time.sleep(2)
    dash.head_yaw(10)
    time.sleep(2)

    #dash.eye(255)
    dash.eye(100)
    #dash.eye(8191)

def TETest (dash, slowPace = False):

    print("turn 1 -> 2 ")
    actualSpeaker = 1
    nextSpeaker = 2
    nextSpeakerName = "my3"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("turn 2 -> 3 ")
    actualSpeaker = 2
    nextSpeaker = 3
    nextSpeakerName = "my4"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("turn 3 -> 2 ")
    actualSpeaker = 3
    nextSpeaker = 2
    nextSpeakerName = "my3"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("turn 2 -> 1 ")
    actualSpeaker = 2
    nextSpeaker = 1
    nextSpeakerName = "my1"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)


    print("turn 1 -> 3 ")
    actualSpeaker = 1
    nextSpeaker = 3
    nextSpeakerName = "my4"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("turn 3 -> 1 ")
    actualSpeaker = 3
    nextSpeaker = 1
    nextSpeakerName = "my1"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)


def HearingTest (dash, explicit, slowPace=False):

    print("hear 2 -> suggested 1 ")
    actualSpeaker = 2
    suggestedSpeaker = 1
    hearing(dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 3 -> suggested 1 ")
    actualSpeaker = 3
    suggestedSpeaker = 1
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 1 -> suggested 1 ")
    actualSpeaker = 1
    suggestedSpeaker = 1
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

    print("TE 1 -> 2 ")
    nextSpeaker = 2
    nextSpeakerName = "my3"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("hear 2 -> suggested 2 ")
    actualSpeaker = 2
    suggestedSpeaker = 2
    hearing(dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 3 -> suggested 2 ")
    actualSpeaker = 3
    suggestedSpeaker = 2
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 1 -> suggested 2 ")
    actualSpeaker = 1
    suggestedSpeaker = 2
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

    print("TE 2 -> 3 ")
    nextSpeaker = 3
    nextSpeakerName = "my4"
    turnexchange(dash, actualSpeaker, nextSpeaker, "my2", nextSpeakerName, slowPace)

    print("hear 1 -> suggested 3 ")
    actualSpeaker = 1
    suggestedSpeaker = 3
    hearing(dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 2 -> suggested 3 ")
    actualSpeaker = 2
    suggestedSpeaker = 3
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

    print("hear 3 -> suggested 3 ")
    actualSpeaker = 3
    suggestedSpeaker = 3
    hearing (dash, suggestedSpeaker, actualSpeaker, explicit)

def main():
    print ("começa")

    dash = robot()
    print(dash.address)
    print(dash.device)

    if dash.is_connected:
        dash.name()

        DashSoundTest(dash,  "huh")
        DashSoundTest(dash,  "my5")
        DashSoundTest(dash, "yawn")
        DashSoundTest(dash, "confused8")
        DashSoundTest(dash, "okay")

        DashSoundTest (dash, sound = "ALL"  )
        #   firstspeaker(dash,1,"my1")

        explicit = True
        # TETest(dash, explicit)

        # HearingTest(dash, explicit)


        print ("close")
        dash.closeDash()



if __name__ == '__main__':
    main()