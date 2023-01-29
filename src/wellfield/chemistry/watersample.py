

class Watersample:

    na = None
    cl = None

    def __init__(self, sample):
        for key in sample.keys():
            exec(f"self.{key} = sample['{key}']")

    def ionbytningsgrad(self):
        if hasattr(self, "na") & hasattr(self, "cl"):
            ig = round((self.na/23.0)/(self.cl/35.5), 2)
            return ig
        else:
            raise AttributeError("Sample doesn\'n contain parameters for calculating ionbytningsgrad")
