import sys
import json
import time
from benchmark_test import run_test
from auxiliary_functions import Auxiliary
from send_recieve import send_prompt_recieve_response



if __name__ == "__main__":
    aux = Auxiliary()
    start = time.time()
    with open("config.json", "r") as f:
        config = json.load(f)

    task = config["task"]
    model_specs = config["model_specifications"]
    seed = config["seed"]
    path = config["path"]
    num_of_processes = config["num_of_processes"]
    questions_req = aux.extract_questions_params_inputs(config["questions"])
    number_of_rounds = aux.extract_result_folder_numbers(config["number_of_rounds"])

    if task == "call_llm":
        for q, r in questions_req.items():
            for num in number_of_rounds:
                send_prompt_recieve_response(path, q, r, model_specs, seed, num)
        print("Calling the LLM is complete.")
        
    elif task == "test":
        for q, r in questions_req.items():
            test_durations = []
            binary_correctness = []
            number_of_parameters = r.get("number_of_parameters")
            all_runs_q_test_start = time.time()
            
            for num in number_of_rounds:
                test_start = time.time()
                binary_correctness += run_test(q, r, model_specs, num, num_of_processes)
                test_durations.append(time.time() - test_start)

            aux.write_html_report(
                path,
                model_specs,
                seed,
                q,
                questions_req,
                number_of_rounds,
                binary_correctness,
                number_of_parameters,
                test_durations
            )
            number_of_all_trials =  number_of_parameters * len(number_of_rounds)
            corr_sc = sum(binary_correctness) / number_of_all_trials
            all_runs_q_test_end = time.time()
            report_content = {
                "Question": q,
                "RCS": corr_sc,
                "Distribution": binary_correctness,
                "Time": all_runs_q_test_end - all_runs_q_test_start,
            }

            with open(f"Q{q}/Q{q}_stats.json", "w") as f:
                json.dump(report_content, f, ensure_ascii=False, indent=2)
        print("Benchmarking process is complete.")
    sys.exit()
