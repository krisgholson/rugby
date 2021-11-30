"""Sportlomo members command."""
import pandas as pd
import sportlomo

EXPORT_COLUMNS = ['club', 'first_name', 'last_name', 'gender', 'membership_package']
SORT_BY = ['club', 'membership_package', 'gender', 'last_name', 'first_name']


def main():
    """get members and print"""
    members = sportlomo.get_members()

    data_frame = pd.DataFrame.from_records(data=members, index='national_number')

    # print(members)
    print('member count (all SC): ' + str(len(members)))
    data_frame.sort_values(by=SORT_BY, inplace=True, key=lambda col: col.str.lower())
    filtered_df = data_frame.query("club == 'Charleston Youth and Junior Rugby' "
                                   "or club == 'Wando Rugby Football Club'")
    print('member count (WRFC): ' + str(len(filtered_df.index)))

    filtered_df.to_csv('./dist/sportlomo_sc_export.csv', columns=EXPORT_COLUMNS)


if __name__ == "__main__":
    main()
