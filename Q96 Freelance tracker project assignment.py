

class FreelanceProjectTracker:
    def __init__(self):
        self.submission_stack = []  
        self.client_request_queue = []  
        self.ongoing_projects_list = []  
    
    
    def submit_project(self, project):
        self.submission_stack.append(project)
        print(f"Project '{project}' submitted.")

    
    def undo_last_submission(self):
        if self.submission_stack:
            undone_project = self.submission_stack.pop()
            print(f"Project submission '{undone_project}' undone.")
            return undone_project
        else:
            print("No project submission to undo.")
            return None

    
    def add_client_request(self, request):
        self.client_request_queue.append(request)
        print(f"Client request '{request}' added to queue.")

    
    def process_client_request(self):
        if self.client_request_queue:
            processed_request = self.client_request_queue.pop(0)
            print(f"Processing client request: '{processed_request}'")
            return processed_request
        else:
            print("No client requests to process.")
            return None

    
    def add_ongoing_project(self, project):
        self.ongoing_projects_list.append(project)
        print(f"Ongoing project '{project}' added to list.")

    
    def view_ongoing_projects(self):
        if self.ongoing_projects_list:
            print("Ongoing projects:")
            for project in self.ongoing_projects_list:
                print(f"- {project}")
        else:
            print("No ongoing projects.")


tracker = FreelanceProjectTracker()


tracker.submit_project("tracker1")
tracker.submit_project("tracker2")


tracker.undo_last_submission()


tracker.add_client_request("horizon")
tracker.add_client_request("volcano")


tracker.process_client_request()


tracker.add_ongoing_project("star")


tracker.view_ongoing_projects()
