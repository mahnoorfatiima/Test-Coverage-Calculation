import requests
from projects import projects

# add Testrail subdomain in the base URL
BASE_URL = "https://<your-sub-domain>.testrail.com/index.php?/api/v2"
HEADERS = {"Content-Type": "application/json"}
# add your Testrail username and password
AUTH = ("<testrail-username>", "<testrail-password>")

if __name__ == '__main__':

    for project in projects:

        print(f"getting all suites in project: {project['title']} ...")
        getSuitesInProjectUrl = f"{BASE_URL}/get_suites/{project['id']}"
        response = requests.get(getSuitesInProjectUrl, headers=HEADERS, auth=AUTH)
        all_suites = response.json()
        suite_ids = [suite['id'] for suite in all_suites]

        all_pending_tests_in_project = []
        all_acceptance_tests_in_project = []

        for suite in suite_ids:
            getCasesInSuiteUrl = f"{BASE_URL}/get_cases/{project['id']}&suite_id={suite}"

            # values for pagination
            offset = 0
            limit = 250

            all_test_cases = []

            while True:
                url = f"{getCasesInSuiteUrl}&offset={offset}&limit={limit}"

                response = requests.get(url, headers=HEADERS, auth=AUTH)
                test_cases = response.json()

                if not test_cases.get("cases", []):
                    break

                all_test_cases.extend(test_cases.get("cases", []))

                offset += limit

            # Filter test cases with acceptance_tests = "pending" (id=2)
            filtered_test_cases = [case for case in all_test_cases if case.get("custom_automation_status") == 2]
            all_pending_tests_in_project.extend(filtered_test_cases)

            # Filter test cases with acceptance_tests = "done" (id=1)
            filtered_test_cases = [case for case in all_test_cases if case.get("custom_automation_status") == 1]
            all_acceptance_tests_in_project.extend(filtered_test_cases)

        all_tests = len(all_pending_tests_in_project) + len(all_acceptance_tests_in_project)
        print(f"Tests with Acceptance Tests as 'Pending' AND 'Done' in {project['title']} are: "
              f"{all_tests}")
        print(f"Tests with Acceptance Tests as 'Done' in {project['title']} are: "
              f"{len(all_acceptance_tests_in_project)}")
        if all_tests != 0:
            print(f" => Coverage Percentage: {round(((len(all_acceptance_tests_in_project) / all_tests) * 100), 2)} %")
        else:
            print(" => Coverage Percentage: N/A (No tests)")
        print("----------")
