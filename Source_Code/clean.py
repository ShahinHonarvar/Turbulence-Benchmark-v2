import os

for q in range(56,61):
    for dirpath, dirnames, filenames in os.walk(f"Q{q}/", topdown=False):
        for filename in filenames:
            if filename.startswith("Final") or filename.startswith(f"Q{q}_stats"):
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)

    for r in range(1, 6):
        for dirpath, dirnames, filenames in os.walk(f"Q{q}/codegemma_results_{r}/", topdown=False):
            for filename in filenames:
                if filename.startswith("all_params") or filename.startswith("response") or filename.startswith("info") or filename.startswith("model_specs"):
                    continue
                file_path = os.path.join(dirpath, filename)
                os.remove(file_path)


