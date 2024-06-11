def extract_final_round_values(data):
    max_rounds = data['max_rounds'] + 1
    steps = data['n_steps'] + 1
    
    final_value = {}
    
    for round in range(max_rounds):
        for step in range(steps):
            key = f"r{round}s{step}"
            if key in data:
                obj = data[key] 
                round_steps = []
                for o_step in obj['steps']:
                    step_obj = {}
                    for param in o_step['param']:
                        if 'name' in param and 'value' in param:
                            step_obj[param['name']] = param['value']

                    round_steps.append(step_obj)
                final_value["data"] = round_steps
                final_value["index"] = key
    return final_value

def parse_sampling_output(file_path):
    lines = ""

    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Remove any lines that don't contain "% Done "
    lines = [line for line in lines if '% Done ' in line]

    percents = []
    percent = 0
    for line in lines:
        percent = float(line.split('% Done ')[0].strip())
        percents.append(percent)

    return {"percent": percent, "data": percents}

def parse_pso_error(file_path, num_steps):
    lines = ""
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    lines = [line for line in lines if 'best_cost' in line]
    lines = [line.replace("pyswarms.single.global_best: ", "") for line in lines]

    round = 1
    step = 1

    round_steps = {}
    percents = []
    best_costs = []
    in100s = False
    percent = 0
    for line in lines:
        best_cost = float(line.split('best_cost=')[1].strip())
        percent = float(line.split('%')[0].strip())

        best_costs.append(best_cost)
        percents.append(percent)

        # Percent is less than last percent or we are at the end of the file
        if (percent == 100 and not in100s):
            in100s = True

            round_steps[f"Round: {round} - Step: {step}"] = {
                "best_cost": best_costs.copy(),
                "percent": percents.copy()
            }

            best_costs = []
            percents = []
            
            step += 1
            if step > num_steps:
                step = 1
                round += 1

        if percent != 100:
            in100s = False

    return {"round": round, "step": step, "percent": percent, "data": round_steps}
