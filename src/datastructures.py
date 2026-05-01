class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

        # Miembros iniciales
        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

        self.add_member({
            "first_name": "Jimmy",
            "age": 5,
            "lucky_numbers": [1]
        })

    # No modificar
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    # Añadir miembro
    def add_member(self, member):
        new_member = {
            "id": member.get("id", self._generate_id()),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member)
        return new_member

    # Eliminar miembro
    def delete_member(self, id):
        for m in self._members:
            if m["id"] == id:
                self._members.remove(m)
                return True
        return False

    # Obtener un miembro
    def get_member(self, id):
        for m in self._members:
            if m["id"] == id:
                return m
        return None

    # Obtener todos los miembros
    def get_all_members(self):
        return self._members
