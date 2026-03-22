from datetime import datetime
from collections import deque

class Patient:
    '''Represents a patient in the clinic queue'''
    
    def __init__(self, name, contact, reason):
        self.name = name
        self.contact = contact
        self.reason = reason
        self.registration_time = datetime.now()
        self.status = "Waiting"
    
    def check_in(self):
        '''Mark patient as checked in'''
        self.status = "Checked In"
    
    def complete(self):
        '''Mark patient as completed'''
        self.status = "Completed"
    
    def get_info(self):
        '''Return patient information as dict'''
        return {
            "name": self.name,
            "contact": self.contact,
            "reason": self.reason,
            "time": self.registration_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }

class ClinicQueue:
    '''Manages the FIFO queue of patients'''
    
    def __init__(self):
        self.queue = deque()
        self.patients_seen_today = 0
    
    def add_patient(self, patient):
        '''Add a patient to the queue'''
        self.queue.append(patient)
    
    def next_patient(self):
        '''Remove and return the next patient in queue'''
        if self.queue:
            patient = self.queue.popleft()
            patient.check_in()
            self.patients_seen_today += 1
            return patient
        return None
    
    def get_queue_list(self):
        '''Return list of all patients in queue'''
        return [patient.get_info() for patient in self.queue]
    
    def get_queue_size(self):
        '''Return number of patients waiting'''
        return len(self.queue)