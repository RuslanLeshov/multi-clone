
class Project:
    id: str
    name: str
    url: str
    folder: str
    
    def __init__(self, id: str, name: str, url: str, folder: str):
        self.id = id
        self.name = name
        self.url = url
        self.folder = folder

data = [
    Project(
        id = "S3-storage",
        name="S3 object storage",
        url = "git@github.com:RuslanLeshov/s3-storage.git",
        folder = "~/repos/java/s3-storage"
    ),
    Project(
        id = "multi-clone",
        name= "Multiple git repositories cloner",
        url = "git@github.com:RuslanLeshov/multi-clone.git",
        folder = "~/repos/python/multi-clone"
    ),
    Project(
        id = "nsu-labs",
        name="NSU labs",
        url = "git@github.com:RuslanLeshov/nsu-labs.git",
        folder = "~/repos/misc/nsu-labs"
    ),
    
]


bundles = [
    {
        "id": "all",
        "name": "Literally everything",
        "projects": ["S3-storage", "multi-clone", "nsu-labs"]
    },
    {
        "id": "nsu",
        "name": "NSU labs",
        "projects": ["nsu-labs"]
    }
]