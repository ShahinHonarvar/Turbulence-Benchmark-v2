import platform


def pytest_html_report_title(report):
    report.title = "Question 54 with parameters set no. 38"


def pytest_configure(config):
    config._metadata = {
        "Benchmarking framework": "Turbulence",
        "Operating system": platform.platform(),
        "Python version": platform.python_version()
    }


def pytest_html_results_table_header(cells):
    cells.pop()


def pytest_html_results_table_row(cells):
    cells.pop()