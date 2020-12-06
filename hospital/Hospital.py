from abc import ABC, abstractmethod

class Hospital:
	def __init__(self, hospitalname, employees):
		if not hospitalname or not employees:
			raise Warning('No Parameters were given')
		self._hospitalname = hospitalname
		try:
			if type(employees) != list:
				self._employees = [employees]
			else:
				self._employees = employees
		except:
			raise Warning('Not given in a list')

	def find_doctor(self,patient):
		result = []
		for problem in patient._problem[:]:
			for i in self._employees:
				if isinstance(i, Doctor):
					if problem.lower() == i.can_treat.lower():
						temp = problem
						i.treat(patient, problem)
						result.append('Problem: {} could be treated and the patient: {} {} is healthy again :)'.format(temp, patient._firstname,patient._lastname))
						
		if len(result) == 0:
			if len(patient._problem) > 0:
				result.append('Patient: {} {} couldn\'t be treated as there is no doctor in the {} hospital to treat: {}'.format(patient._firstname, patient._lastname, self._hospitalname, patient._problem))
			else:
				result.append('Patient: {} {} couldn\'t be treated as there seems to be no problems with patient'.format(patient._firstname, patient._lastname))
		return result
	
	def list_all_doctors(self):
		res = []
		for i in self._employees:
			if isinstance(i, Doctor):
				res.append(type(i).__name__)
		return res
	
	def list_all_non_doctors(self):
		res = []
		for i in self._employees:
			if not isinstance(i, Doctor):
				res.append(type(i).__name__)
		return res
	
	def add_emp(self, employee):
		if isinstance(employee, Employee):
			self._employees.append(employee)
			return 'Successfully added the following employee: {}'.format(employee)
		elif isinstance(employee, list):
			for i in employee:
				if isinstance(i, Employee):
					self._employees.append(i)
			return 'Successfully added the list of the following employees: {}'.format(employee)
		else:
			raise Warning('Object is not a valid object of Employee')
			
	def rem_emp(self, employee):
		if isinstance(employee, Employee):
			for i in self._employees:
				if i == employee:
					self._employees.remove(employee)
					return 'Successfully removed {} the employee from the {} Hospital'.format(employee,self._hospitalname)
		else:
			raise Warning('Not a valid Employee of this Hospital')
		
class Patient:
	def __init__(self, name, age, problem):
		self._firstname = name[:name.find(' ')].lower()
		self._lastname = name[name.find(' ')+1:].lower()
		self._age = age
	
		try:
			if type(problem) != list:
				self._problem = [problem]
			else:
				self._problem = problem
		except:
			raise Warning('Not given in a list')

class Employee(ABC):
	
	default_salary = 70000
	__id = 0
	
	def __init__(self, name, age):
		self._firstname = name[:name.find(' ')].lower()
		self._lastname = name[name.find(' ')+1:].lower()
		self._age = age
		self.salary = Employee.default_salary
		self.__id = Employee.__id
		Employee.__id += 1
	
	def _salary(self):
		return str(self.salary) + ' CHF'
	
	def _works(self):
		return 'The: {} name is: {} {}'.format(type(self).__name__, self._firstname, self._lastname)
	
	def __repr__(self):
		return '{} {} {} {}'.format(type(self).__name__, self._firstname, self._lastname, self.salary)
	
	def __eq__(self, other):
		if not isinstance(other, Employee):
			raise Warning('other is not an Employee')
		return self.__id == other.__id and self._firstname == other._firstname and self._lastname == other._lastname and self._age == other._age and self._salary == other._salary 

class Doctor(Employee,ABC):
	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title
		self.salary = 100000 + (100000 * age * 0.01)
		
	def _works(self):
		return 'The: {} name is: {} {} and has the following titles: {}'.format(type(self).__name__, self._firstname, self._lastname, self._title)
	
	@abstractmethod
	def treat(self, other, problem):
		pass
		
	def __repr__(self):
		return super().__repr__() + ' {} {}'.format(self._title, self.can_treat)
	
	def __eq__(self, other):
		if not isinstance(other, Doctor):
			return False
		return self._firstname == other._firstname and self._lastname == other._lastname and self._age == other._age and self.salary == other.salary and self._title == other._title and self.can_treat == other.can_treat

class CoronaSpecialist(Doctor):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'corona'
		
	def treat(self, other,problem):
		if not isinstance(other, Patient):
			raise Warning('There is no patient')
		other._problem.remove(problem)
		print('{} {} {} removed {} {} {}'.format(type(self).__name__, self._firstname, self._lastname, other._firstname, other._lastname, problem))

class FluSpecialist(Doctor):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'flu'
	
	def treat(self, other,problem):
		if not isinstance(other, Patient):
			raise Warning('There is no patient')
		other._problem.remove(problem)
		print('{} {} {} removed {} {} {}'.format(type(self).__name__, self._firstname, self._lastname, other._firstname, other._lastname, problem))

class Surgeon(Doctor):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'tumor'
		
	def treat(self, other,problem):
		if not isinstance(other, Patient):
			raise Warning('There is no patient')
		other._problem.remove(problem)
		print('{} {} {} removed {} {} {}'.format(type(self).__name__, self._firstname, self._lastname, other._firstname, other._lastname, problem))

class Ophtalmologist(Doctor):
	def __init__(self, name, age, title):
		super().__init__(name, age, title)
		self.can_treat = 'Ophtalmologist'
	
	def treat(self, other,problem):
		if not isinstance(other, Patient):
			raise Warning('There is no patient')
		other._problem.remove(problem)
		print('{} {} {} removed {} {} {}'.format(type(self).__name__, self._firstname, self._lastname, other._firstname, other._lastname, problem))

class Administration(Employee):
	def _breaks(self):
		self._has_often_breaks = True

class Janitor(Employee):
	pass

class Administrator(Employee):
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
	emp2 = [
		CoronaSpecialist('Matthias Imhof', 24, 'Dr. Dr. PHD'),
		Administration('Matthias5 Imhof5', 24),
		Janitor('Matthias6 Imhof6', 24)
	]
	
	h1 = Hospital('Weid',emp)
	h2 = Hospital('Unispital Zurich',emp2)
	
	print(h2.add_emp([Ophtalmologist('Matthias4 Imhof4', 24, 'Dr. Dr. PHD'), FluSpecialist('Matthias2 Imhof2', 24, 'Dr. Dr. PHD')]))
	print(h2.list_all_doctors())
	print(h2.rem_emp(Ophtalmologist('Matthias4 Imhof4', 24, 'Dr. Dr. PHD')))
	print(h2.list_all_doctors())
	print()
	
	patient0 = Patient('Max Muster', 60, ['corona','tumor','flu'])
	patient_gandalf = Patient('Wizzard Gandalf', 30000, 'weed overdose')
	
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
	
	
	
	