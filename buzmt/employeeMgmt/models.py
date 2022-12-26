from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    @classmethod
    def get_default_pk(cls):
        country, created = cls.objects.get_or_create(name='Mali')
        return country.pk
    def __str__(self):
        return (self.name)

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default=Country.get_default_pk)
    @classmethod
    def get_default_pk(cls):
        city, created = cls.objects.get_or_create(name='Bamako')
        return city.pk    
    def __str__(self):
        return (self.name)

class Office(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=25)
    telephone = models.CharField(max_length=25)
    city = models.ForeignKey(City, on_delete=models.CASCADE,default=City.get_default_pk)
    @classmethod
    def get_default_pk(cls):
        office, created = cls.objects.get_or_create(name='Head Office')
        return office.pk    
    def __str__(self):
        return (self.name)

class Department(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    office = models.ForeignKey(Office, on_delete=models.CASCADE,default=Office.get_default_pk)
    @classmethod
    def get_default_pk(cls):
        department, created = cls.objects.get_or_create(name='Admin')
        return department.pk      
    def __str__(self):
        return (self.name)

class Job(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    level = models.IntegerField
    @classmethod
    def get_default_pk(cls):
        job, created = cls.objects.get_or_create(title='New team member')
        return job.pk        
    def __str__(self):
        return (self.title)

class JobType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    @classmethod
    def get_default_pk(cls):
        jobtype, created = cls.objects.get_or_create(code='FT')
        return jobtype.pk       
    def __str__(self):
        return (self.code)

class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    dob = models.DateField(null=False,default='1900-01-01')
    gender = models.CharField(max_length=1,null=False,default='M')
    address = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=25)
    telephone = models.CharField(max_length=25,default='+223-12-34-56-78')
    city = models.ForeignKey(City, on_delete=models.CASCADE,default=City.get_default_pk)
    jobTitle = models.ForeignKey(Job, on_delete=models.CASCADE,default=Job.get_default_pk)
    jobType = models.ForeignKey(JobType, on_delete=models.CASCADE,default=JobType.get_default_pk)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,default=Department.get_default_pk)


    addedDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['lastName','firstName']
        indexes = [
            models.Index(fields=['lastName','firstName']),
        ]

    @classmethod
    def get_default_pk(cls):
        employee, created = cls.objects.get_or_create(firstName='You',lastName='Yourself')
        return employee.pk  

    def __str__(self):
        return (self.lastName.upper()+', '+self.firstName)

class EmploymentTerm(models.Model):
    salary = models.FloatField(null=False, default=0)
    bonus = models.FloatField(max_length=50)
    startDate = models.DateField(null=False,default='1900-01-01')
    endDate = models.DateField(null=False,default='9999-12-31')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=Employee.get_default_pk)
    def __str__(self):
        return (self.salary)

class JobHistory(models.Model):
    startDate = models.DateField(null=False,default='1900-01-01')
    endDate = models.DateField(null=False,default='9999-12-31')
    activeInd = models.CharField(max_length=1,null=False,default='Y')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=Employee.get_default_pk)
    jobTitle = models.ForeignKey(Job,on_delete=models.CASCADE,default=Job.get_default_pk)
    def __str__(self):
        return (self.jobTitle.title+', Active='+self.activeInd)

class DepartmentHistory(models.Model):
    startDate = models.DateField(null=False,default='1900-01-01')
    endDate = models.DateField(null=False,default='9999-12-31')
    activeInd = models.CharField(max_length=1,null=False,default='Y')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=Employee.get_default_pk)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,default=Department.get_default_pk)
    def __str__(self):
        return (self.department.name+', Active'+self.activeInd)

class Schedule(models.Model):
    code = models.CharField(max_length=10,null=False)
    desc = models.CharField(max_length=25)
    @classmethod
    def get_default_pk(cls):
        schedule, created = cls.objects.get_or_create(code='WW')
        return schedule.pk
    def __str__(self):
        return (self.code)

class WorkHour(models.Model):
    dateWorked = models.DateField(null=False,default='2023-01-01')
    startTime = models.TimeField(null=False,default='09:00')
    endTime = models.TimeField(null=False,default='17:00')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=Employee.get_default_pk)
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,default=Schedule.get_default_pk)
    def __str__(self):
        return (self.dateWorked+' '+self.startTime+' '+self.endTime+' '+self.schedule.code)

class SalaryPayment(models.Model):
    periodStart = models.DateField(null=False,default='2023-01-01')
    periodEnd = models.DateField(null=False,default='2023-01-05')
    grossPayment = models.FloatField
    tax = models.FloatField
    netPayment  = models.FloatField(null=False,default=0)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,default=Employee.get_default_pk)
    def __str__(self):
        return (self.periodStart+' '+self.periodEnd+' '+self.netPayment)