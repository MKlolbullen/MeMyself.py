#!/usr/bin/env python3
"""
Fun self‑representation of Victor Åhgren in Python.
Run this file to print a colourful résumé to the terminal.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from statistics import fmean
from typing import List

from colorama import Fore, Style, init

# Auto‑reset ANSI styles so we don’t have to spell out Style.RESET_ALL everywhere
init(autoreset=True)

BULLET = "•"

# ---------------------------------------------------------------------------
#  Data structures
# ---------------------------------------------------------------------------


@dataclass
class About:
    """General stuff that makes Victor tick."""

    hobbies: List[str] = field(
        default_factory=lambda: [
            "Cybersecurity",
            "Programming",
            "Drumming",
            "Making music",
            "Spending time with close friends and family",
        ]
    )
    interests: List[str] = field(
        default_factory=lambda: [
            "A general love for learning new things, meeting interesting people and just growing as a person",
        ]
    )
    traits: List[str] = field(
        default_factory=lambda: [
            "Detail‑oriented",
            "Analytical with a very high work ethic",
            "Teamwork makes the dream work! I truly believe in a diverse range of opinions and personalities in a team.",
        ]
    )


@dataclass
class Program:
    name: str
    category: str  # "Offensive", "Defensive", or "Offensive/Defensive"
    source: str    # "Open‑source", "Proprietary", etc.
    description: str


@dataclass
class Skill:
    name: str
    theory: float
    usage: float
    usage_time: float

    def knowledge(self) -> tuple[str, float]:
        """Return a verbal level + rounded mean score (0‑5)."""
        score = fmean((self.theory, self.usage, self.usage_time))
        if score >= 4.5:
            level = "Highly experienced and competent"
        elif score >= 3:
            level = "Very experienced and competent"
        elif score >= 2:
            level = "Experienced; as competent as time allowed"
        elif score >= 1:
            level = "Familiar; would be fully operational very quickly"
        else:
            level = "Have tried but not very experienced"
        return level, round(score, 2)


@dataclass
class Person:
    firstname: str
    lastname: str
    age: int
    jobtitles: List[str]
    website: str
    notionsite: str
    musicsite: str
    interests: List[str] = field(default_factory=list)
    hobbies: List[str] = field(default_factory=list)
    skills: List[Skill] = field(default_factory=list)
    traits: List[str] = field(default_factory=list)
    programs: List[Program] = field(default_factory=list)
    programming_languages: List[str] = field(default_factory=list)

    # ---------------------------------------------------------------------
    #  Convenience adders
    # ---------------------------------------------------------------------

    def add_skill(self, *args, **kwargs):
        self.skills.append(Skill(*args, **kwargs))

    def add_program(self, *args, **kwargs):
        self.programs.append(Program(*args, **kwargs))

    def add_interest(self, interest: str):
        self.interests.append(interest)

    def add_hobby(self, hobby: str):
        self.hobbies.append(hobby)

    def add_trait(self, trait: str):
        self.traits.append(trait)

    def add_programming_language(self, lang: str):
        self.programming_languages.append(lang)

    # ---------------------------------------------------------------------
    #  Derived data
    # ---------------------------------------------------------------------

    def experience(self) -> dict[str, str]:
        return {
            "Penetration testing": "Bug bounty hunting and OSCP‑style engagements",
            "OSINT": "Gathering and analysing information from open sources",
            "SOC / Analyst": "Hands‑on with most major SIEM/XDR systems",
            "Problem‑solving": "Breaking down and solving complex problems",
            "Data analysis": "Analysing large datasets and drawing insightful conclusions",
        }

    # ---------------------------------------------------------------------
    #  Pretty‑printing (main attraction)
    # ---------------------------------------------------------------------

    def print_info(self):  # noqa: C901  (long but readable CLI output)
        print(f"{Fore.CYAN}{self.firstname} {self.lastname}{Style.RESET_ALL} — Age {self.age}")
        print(f"{Fore.MAGENTA}{', '.join(self.jobtitles)}{Style.RESET_ALL}\n")

        print(f"{Fore.LIGHTBLUE_EX}Website:{Style.RESET_ALL} {self.website}")
        print(f"{Fore.LIGHTBLUE_EX}Notion site:   {Style.RESET_ALL} {self.notionsite}")
        print(f"{Fore.LIGHTBLUE_EX}Music:  {Style.RESET_ALL} {self.musicsite}\n")

        # Skills
        print(f"{Fore.GREEN}Skills{Style.RESET_ALL}")
        for skill in self.skills:
            level, score = skill.knowledge()
            print(f"  {BULLET} {Fore.YELLOW}{skill.name:<24}{Style.RESET_ALL} {level} (⌀ {score})")
        print()

        # Programs organised by category
        print(f"{Fore.GREEN}Programs{Style.RESET_ALL}")
        cats = defaultdict(list)
        for prg in self.programs:
            cats[prg.category].append(prg)
        for cat, prgs in cats.items():
            colour = (
                Fore.RED if cat == "Offensive" else Fore.GREEN if cat == "Defensive" else Fore.YELLOW
            )
            print(f" {colour}{cat}{Style.RESET_ALL}")
            for prg in prgs:
                print(f"   {BULLET} {prg.name:<20} — {prg.description}")
        print()

        # Programming languages
        print(f"{Fore.GREEN}Programming Languages{Style.RESET_ALL}")
        for lang in self.programming_languages:
            print(f"  {BULLET} {lang}")
        print()

        # Experience bullets
        print(f"{Fore.GREEN}Experience{Style.RESET_ALL}")
        for k, v in self.experience().items():
            print(f"  {BULLET} {k}: {v}")
        print()

        # Personality
        about = About()
        merged_traits = list(dict.fromkeys(self.traits + about.traits))
        merged_hobbies = list(dict.fromkeys(self.hobbies + about.hobbies))

        print(f"{Fore.GREEN}Personality Traits{Style.RESET_ALL}")
        for t in merged_traits:
            print(f"  {BULLET} {t}")
        print(f"\n{Fore.GREEN}Hobbies{Style.RESET_ALL}")
        for h in merged_hobbies:
            print(f"  {BULLET} {h}")


# ---------------------------------------------------------------------------
#  Helper to build Victor & run script directly
# ---------------------------------------------------------------------------


def build_victor() -> Person:
    """Return a fully‑loaded Person instance representing Victor."""

    return Person(
        firstname="Victor",
        lastname="Åhgren",
        age=35,
        jobtitles=[
            "Cyber‑Security Consultant",
            "Analyst",
            "Engineer",
            "Penetration Tester",
            "Bug Bounty Hunter",
        ],
        website="https://victorahgren.com/ (#under recontructrion)",
        notionsite="https://victorahgren.notion.site/VICTOR-HGREN-CYBER-SECURITY-SPECIALIST-f9e8a93d1a634af09c7d1ce083ade798",
        musicsite="https://www.youtube.com/@victorahgren560",
        hobbies=[
            "Cybersecurity",
            "Programming",
            "Drumming",
            "Making music",
            "Spending time with close friends and family",
        ],
        skills=[
            # Core
            Skill("Defensive security", 4.28, 3.4, 3.5),
            Skill("Offensive security", 4.6, 4.78, 4.36),
            Skill("Programming", 4.5, 4.8, 5),
            Skill("Cybersecurity", 4.7, 4.9, 5),
            # specialist skills
            Skill("Web application security", 4.7, 4.9, 5),
            Skill("Cloud security", 4.2, 4.0, 3.5),
            Skill("Reverse engineering", 3.6, 3.2, 2.8),
            Skill("Exploit development", 3.9, 3.8, 3.2),
            Skill("Automation & scripting", 4.8, 4.0, 4.2),
        ],
        traits=[
            "Detail‑oriented",
            "Charmingly semi-autistic",
            "Analytical with a very high work ethic",
            "High work ethic",
            "Love a good laugh",
            "Responsible, which includes my own mistakes"
        ],
        programs=[
            # Defensive / Hybrid
            Program("Nessus", "Defensive", "Proprietary", "Vulnerability scanner by Tenable"),
            Program("Rapid7 InsightVM", "Defensive", "Proprietary", "Vulnerability management"),
            Program("Qualys", "Defensive", "Proprietary", "Cloud VM platform"),
            Program("IBM QRadar", "Defensive", "Proprietary", "SIEM"),
            Program("CrowdStrike Falcon", "Defensive", "Proprietary", "Endpoint security"),
            Program("Splunk", "Defensive", "Proprietary", "Log analytics / SIEM"),
            Program("Dnsx", "Defensive", "Open‑source", "DNS toolkit in Go"),
            Program("Trellix package", "Defensive", "Proprietary", "E‑XDR suite"),

            # Offensive / Dual‑use classics
            Program("Metasploit", "Offensive", "Open‑source/Proprietary", "Exploit framework"),
            Program("Impacket", "Offensive", "Open‑source", "Python classes for crafting network attacks"),
            Program("Nmap", "Offensive/Defensive", "Open‑source", "Network mapper & scanner"),
            Program("masscan", "Offensive/Defensive", "Open‑source", "Internet‑scale TCP port scanner"),
            Program("Naabu", "Offensive/Defensive", "Open‑source", "Fast port scanner in Go"),
            Program("sqlmap", "Offensive", "Open‑source", "Automated SQL injection tool"),
            Program("Hydra", "Offensive", "Open‑source", "Parallel login brute‑forcer"),
            Program("Gobuster", "Offensive", "Open‑source", "Content & directory brute‑forcer"),
            Program("feroxbuster", "Offensive", "Open‑source", "Recursive content discovery in Rust"),
            Program("ffuf", "Offensive", "Open‑source", "Fast web fuzzer"),
            Program("Amass", "Offensive/Defensive", "Open‑source", "In‑depth DNS enumeration"),
            Program("Subfinder", "Offensive/Defensive", "Open‑source", "Passive subdomain discovery"),
            Program("nuclei", "Offensive/Defensive", "Open‑source", "Template‑based vulnerability scanner"),
            Program("ZAP", "Offensive", "Open‑source", "OWASP Zed Attack Proxy"),
            Program("wpscan", "Offensive", "Open‑source", "WordPress security scanner"),
            Program("nikto", "Offensive", "Open‑source", "Web server scanner"),
            Program("Responder", "Offensive", "Open‑source", "LLMNR/NBT‑NS/MDNS poisoner"),
            Program("Bettercap", "Offensive", "Open‑source", "Network attack & monitoring toolkit"),
            Program("BloodHound", "Offensive", "Open‑source", "AD privilege escalation path mapper"),
            Program("mimikatz", "Offenshttps://www.youtube.com/@victorahgren560ive", "Open‑source", "Credential dumper for Windows"),
            Program("enum4linux‑ng", "Offensive", "Open‑source", "Samba/Windows enum tool"),
            Program("linpeas", "Offensive", "Open‑source", "Linux privilege escalation checks"),
            Program("winpeas", "Offensive", "Open‑source", "Windows privilege escalation checks"),
            Program("pspy", "Offensive/Defensive", "Open‑source", "Process snooper without root"),
            Program("gitleaks", "Offensive/Defensive", "Open‑source", "Audit Git repos for secrets"),
            Program("trufflehog", "Offensive/Defensive", "Open‑source", "Search for secrets across code"),
            Program("BBot", "Offensive", "Open‑source", "Automated OSINT/recon toolkit"),
            Program("Burp Suite", "Offensive", "Proprietary", "Web application security testing GUI"),
        ],
        programming_languages=[
            "Python",
            "Go",
            "Rust",
            "Shell scripting",
            "C",
            "C++",
            "Java",
            "JavaScript",
        ],
    )


# ---------------------------------------------------------------------------
#  Main entry‑point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    build_victor().print_info()
                                                                                                                           

