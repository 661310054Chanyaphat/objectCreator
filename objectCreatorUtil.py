import maya.cmds as cmds

def create_object(obj_type: str, name: str = None):
    
    obj_map = {
        "cube": cmds.polyCube,
        "cone": cmds.polyCone,
        "sphere": cmds.polySphere,
        "torus": cmds.polyTorus,
    }

    if obj_type not in obj_map:
        cmds.warning(f"Unknown object type: {obj_type}")
        return None

    create_func = obj_map[obj_type]
    obj, _ = create_func()

    
    if name:
        obj = cmds.rename(obj, name)

    return obj
