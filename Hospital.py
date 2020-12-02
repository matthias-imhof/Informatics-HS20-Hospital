from abc import ABC, abstractmethod

class Hospital:
	def __init__(self, HospitalName, Employees):
		self._Hospitalname = HospitalName
		self._employees = Employees

	def find_doctor(self,patient):
		for i in self._employees:
			if isinstance(i, Doctors):
				if patient._problem.lower() == i.can_treat.lower():
					temp = patient._problem
					i.treat(patient)
					return 'Patient\'s problem: {} could be treated and the patient: {} {} is healthy again :)'.format(temp, patient._firstname,patient._lastname)
		if len(patient._problem) > 0:
			return 'Patient: {} {} couldn\'t be treated as there is no doctor in the {} hospital to treat: {}'.format(patient._firstname, patient._lastname, self._Hospitalname, patient._problem)
		
	def list_all_doctors(self):
		res = []
		for i in self._employees:
			if isinstance(i, Doctors):
				res.append(type(i).__name__)
		return res
	
	def list_all_non_doctors(self):
		res = []
		for i in self._employees:
			if not isinstance(i, Doctors):
				res.append(type(i).__name__)
		return res
				
class Patients:
	def __init__(self, name, age, problem):
		self._firstname = name[:name.find(' ')].lower()
		self._lastname = name[name.find(' ')+1:].lower()
		self._age = age
		self._problem = problem

class Employees(ABC):
	
	default_salary = 70000
	
	def __init__(self, name, age):
		self._firstname = name[:name.find(' ')].lower()
		self._lastname = name[name.find(' ')+1:].lower()
		self._age = age
		self.salary = Employees.default_salary
	
	def _salary(self):
		return str(self.salary) + ' CHF'

class Doctors(Employees,ABC):
	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title
		self.salary = 100000 + (100000 * age * 0.01)
		
	def _works(self):
		return 'The: {} name is: {} {} and has the following titles: {}'.format(type(self).__name__, self._firstname, self._lastname, self._title)
	
	def treat(self, other):
		if not isinstance(other, Patients):
			raise Warning('There is no patient')
		other._problem = ''

class CoronaSpecialist(Doctors):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'corona'

class FluSpecialist(Doctors):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'flu'

class Surgeon(Doctors):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'tumor'

class Ophtalmologist(Doctors):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'Ophtalmologist'

class Administration(Employees):
	def _breaks(self):
		self._has_often_breaks = True

class Janitor(Employees):
	pass

class Administrator(Employees):
	pass

if __name__ == '__main__':
	emp = [
		CoronaSpecialist('Matthias Imhof', 24, 'Dr. Dr. PHD'),
		FluSpecialist('Matthias2 Imhof2', 24, 'Dr. Dr. PHD'),
		Surgeon('Matthias3 Imhof3', 24, 'Dr. Dr. PHD'),
		Ophtalmologist('Matthias4 Imhof4', 24, 'Dr. Dr. PHD'),
		Administration('Matthias5 Imhof5', 24),
		Janitor('Matthias6 Imhof6', 24)
	]
	
	h1 = Hospital('Weid',emp)
	h2 = Hospital('Unispital Zurich',emp)
	
	patient0 = Patients('Max Muster', 60, 'corona')
	patient_gandalf = Patients('Wizzard Gandalf', 30000, 'weed overdose')
	
	print(patient0._problem)
	print(h1.find_doctor(patient0))
	print(patient0._problem)
	print()
	print(patient_gandalf._problem)
	print(h1.find_doctor(patient_gandalf))
	print(h2.find_doctor(patient_gandalf))
	print(patient_gandalf._problem)
	print()
	print(h1.list_all_doctors())
	print(h1.list_all_non_doctors())
	
	print(emp[1]._works())
	
	
	