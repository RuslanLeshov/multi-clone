
data = {
    "s3-storage": {
        "name": "S3 object storage",
        "description": "S3-compatible object storage server implemented in Java using Spring Boot",
        "url": "git@github.com:RuslanLeshov/s3-storage.git",
        "folder": "~/repos/java/s3-storage"
    },
    "multi-clone": {
        "name": "MultiClone",
        "description": "Multiple git repositories cloner implemented in Python using Textual",
        "url": "git@github.com:RuslanLeshov/multi-clone.git",
        "folder": "~/repos/python/multi-clone"
    },

    "nsu-labs": {
        "name": "NSU labs",
        "description": "Various labs I did during my studies at NSU",
        "url": "git@github.com:RuslanLeshov/nsu-labs.git",
        "folder": "~/repos/misc/nsu-labs"
    },
    
}


bundles = {
    "all": {
        "name": "Everything",
        "description": "Literally everything",
        "projects": ["S3-storage", "multi-clone", "nsu-labs"]
    },
    "nsu": {
        "name": "NSU labs",
        "description": "All NSU labs projects",
        "projects": ["nsu-labs"]
    }
}