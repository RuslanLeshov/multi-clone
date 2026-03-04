import subprocess
from pathlib import Path
from textual import log
from Projects import data as projects_data, bundles as bundles_data


def install_projects(projects: list[str]):
    for project in projects:
        log.info(f"Installing project: {project}")
        data = projects_data[project]
        create_folder(data["folder"])
        clone_repo(data["url"], data["folder"])


def install_bundles(bundles: list[str]):
    for bundle in bundles:
        log.info(f"Installing bundle: {bundle}")
        data = bundles_data[bundle]

        log.info(f"Creating bundle folder: {data['folder']}")


def create_folder(path: str):
    log.info(f"Creating folder: {path}")
    Path(path).expanduser().resolve().mkdir(parents=True, exist_ok=True)

def clone_repo(url: str, folder: str):
    target = Path(folder).expanduser().resolve()
    log.info(f"Cloning repository: {url} into {target}")
    result = subprocess.run(
        ["git", "clone", url, target], 
        capture_output=True, 
        text=True
    )
    if result.returncode == 0:
        log.info(f"Successfully cloned {url} into {target}")
    else:
        log.error(f"Failed to clone {url} into {target}. Error: {result.stderr}")
