records = [
    "What do you need;Released: 03 September 2011;Label: Apple Music;1;1;1;3;4;1;1",
    "Echoes of Silence;Released: 21 December 2011;Label: XO Records;5;3;2;7;1;4;6",
    "Midnight Memories;Released: 25 November 2013;Label: Columbia Records;1;2;1;1;3;2;2",
    "Random Access Memories;Released: 17 May 2013;Label: Columbia Records;3;1;1;5;2;3;1",
    "25;Released: 20 November 2015;Label: XL Recordings;1;1;1;1;1;1;1",
    "After Hours;Released: 20 March 2020;Label: XO Records;2;1;2;2;1;1;3",
    "Melodrama;Released: 16 June 2017;Label: Republic Records;2;2;1;4;3;5;2",
    "Dawn FM;Released: 7 January 2022;Label: XO Records;3;1;3;3;4;2;1",
]

chart = ["USA", "UK", "CAN", "AUS", "FRA", "GER", "JPN"]


# Activity 1
class Record:
    """Class to define the Record schema"""

    title: str = ""
    released: str = ""
    label: str = ""
    top_nmr: dict = {}

    # Part of activity 2
    def get_number_one(self):
        """Function that returns the number one record in all countries"""

        for number in self.top_nmr[0].values():
            if number != "1":
                return False

        return True


#  Activity 2
def parse_data(chart: list, records: list) -> list:
    """Function to parse records data from a list"""

    data = []
    for record in records:
        split = record.split(";")

        split[0] = f"Title: {split[0]}"

        tops = {
            chart[0]: split[3],
            chart[1]: split[4],
            chart[2]: split[5],
            chart[3]: split[6],
            chart[4]: split[7],
            chart[5]: split[8],
            chart[6]: split[9],
        }

        split[3:] = ""
        split.append(tops)

        data.append(split)

    return data


def create_instances(records: list) -> list[Record]:
    """Function to create instances from the Record class"""

    clean_data = parse_data(chart, records)
    my_Records = []

    for record in clean_data:
        new_record = Record()

        new_record.title = record[0]
        new_record.released = record[1]
        new_record.label = record[2]
        new_record.top_nmr = record[3:]

        my_Records.append(new_record)

    return my_Records


def number_one(records: list[Record]) -> str:
    """Function to print the number one record in all countries"""

    for record in records:
        if record.get_number_one():
            return f"{(record.title).split(': ')[1]} released on {(record.label).split(': ')[1]} is number one in all countries."

    return None


def run():
    my_records = create_instances(records)
    print(number_one(my_records))


if __name__ == "__main__":
    run()
