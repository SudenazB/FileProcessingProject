schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "minLength": 1,
            "maxLength": 64
        },
        "attributes": {
            "type": "object",
            "properties": {
                "val_0": {"type": "string"},
                "val_1": {"type": "string"},
                "val_2": {"type": "string"},
                "val_3": {"type": "string"},
                "val_4": {"type": "string"},
                "val_5": {"type": "string"},
                "val_6": {"type": "string"},
                "val_7": {"type": "string"},
                "val_8": {"type": "string"},
                "val_9": {"type": "string"}
            },
            "required": [
                "val_0", "val_1", "val_2", "val_3", "val_4",
                "val_5", "val_6", "val_7", "val_8", "val_9"
            ]
        }
    },
    "required": ["id", "attributes"]
}
