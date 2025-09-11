# Turbulence-Benchmark-v2 <a id="top"></a>

**Turbulence** is a benchmark and automated testing framework based on the **question neighbourhood approach** for systematically evaluating instruction-tuned large language models (LLMs) for code generation. It measures:

- **Accuracy (AS):** the overall rate of correctness across all generated outputs.  
- **Correctness Potential (CPS):** whether the LLM produces at least one correct output for a given input.  
- **Consistent Correctness (CCS):** the model’s ability to consistently produce correct outputs for the same input across successive generations.

---

# 📖 Table of Contents

- [Turbulence-Benchmark-v2 ](#turbulence-benchmark-v2-)
- [📖 Table of Contents](#-table-of-contents)
  - [📘 Overview ](#-overview-)
- [⚙️ Execution Instructions ](#️-execution-instructions-)
  - [🛠️ Step 1: Install Required Libraries ](#️-step-1-install-required-libraries-)
  - [🔑 Step 2: Set API Keys as Environment Variables ](#-step-2-set-api-keys-as-environment-variables-)
  - [📝 Step 3: Define Prerequisite Settings ](#-step-3-define-prerequisite-settings-)
  - [▶️ Step 4: Execution ](#️-step-4-execution-)
- [🗂️ Repository Organisation ](#️-repository-organisation-)
  - [📂 Inside Each Question Subfolder (Qn) ](#-inside-each-question-subfolder-qn-)
  - [🧪 Execution Rounds ](#-execution-rounds-)


---

## 📘 Overview <a id="overview"></a>

Turbulence consists of a large set of natural language **question templates**—each a parameterised programming problem that can be instantiated in many different forms. Every template is paired with a **test oracle** that determines whether a code solution returned by an LLM is correct. This allows the generation of a **neighbourhood of closely related questions** from a single template, enabling fine-grained assessment of model behaviour across similar tasks.

Turbulence systematically identifies cases where an LLM can solve some instances within a neighbourhood but fails to generalise across the entire set. By employing **accuracy**, **correctness potential**, and **consistent correctness** as core metrics, Turbulence provides a structured methodology to reveal model weaknesses and offers a more nuanced characterisation of LLM behaviour in structured problem spaces.

**Version 2 (v2) update:** this is the direct update to version 1. In v2, two new metrics and rigorous statistical analysis have been added to the source code.

🌐 The complete benchmark and dataset are also publicly available on [IEEE DataPort](https://ieee-dataport.org/documents/turbulence-benchmark-v2).

[⬆️ Back to top](#top)

---

# ⚙️ Execution Instructions <a id="execution-instructions"></a>

To execute the benchmark, please ensure that your operating system is either **Linux** or **macOS**, and that Python version **3.10 or higher** is installed. Follow the steps below in the specified order:

## 🛠️ Step 1: Install Required Libraries <a id="step-1"></a>

Open the terminal and use the `cd` command to move into the Turbulence folder. Then run:

```bash
pip install -r requirements.txt
```

## 🔑 Step 2: Set API Keys as Environment Variables <a id="step-2"></a>

Configure the API keys as environment variables on your operating system. Depending on the API and the platform you use to access the LLM, you may need to modify the content of `run_llm.py`.

## 📝 Step 3: Define Prerequisite Settings <a id="step-3"></a>

Download the `Source_Code` folder. In the `config.json` file, define the prerequisite settings as outlined below. The **keys must remain unchanged**, but their values can be adjusted based on your preferences.

- **`task`**:  
  Set this to `"run_llm"` when generating responses from the LLM, or `"test"` when testing previously generated responses.

- **`model_specifications`**:  
  Define the LLM’s name, maximum generation length (`max_tokens`), and temperature.

- **`seed`**:  
  Sets the random seed for reproducibility.

- **`questions`**:  
  Specify which question templates to use:  
  - A single number (e.g., `34`) for one question template.  
  - A range (e.g., `24-45`) for consecutive question templates.  
  - A list (e.g., `1, 5, 57`) for non-consecutive question templates. The order of numbers does not matter.  
  - A combination (e.g., `1, 5, 57, 25-45`) is also allowed.  
  - To use all templates, write `1-60`.

- **`number_of_parameters`**:  
  Sets the number of instances per neighbourhood.

- **`shuffle`**:  
  If `"True"`, shuffles question instances within each neighbourhood before sending them to the LLM.

- **`fuzzy_testing`**:  
  If `"True"`, runs additional fuzz testing after the fixed test suites. If `"False"`, skips fuzz testing to reduce evaluation cost.

- **`number_of_fuzzy_inputs`**:  
  The number of random inputs to be generated for the fuzzy testing phase.

- **`terminates_with_first_error`**:  
  If `"True"`, stops the testing campaign upon encountering the first failure.

- **`allowed_time`** and **`allowed_memory`**:  
  Set the time (in seconds) and memory (in GB) limits for executing each test. These settings help control evaluation cost and prevent the testing process from stalling due to overly complex or resource-intensive outputs generated by the LLM.

- **`number_of_rounds`**:  
  Number of times each instance is sent to the LLM.

- **`num_of_processes`**:  
  Number of processes to use during testing.

- **`confidence_level`**:  
  Statistical confidence level for analysis.

- **`path`**:  
  Absolute path to the Turbulence source code and config file.

## ▶️ Step 4: Execution <a id="step-4"></a>

Make sure you are in the folder. Next, enter the command `python3 main.py` and press the enter key to execute it.

[⬆️ Back to top](#top)

---

# 🗂️ Repository Organisation <a id="repository-organisation"></a>

In addition to the **Source_Code** folder, there are **44 folders**, each serving a specific LLM. For instance, `Claude_3_5_Haiku_T_0` consists of the results for Claude 3.5 Haiku with a temperature setting of 0, while `Claude_3_5_Haiku_T_D` contains the results for the same model but with the default temperature. Each of these primary folders contains **60 subfolders** and **three result JSON files**: `Classified_AS.json`, `Classified_CPS.json`, and `Classified_CCS.json`.

## 📂 Inside Each Question Subfolder (Qn) <a id="inside-qn"></a>

Within each subfolder labelled `Q<n>` (where `n` is a question number between 1 and 60), there are five subfolders and multiple files. The pair of (*question template*, *test oracle*) for each question is available here. The `question.txt.template` file contains the question in English. `genparams.py` contains a function for generating unique random parameter values to replace placeholders in the template. With some question templates, we manually wrote **20 parameter values representing the edge cases**...
When such hand-chosen parameter values were used, they are documented in a file called `manually_chosen_params.txt`.

Other files include:  
- `test.py.template` → template test cases.  
- `solution.py.template` → solution template.  
- `gen_function_params.py` → generates fuzzy inputs.  
- `Final_report*.html` → HTML summary reports.  
- `stats.json` → three metric scores + correctness distributions.

[⬆️ Back to top](#top)

## 🧪 Execution Rounds <a id="execution-rounds"></a>

Each question instance was given to the LLM **five times** (`number_of_rounds = 5`). Subfolders named after the LLM, ending with `result_<number>` (1 ≤ number ≤ 5), contain rounds of experiments, each with **100 folders** and various files such as the `all_params.txt` file that holds all parameter values generated by `genparams.py`. Other files include reports, for example, on parameter values to which the LLM generated correct (`correct_params.html`) or incorrect (`wrong_params.html`) answers. Folders l...

[⬆️ Back to top](#top)
