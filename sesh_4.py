# Created by Kaelen Cook
# Jan 2024

class Animal:
    def __init__(self, armLength, legLength, eyes, tail, furry):
        self.armLength = armLength      # arm length in meters
        self.legLength = legLength      # leg length in meters
        self.eyes = eyes        # eyes in how many they have
        self.tail = tail        # tail in do they have one
        self.furry = furry      # furry in are they or are they not
    
    def describe(self):
        print(f"""This animal's arms are {self.armLength} meters in length, their legs are {self.legLength} meters;
              they have {self.eyes} eyes.""")
        if (self.tail):
            print("They have a tail.")
        else:
            print("They are tailless (so sad).")
        if (self.furry):
            print("They are a furry lil individual.")
        else:
            print("They are as bare nakey as they come. Skin only.")


greg = Animal(2, 0.2, 2.5, True, False)