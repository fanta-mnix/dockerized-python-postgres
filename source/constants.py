def absolutify(*paths):
    import os
    *components, _ = os.path.split(os.path.dirname(__file__))
    return os.path.join(*components, *paths)
