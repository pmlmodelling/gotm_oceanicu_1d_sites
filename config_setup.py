import shutil

base_dir = "./"


def merge_gotm_yaml(site, model):
    import os
    from ruamel.yaml import YAML

    # Initialize YAML object
    yaml = YAML()

    f1 = f"{base_dir}/{site}/gotm.yaml"
    f2 = f"{base_dir}/gotm-snippets/gotm_fabm_{model}.yaml"

    # Read the original file
    with open(f1, "r") as file:
        original_data = yaml.load(file)

    # Read the update file
    with open(f2, "r") as file:
        update_data = yaml.load(file)

    # Update the original data with the new data
    original_data.update(update_data)

    if not os.path.exists(f"{f1}.org"):
        shutil.copy(f1, f"{f1}.org")

    #    shutil.copy(f1, f2)
    # Write the updated data back to the original file
    with open(f1, "w") as file:
        yaml.dump(original_data, file)


def copy_fabm_yaml_file(site, model):
    f1 = f"{base_dir}/fabm-yaml/fabm_{model}.yaml"
    f2 = f"{base_dir}/{site}/fabm.yaml"

    shutil.copy(f1, f2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("site")
    parser.add_argument("model")
    args = parser.parse_args()

    merge_gotm_yaml(args.site, args.model)

    copy_fabm_yaml_file(args.site, args.model)
