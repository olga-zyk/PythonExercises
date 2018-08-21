# Christmas is coming. Elves are busy producing decorations.
# Each one has a to produce a different amount of items (quota).
# Load data from `elves.json` and create a report `elves.txt`.
# An example report is displayed in `elves_sample.txt`

# Your code here
import json


class Elves:

    def __init__(self, config):
        self.report_file = 'elves.txt'
        self.data = None

        self.load(config['file_name'])

    def load(self, filename):
        try:
            with open(filename, 'r') as json_file:
                self.data = json.load(json_file)
        except IOError as io_error:
            print 'Error loading file. {0}'.format(io_error)
        except ValueError as val_error:
            print 'File decoding error. {0}'.format(val_error)

    def write_report(self):
        if self.data is None:
            return

        data_report = []
        self.format_elves(data_report)

        try:
            with open(self.report_file, 'w+') as report:
                report.write('\n'.join(data_report))
        except IOError as io_error:
            print('Data could not be written to file. {error}'.format(error=io_error))
        else:
            print 'Report was successfully saved to "{file_name}" file'.format(file_name=self.report_file)

    def format_elves(self, data_report):
        for elf in self.data['elves']:
            data_report.append(
                '=========\nElf: {elf[name]} {elf[surname]}\nQuota: {elf[quota]}'.format(elf=elf)
            )
