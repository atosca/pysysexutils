import mido
import csv

""" 
Translates sysex to csv and vice versa.

@TODO: write a cli wrapper

"""

def csv_to_syx(csv_file_name, syx_file_name):
        """Writes csv file to sysex.

        csv format: one column which maps to a list of bytes
        @TODO: Map bytes

        """
        with open(csv_file_name, "rU") as f:
                reader = csv.reader(f)
                vals = list(reader)
        data = []
        for i in vals:
                data.append(int(i[0]))
        msg = mido.Message('sysex', data=data)
        mido.write_syx_file(syx_file_name, [msg])

def syx_to_csv(syx_file_name, csv_file_name):
    """Writes sysex file to csv.

    csv format: one column which maps to a list of bytes
    @TODO: Map bytes
    """
    msg = mido.read_syx_file(syx_file_name)
    vals = msg[0].data
    with open(csv_file_name, "wb") as f:
        wr = csv.writer(f)
        for i in vals:
            wr.writerow([i])


