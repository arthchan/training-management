#!/usr/bin/env python3
"""Process report."""

# Import libraries
from common import get_timestamp, read_configuration_file
import pandas as pd
import glob

# Configure Pandas
pd.set_option('mode.chained_assignment', None)


# Function for generating report in CSV format
def generate_report(config):
    """Generate report in CSV format."""
    # Initialise dataframe for all data
    df_all = pd.DataFrame([])

    # Read individual reports
    files = glob.glob("reports/*.csv")
    for f in files:
        df = pd.read_csv(f)

        # Append data to main dataframe
        df_all = pd.concat([df_all, df], ignore_index=True)

    # Export report as CSV file in local folder
    df_all.to_csv(config["report_path"], index=False, encoding="utf_8_sig")

    # Export report as CSV file to Personal OneDrive
    try:
        df_all.to_csv(config["report_abs_path"], index=False,
                      encoding="utf_8_sig")
    except BaseException:
        df_all.to_csv(config["report_abs_path"].split(".csv")[0] + '_' +
                      get_timestamp(format="%Y%m%d-%H%M") + ".csv",
                      index=False, encoding="utf_8_sig")

    finally:
        pass

    return df_all


if __name__ == "__main__":
    # Read configuration file
    config = read_configuration_file()

    # Generate report
    generate_report(config)
