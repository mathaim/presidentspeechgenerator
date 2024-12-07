# presidentspeechgenerator
Web scrapes presidential speeches, fine tunes an LLM on speech data to generate responses like presidents, and deploys a local dash app to interact with it


### Step 1: Start an HPC sessions with the following specifications:
- GPU
- Number of cores: 1
- Memory request in GB: ~80
- GPU Type: NVIDIA A100
- Number of GPUs: 1
- Optional: Slurm Option (Reservation, Constraint): --constraint=a100_80gb

### Step 2: Run webscrape.ipynb after importing any necessary libraries
  1. Alternatively download the merged_data.zip file and make sure it is in your directory

### Step 3: Run speech-llama3.1.ipynb after importing necessary libraries
- Make sure a folder called "fine_tuned_model" is generated in your directory containing the following files:
  1. adpater_config.json
  2. adapter_model.safetensors
  3. README.md
  4. special_tokens_map.json
  5. tokenizer_config.json
  6. tokenizer.json

### Step 4: Save the app.py file in your directory 

### Step 5: Through HPC, generate an interactive desktop on one or more compute nodes. You will have full access to the resources these nodes provide. This is analogous to an interactive batch job. It should have the following specifications:
  1. Interactive
  2. Number of cores: 1
  3. Memory request in GB: ~8GB
  4. Optional GPU for interactive participation: Yes
  5. Number of GPUs: 1

### Step 6: Open a terminal and enter "module load miniforge"

### Step 7: Create a virtual environment

### Step 8: Type python app.py and import any libraries it requires that prevents the app from launching

### Step 9: Launch the app and ask a president their thoughts on a topic!
