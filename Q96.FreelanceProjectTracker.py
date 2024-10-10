# Freelance Project Tracker: Stack for undoing project submissions, queue for processing client requests, and list to track ongoing projects.

class FreelanceProjectTracker:
    def __init__(self):
        self.submission_stack = []  # Stack to undo project submissions
        self.client_request_queue = []  # Queue to process client requests
        self.ongoing_projects_list = []  # List to track ongoing projects
    
    # Method to submit a project (push to stack)
    def submit_project(self, project):
        self.submission_stack.append(project)
        print(f"Project '{project}' submitted.")

    # Method to undo the last submitted project (pop from stack)
    def undo_last_submission(self):
        if self.submission_stack:
            undone_project = self.submission_stack.pop()
            print(f"Project submission '{undone_project}' undone.")
            return undone_project
        else:
            print("No project submission to undo.")
            return None

    # Method to add a client request (enqueue)
    def add_client_request(self, request):
        self.client_request_queue.append(request)
        print(f"Client request '{request}' added to queue.")

    # Method to process a client request (dequeue)
    def process_client_request(self):
        if self.client_request_queue:
            processed_request = self.client_request_queue.pop(0)
            print(f"Processing client request: '{processed_request}'")
            return processed_request
        else:
            print("No client requests to process.")
            return None

    # Method to add an ongoing project to the list
    def add_ongoing_project(self, project):
        self.ongoing_projects_list.append(project)
        print(f"Ongoing project '{project}' added to list.")

    # Method to view ongoing projects
    def view_ongoing_projects(self):
        if self.ongoing_projects_list:
            print("Ongoing projects:")
            for project in self.ongoing_projects_list:
                print(f"- {project}")
        else:
            print("No ongoing projects.")

# Example usage:
tracker = FreelanceProjectTracker()

# Submitting projects
tracker.submit_project("Website Design")
tracker.submit_project("Mobile App Development")

# Undoing the last project submission
tracker.undo_last_submission()

# Adding client requests to the queue
tracker.add_client_request("New logo design")
tracker.add_client_request("SEO optimization")

# Processing client requests
tracker.process_client_request()

# Adding ongoing projects
tracker.add_ongoing_project("Website Redesign")

# Viewing ongoing projects
tracker.view_ongoing_projects()
