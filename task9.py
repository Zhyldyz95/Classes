colors = {"BLACK": {"CATEGORY": "HUE",
                        "TYPE": "PRIMARY",
                        "CODE": {
                            "RGBA": [255, 255, 255, 1],
                            "HEX": "#000"
                        }
                        },
              "WHITE": {
                  "CATEGORY": "VALUE",
                  "TYPE": "PRIMARY",
                  "CODE": {
                      "RGBA": [0, 0, 0, 1],
                      "HEX": "#FFF"
                  }
              },
              "RED": {
                  "CATEGORY": "HUE",
                  "TYPE": "PRIMARY",
                  "CODE": {
                      "RGBA": [255, 0, 0, 1],
                      "HEX": "#FF0"
                  }
              },
              "BLUE": {
                  "CATEGORY": "HUE",
                  "TYPE": "PRIMARY",
                  "CODE": {
                      "RGBA": [0, 0, 255, 1],
                      "HEX": "#00F"
                  }
              },
              "YELLOW": {
                  "CATEGORY": "HUE",
                  "TYPE": "PRIMARY",
                  "CODE": {
                      "RGBA": [255, 255, 0, 1],
                      "HEX": "#FF0"
                  }
              },
              "GREEN": {
                  "CATEGORY": "HUE",
                  "TYPE": "SECONDARY",
                  "CODE": {
                      "RGBA": [0, 255, 0, 1],
                      "HEX": "#0F0"
                  }
              }
              }
class Data1:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.k = self.kwargs.keys()
        self.v = self.kwargs.values()

    def get_keys_tuple(self):
        return tuple(self.k)
    def get_values_tuple(self):
        return tuple(self.v)
    def get_keys_list(self):
        return list(self.k)
    def get_values_list(self):
        return list(self.v)
    def get_keys_set(self):
        return set(self.k)
    def get_values_set(self):
        return frozenset(self.v)

data = Data1(**colors)
print(data.k)
print(data.v)
print(data.get_keys_tuple())
print(data.get_values_tuple())
print(data.get_keys_list())
print(data.get_values_list())
print(data.get_keys_set())
print(data.get_values_set())
