import sys
import time
# version 2
from random import choice

class Person:
    def __init__(self):
        self.gender = None
        self.age = None
        self.name = None
        self.profession = None
        self.interests = []
        self.hobbies = []
        self.skills = {}
        self.personal_traits = []

        # Program Environment and Programming Language Proficiency
        self.program_environment = {}
        self.language_proficiency = {}

        # Cyber Security Abilities
        self.defensive_cyber_sec = False
        self.offensive_cyber_sec = False

    def set_gender(self, gender):
        if gender.lower() in ["male", "female", "other"]:
            self.gender = gender
        else:
            print("Invalid gender input. Please enter 'male', 'female', or 'other'.")

    def set_age(self, age):
        if isinstance(age, int) and 0 < age <= 100:
            self.age = age
        else:
            print("Invalid age range. Please enter an integer between 1 and 100.")

    def set_name(self, name):
        self.name = name

    def add_interest(self, interest):
        if isinstance(interest, str) and len(interest) > 0:
            self.interests.append(interest)
        else:
            print("Invalid interest input. Please enter a non-empty string.")

    def remove_interest(self, interest):
        if interest in self.interests:
            self.interests.remove(interest)
        else:
            print("Interest not found in list of interests.")

    def add_hobby(self, hobby):
        if isinstance(hobby, str) and len(hobby) > 0:
            self.hobbies.append(hobby)
        else:
            print("Invalid hobby input. Please enter a non-empty string.")

    def remove_hobby(self, hobby):
        if hobby in self.hobbies:
            self.hobbies.remove(hobby)
        else:
            print("Hobby not found in list of hobbies.")

    def set_profession(self, profession):
        self.profession = profession

    def add_skill(self, skill_name, proficiency_level):
        if isinstance(skill_name, str) and isinstance(proficiency_level, int) and 1 <= proficiency_level <= 10:
            self.skills[skill_name] = proficiency_level
        else:
            print("Invalid input for skill name or proficiency level.")

    def remove_skill(self, skill_name):
        if skill_name in self.skills:
            del self.skills[skill_name]
        else:
            print("Skill not found in list of skills.")

    def add_trait(self, trait):
        if isinstance(trait, str) and len(trait) > 0:
            self.personal_traits.append(trait)
        else:
            print("Invalid trait input. Please enter a non-empty string.")

    def remove_trait(self, trait):
        if trait in self.personal_traits:
            self.personal_traits.remove(trait)
        else:
            print("Trait not found in list of traits.")

    def set_program_environment(self, environment, proficiency_level):
        if isinstance(environment, str) and isinstance(proficiency_level, int) and 1 <= proficiency_level <= 10:
            self.program_environment[environment] = proficiency_level
        else:
            print("Invalid input for program environment or proficiency level.")

    def set_language_proficiency(self, language, proficiency_level):
        if isinstance(language, str) and isinstance(proficiency_level, int) and 1 <= proficiency_level <= 10:
            self.language_proficiency[language] = proficiency_level
        else:
            print("Invalid input for programming language or proficiency level.")

    def set_defensive_cyber_sec(self):
        self.defensive_cyber_sec = True

    def set_offensive_cyber_sec(self):
        self.offensive_cyber_sec = True

    def __str__(self):
        txt_color = '\033[92m'
        end_color = '\033[0m'

        info_str = f"\n{txt_color}Name: {end_color}{self.name}\n"
        info_str += f"{txt_color}Gender: {end_color}{self.gender}\n"
        info_str += f"{txt_color}Age: {end_color}{self.age}\n"
        info_str += f"{txt_color}Profession: {end_color}{self.profession}\n"

        interests_txt = '\033[94m'
        hobbies_txt = '\033[95m'

        for interest in self.interests:
            info_str += f"{interests_txt}Interests: {end_color}{interest}, "

        for hobby in self.hobbies:
            info_str += f"{hobbies_txt}Hobbies: {end_color}{hobby}, "

        skills_txt = '\033[93m'
        personal_traits_txt = '\033[96m'

        for skill, level in self.skills.items():
            info_str += f"\n{skills_txt}Skills: {skill} ({level}/10), "

        for trait in self.personal_traits:
            info_str += f"{personal_traits_txt}Personal Traits: {end_color}{trait}, "

        program_environment_txt = '\033[91m'
        language_proficiency_txt = '\033[92m'

        for env, level in self.program_environment.items():
            info_str += f"\n{program_environment_txt}Program Environment: {env} ({level}/10), "

        for lang, proficiency_level in self.language_proficiency.items():
            info_str += f"{language_proficiency_txt}Programming Languages: {lang} ({proficiency_level}/10), "

        if self.defensive_cyber_sec:
            info_str += f"\n{txt_color}Defensive Cyber Security Experience: Yes{end_color}"
        else:
            info_str += f"\n{txt_color}Defensive Cyber Security Experience: No{end_color}"

        if self.offensive_cyber_sec:
            info_str += f"\n{txt_color}Offensive Cyber Security Experience: Yes{end_color}"
        else:
            info_str += f"\n{txt_color}Offensive Cyber Security Experience: No{end_color}"

        return info_str

# Create a person
person = Person()

# Set general information
person.set_name("Victor Åhgren")
person.set_age(34)
person.set_gender("male")

# Add interests and hobbies
interests = ["programming", "problem-solving", "technology", "drumming", "making music", "socializing"]
hobbies = ["drumming", "music production"]

for interest in interests:
    person.add_interest(interest)

for hobby in hobbies:
    person.add_hobby(hobby)

# Set profession
person.set_profession("Cyber Security Consultant/Specialist")

# Add education and skills
educations = [
    {"degree": "Computer Engineering", "duration": 3.5},
    {"degree": "Cyber Security Specialist", "duration": None}
]

for edu in educations:
    print(f"{edu['degree']} ({edu['duration']} years)")

programming_languages = ["Java", "Go", "C", "C++", "Python", "Rust", "JavaScript", "HTML", "CSS", "PHP", "SQL"]

print("Programming Languages:")
for lang in programming_languages:
    person.add_skill(lang, 7)  # proficiency level set to 7 (out of 10)

# Add defensive cyber security experience
defensive_experience = ["Rapid7 InsightVM", "IDR", "Splunk Enterprise", "CrowdStrike Falcon", "IBM QRadar", "Nessus Expert", "Burp Suite", "ELK Stacks"]
for exp in defensive_experience:
    print(exp)

# Add personal traits
personal_traits = ["Analytical", "Creative", "Collaborative"]

for trait in personal_traits:
    person.add_trait(trait)

# Function to create typing effect
def typing_effect(text, speed=0.033):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # For newline after the message

# Example usage in your script with the person object:
typing_effect(str(person))


