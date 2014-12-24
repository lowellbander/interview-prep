def buildMap (students):
    mapping = {}
    for s in students:
        mapping[s.getID()] = s
    return mapping
