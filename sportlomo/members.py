"""Sportlomo members command."""
import pandas as pd
import sportlomo

EXPORT_COLUMNS = ['club', 'first_name', 'last_name', 'gender', 'membership_package']
SORT_BY = 'last_name'


def main():
    """get members and print"""
    members = sportlomo.get_members()

    data_frame = pd.DataFrame.from_records(data=members, index='national_number')

    # print(members)
    print(len(members))
    data_frame.sort_values(by=SORT_BY, inplace=True)
    data_frame.to_csv('./dist/sportlomo_sc_export.csv', columns=EXPORT_COLUMNS)


if __name__ == "__main__":
    main()
