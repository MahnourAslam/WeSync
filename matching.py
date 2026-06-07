tasks = [
    {"name": "Build login API", "required_skill": "backend", "difficulty": 3, "estimated_hours": 6},
    {"name": "Design user dashboard", "required_skill": "frontend", "difficulty": 2, "estimated_hours": 4}
]

teammates = [
    {"name": "Mahnour", "skills": {"backend": 4, "frontend": 2}, "available_hours": 10},
    {"name": "Ahmed", "skills": {"backend": 3, "frontend": 3}, "available_hours": 8},
    {"name": "Fatima", "skills": {"backend": 2, "frontend": 4}, "available_hours": 12}
]

#Assigns task to teammate based on skill and available hours
#Can make weight configurable or learn from data later
# What goes in: list of task dicts, list of teammate dicts
# What comes out: dictionary of {task_name: teammate_name}
# What could go wrong: no skill match, not enough hours, no teammates at all
def assign_tasks(tasks, teammates): 
    max_hours = max(teammate["available_hours"] for teammate in teammates)
    assignments = {}
    for task in tasks:
        best_fit = (None,0)  # (teammate_name, score)
        for teammate in teammates:
            if task["required_skill"] in teammate["skills"] and teammate["available_hours"] >= task["estimated_hours"]:
                norm_skill = teammate["skills"][task["required_skill"]] / 5
                norm_hours = teammate["available_hours"] / max_hours
                score = (0.7 * norm_skill) + (0.3 * norm_hours)

                if best_fit[1] < score:
                    best_fit= (teammate["name"],score)


        if best_fit[0] is not None:
            assignments[task["name"]]= best_fit[0]
            for t in teammates:
                if t["name"] == best_fit[0]:
                    t["available_hours"] -= task["estimated_hours"]
        else:
            assignments[task["name"]]= None # No suitable teammate found
    #print(assignments)    
    return assignments

teammates_T1 =[{"name": "Nour", "skills": {"backend":1, "C++": 3}, "available_hours": 3}]
teammates_T2 =[{"name": "Ali", "skills": {"backend": 4, "frontend": 2}, "available_hours": 2},
               {"name": "Nour", "skills": {"backend":4, "C++": 3}, "available_hours": 3}]
teammates_T3 =[{"name": "Ali", "skills": {"backend": 4, "frontend": 4}, "available_hours": 13},
               {"name": "Nour", "skills": {"backend":5, "frontend": 5}, "available_hours": 7}]

print("Test 1 - no skill match:", assign_tasks(tasks, teammates_T1))
print("Test 2 - not enough hours:", assign_tasks(tasks, teammates_T2))

print("Test 3 - best scorer wins:", assign_tasks(tasks, teammates_T3))
