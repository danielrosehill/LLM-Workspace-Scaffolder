import os

def create_directory(path):
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, '.gitkeep'), 'w') as f:
        pass

def create_llm_workspace():
    # Create main directories
    main_dirs = ['agents', 'prompts', 'outputs']
    for main_dir in main_dirs:
        create_directory(main_dir)

    # Create subdirectories for prompts
    prompt_subdirs = ['active', 'drafts', 'archived']
    for subdir in prompt_subdirs:
        create_directory(os.path.join('prompts', subdir))

    # Create subdirectories for agents
    agent_subdirs = ['text-configs', 'json-configs']
    for subdir in agent_subdirs:
        create_directory(os.path.join('agents', subdir))

    # Create subdirectories for outputs
    output_subdirs = ['to-sort', 'by-subject', 'by-date']
    for subdir in output_subdirs:
        create_directory(os.path.join('outputs', subdir))

    print("LLM workspace folders created successfully.")

if __name__ == "__main__":
    create_llm_workspace()