from flask import Flask, render_template, request, redirect, url_for
from models import Patient, ClinicQueue

app = Flask(__name__)

# Initialize clinic queue (in-memory storage)
clinic = ClinicQueue()

@app.route('/')
def home():
    """Display the clinic home page with queue info"""
    queue_list = clinic.get_queue_list()
    queue_size = clinic.get_queue_size()
    patients_seen = clinic.patients_seen_today
    
    return render_template('index.html', 
                         queue=queue_list, 
                         queue_size=queue_size,
                         patients_seen=patients_seen)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new patient"""
    if request.method == 'POST':
        name = request.form.get('name')
        contact = request.form.get('contact')
        reason = request.form.get('reason')
        
        # Create new patient and add to queue
        patient = Patient(name, contact, reason)
        clinic.add_patient(patient)
        
        return redirect(url_for('home'))
    
    return render_template('register.html')

@app.route('/next-patient')
def call_next_patient():
    """Call the next patient in the queue"""
    patient = clinic.next_patient()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)