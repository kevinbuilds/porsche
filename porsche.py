
class Porsche:
    def __init__(self, model: str,
                 price: int,
                 year: int,
                 energy= "thermic",
                 hp=0,
                 acceleration=0,
                 maxspeed=0,
                 exterior_color="grey",
                 interior_color="black"):
        self.model = model
        self.price = price
        # The year of its generation
        self.year = year
        # Defines if it's an electric, a hybrid or thermic engine
        self.energy = energy
        self.hp = hp
        self.acceleration = acceleration
        self.maxspeed = maxspeed
        self.exterior_color = exterior_color
        self.interior_color = interior_color

    def set_technicals(self, hp: int, acceleration: float, maxspeed: int):
        self.hp= hp
        self.acceleration= acceleration
        self.maxspeed= maxspeed
        return self.hp, self.acceleration, self.maxspeed

    def exterior_color(self, color: str):
        self.color=color
        return self.color

    def base_spec(self):
        dict= {
            "price": self.price,
            "year": self.year,
            "energy": self.energy,
            "technical": {
                "hp": self.hp,
                "acceleration": self.acceleration,
                "Max speed": self.maxspeed
            },
            "design": {
                "exterior color": self.exterior_color,
                "interior color": self.interior_color
            }
        }
        return dict


class Carrera(Porsche):
    def __init__(self, phase: str, convertible = False, **kwargs):
        super().__init__(**kwargs)
        self.phase = phase
        self.convertible = convertible

    def carrera_name(self):
        part_name = self.model + " " + self.phase
        if self.convertible is False:
            full_name = part_name
        else:
            full_name = part_name + " convertible."
        return full_name

    def carrera_card(self):
        carrera = {
            "full id": self.carrera_name(),
            "model": self.model,
            "phase": self.phase,
            "convertible": self.convertible,
        }
        return carrera

    def __repr__(self):
        return f"Porsche {self.carrera_name()}"

class Targa(Porsche):
    def __init__(self, phase: str, **kwargs):
        super().__init__(**kwargs)
        self.phase = phase

    def targa_name(self):
        full_name = self.model + self.phase
        return full_name

    def targa_card(self):
        targa = {
            "full id": self.targa_name(),
            "model": self.model,
            "phase": self.phase,
        }

        return targa

    def __repr__(self):
        return f"Porsche {self.targa_name()}."

class Turbo911(Porsche):
    def __init__(self, phase: str, convertible = False, **kwargs):
        super().__init__(**kwargs)
        self.phase = phase
        self.convertible = convertible

    def turbo911_name(self):
        part_name = self.model + " " + self.phase
        if self.convertible is False:
            full_name = part_name
        else:
            full_name = part_name + " convertible."
        return full_name

    def turbo_card(self):
        turbo911 = {
            "full id": self.turbo911_name(),
            "model": self.model,
            "phase": self.phase,
            "convertible": self.convertible,
        }

        return turbo911

    def __repr__(self):
        return self.turbo911_name()

class Cayman(Porsche):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cayman_card(self):
        cayman718 = {
            "model": self.model
        }

        return cayman718

    def __repr__(self):
        return f"Porsche {self.model}"

class Boxster(Cayman):
    def __init__(self, convertible = True, **kwargs):
        super().__init__(**kwargs)
        self.convertible = convertible

    def boxster_card(self):
        boxter718 = {
            "model": self.model
        }

        return boxter718

    def __repr__(self):
        return f"Porsche {self.model}"


class Taycan(Porsche):
    def __init__(self, type: str, **kwargs):
        super().__init__(**kwargs)
        self.type = type

    def taycan_name(self):
        assert "taycan" in self.model.lower()
        full_name = self.model + self.type
        return full_name

    def taycan_card(self):
        taycan = {
            "full name": self.taycan_name(),
            "model": self.model,
            "type": self.type
        }
        return taycan

    def __repr__(self):
        return f"Porsche {self.taycan_name()}"

class Panamera(Porsche):
    def __init__(self, type: str, **kwargs):
        super().__init__(**kwargs)
        self.type = type

    def panamera_name(self):
        assert "panamera" in self.model.lower()
        full_name = self.model + self.type
        return full_name

    def panamera_card(self):
        panamera = {
            "full name": self.panamera_name(),
            "model": self.model,
            "type": self.type
        }
        return panamera

    def __repr__(self):
        return f"Porsche {self.panamera_name()}"

class Macan(Porsche):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def macan_name(self):
        assert "macan" in self.model.lower()
        full_name = self.model + self.type
        return full_name

    def macan_card(self):
        macan = {
            "full name": self.macan_name(),
            "model": self.model,
            "type": self.type
        }
        return macan

    def __repr__(self):
        return f"Porsche {self.macan_name()}"

class Cayenne(Porsche):
    def __init__(self, type: str, **kwargs):
        super().__init__(**kwargs)
        self.type = type

    def cayenne_name(self):
        full_name = self.model + self.type
        return full_name

    def cayenne_card(self):
        cayenne = {
            "full name": self.cayenne_name(),
            "model": self.model,
            "type": self.type
        }

    def __repr__(self):
        return f"Porsche {self.cayenne_name()}."
