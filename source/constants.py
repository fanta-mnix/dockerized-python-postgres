def project_root():
    import os
    components = os.path.split(os.path.dirname(__file__))
    return os.path.join(*components[:-1])


def absolutify(*paths):
    import os
    return os.path.join(project_root(), *paths)
