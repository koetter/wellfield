import datetime

class Wellfield:

    def __init__(self, name):
        self.name = name
        self.created_date = datetime.date.today()
        self.wells = {}

    def add_well(self, wellno, welltype, dguno):
        #TODO Check that well doesn't exist
        self.wells[wellno] = well

    def get_well(self, wellno):
        #TODO: check that well exist
        well = self.wells[wellno]
        return well

    def list_wells(self):
        for well in self.wells:
            print(well)
    
