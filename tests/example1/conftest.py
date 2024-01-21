def pytest_configure(config):
    ##Initialize variables to store test results.
    config._successful_tests = []
    config._failed_tests = []

def pytest_runtest_makereport(item, call):
    ##Hook to capture the result of each test item.
    if call.when == "call":
        if call.excinfo is None or call.excinfo.typename != "AssertionError":
            item.config._successful_tests.append(item.name)
        else:
            item.config._failed_tests.append(item.name)

def pytest_sessionfinish(session, exitstatus):
    ##Hook to execute at the end of the test session.
    print("\nSuccessful tests:", session.config._successful_tests)
    print("Failed tests:", session.config._failed_tests)