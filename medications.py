class Medication:
    def __init__(self, name, dose, frequency, start_date, end_date=None):
        self.name = name
        self.dose = dose
        self.frequency = frequency
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"{self.name} ({self.dose})"


def add_medication(med_list, medication):
    med_list.append(medication)


def remove_medication(med_list, medication_name):
    med_list[:] = [med for med in med_list if med.name != medication_name]


def list_medications(med_list):
    return med_list


def find_medication(med_list, medication_name):
    for med in med_list:
        if med.name == medication_name:
            return med
    return None
