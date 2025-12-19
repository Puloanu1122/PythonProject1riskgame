import tkinter as tk
from tkinter import messagebox

# --- Game Data ---
scenarios = [
    {
        "scenario": "Hotel Lobby: A suspicious package is near the reception desk.",
        "risks": ["Bomb threat", "Theft", "Unauthorized access", "Fire hazard"],
        "correct": ["Bomb threat", "Unauthorized access"]
    },
    {
        "scenario": "Corporate Office: A delivery truck is parked outside the main entrance for a long time.",
        "risks": ["Bomb threat", "Unauthorized access", "Chemical spill", "Theft"],
        "correct": ["Bomb threat", "Unauthorized access", "Theft"]
    },
    {
        "scenario": "Shopping Mall: Crowd is gathering near an exit during an event.",
        "risks": ["Stampede risk", "Theft", "Fire hazard", "Suspicious activity"],
        "correct": ["Stampede risk", "Suspicious activity", "Theft"]
    }
]

score = 0
current = 0


# --- Functions ---
def submit_answers():
    global score, current
    selected = [var.get() for var in risk_vars if var.get() != ""]
    correct_risks = scenarios[current]["correct"]

    feedback = ""
    for s in selected:
        if s in correct_risks:
            score += 10
            feedback += f"Correct: {s}\n"
        else:
            score -= 5
            feedback += f"Incorrect: {s}\n"

    feedback_label.config(text=feedback + f"\nCurrent Score: {score}")
    current += 1

    if current >= len(scenarios):
        messagebox.showinfo("Game Over", f"Final Score: {score}")
        root.destroy()
    else:
        load_scenario()


def load_scenario():
    scenario_data = scenarios[current]
    scenario_label.config(text=f"Scenario {current + 1}: {scenario_data['scenario']}")
    for i, risk in enumerate(scenario_data["risks"]):
        checkbuttons[i].config(text=risk)
        risk_vars[i].set("")


# --- GUI Setup ---
root = tk.Tk()
root.title("Risk Analysis Game")

# Scenario text
scenario_label = tk.Label(root, text="", wraplength=500, justify="left", font=("Arial", 12))
scenario_label.pack(pady=20)

# Checkbuttons for risks
risk_vars = [tk.StringVar() for _ in range(4)]
checkbuttons = []
for i in range(4):
    cb = tk.Checkbutton(root, text="", variable=risk_vars[i], onvalue=scenarios[0]['risks'][i], offvalue="")
    cb.pack(anchor="w")
    checkbuttons.append(cb)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_answers)
submit_btn.pack(pady=15)

# Feedback label
feedback_label = tk.Label(root, text="", wraplength=500, justify="left", font=("Arial", 10))
feedback_label.pack(pady=10)

# Load first scenario
load_scenario()

root.mainloop()
