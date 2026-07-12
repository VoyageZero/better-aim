from rep import Rep
from typing import List

class Scenario:
    def __init__(self, name: str, reps: List[Rep]):
        self.name = name
        self.reps = reps