"""Entry file for the main functionality."""

import logging
import json
from datetime import datetime as dt, timedelta, date
from report_helper import ReportHelper


logger = logging.getLogger(__file__)


def time_to_generate_monthly_report(today):
    """Check whether it is the right time to generate monthly report."""
    return today.day in (1, 2, 3, 4, 5, 6, 7)


def main():
    """Generate the weekly and monthly stacks report."""
    r = ReportHelper()

    today = dt.today()

    start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    end_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    weekly_response = r.get_report(start_date, end_date, 'weekly')
    logger.debug('Weekly report data from {s} to {e}'.format(s=start_date, e=end_date))
    logger.debug(json.dumps(weekly_response, indent=2))

    if time_to_generate_monthly_report(today):
        last_day_of_prev_month = date(today.year, today.month, 1) - timedelta(days=1)
        last_month_first_date = last_day_of_prev_month.strftime('%Y-%m-01')
        last_month_end_date = last_day_of_prev_month.strftime('%Y-%m-%d')
        monthly_response = r.get_report(last_month_first_date, last_month_end_date, 'monthly')
        logger.debug('Monthly report data from {s} to {e}'.format(s=start_date, e=end_date))
        logger.debug(json.dumps(monthly_response, indent=2))


if __name__ == '__main__':
    main()
