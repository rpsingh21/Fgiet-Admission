from django.db import models

cat_choices = (
    ('Gen','Gen'),
    ('OBC','OBC'),
    ('ST','ST'),
    ('SC','SC')
)

course_choices = (
    ('BTech','Bachelor of Technology'),
    ('MCA','Master of Computer Application')
)

branch_choices = (
    ('AE','Aeronautical Engineering'),
    ('CSE','Computer Science & Engg.'),
    ('ECE','Electronics & Communication Engg.'),
    ('ME','Mechanical Engg.')
)

apply_year = (
    ('1','1st Year'),
    ('2','2nd Year')
)

gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
    ('Unspecified','Unspecified')
)

passing_year = [(str(i),str(i)) for i in range(2000,2019)]

# ImageLoad Location
def upload_location(instance, filename):
    return "CandidateImages/%s/%s" % (instance,filename)

# Condidate pername details
class Candidate(models.Model):
    registrationNo = models.CharField(max_length=16, blank=True, null=True)
    applyYear = models.CharField(max_length= 16, choices= apply_year)
    aadharNo = models.CharField(max_length=16)
    gender = models.CharField(max_length= 16, choices= gender_choices)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    fatherName = models.CharField(max_length = 64)
    dob = models.DateField()
    category = models.CharField(max_length=4, choices = cat_choices)
    address = models.CharField(max_length=256)
    course = models.CharField(max_length=16, choices = course_choices)
    mobileNo = models.CharField(max_length=10)
    guardianIncome = models.IntegerField()
    image = models.ImageField(upload_to=upload_location)
    signImage = models.ImageField(upload_to=upload_location)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

# high school details model
class HighSchool(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE,related_name="hs")
    highSchoolPassingYear = models.CharField(max_length= 16, choices=passing_year)
    highSchoolBoard = models.CharField(max_length = 64)
    highSchoolRollNo = models.CharField(max_length = 16)
    highSchoolPercentageMarks = models.FloatField()
    highSchoolResultImage = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.candidate.registrationNo

# Intermediate details model
class Intermediate(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="inter")
    intermediatePassingYear = models.CharField(max_length= 16, choices=passing_year)
    intermediateBoard = models.CharField(max_length = 64)
    intermediateRollNo = models.CharField(max_length=32)
    intermediatePercentageMarks = models.FloatField()
    intermediateResultImage = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.candidate.registrationNo

# PCM data table
class PCM(models.Model):
    intermediate = models.OneToOneField(Intermediate, on_delete=models.CASCADE, related_name="pcm")
    math = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()

    def __str__(self):
        return self.intermediate.candidate.registrationNo

# UG or Diploma details fields
class UgOrDiploma(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="ug")
    ugOrDiplompassingYear = models.CharField(max_length=16, choices=passing_year)
    ugOrDiplomBoard = models.CharField(max_length = 64)
    ugOrDiplomRollNo = models.CharField(max_length=16)
    ugOrDiplomBranch = models.CharField(max_length = 32)
    ugOrDiplomPercentageMarks = models.FloatField()
    ugOrDiplomResultimage = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.candidate.registrationNo

# upsee details fields
class Upsee(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="upsee")
    rank = models.IntegerField(blank=True, null=True)
    catRank = models.IntegerField(blank=True, null=True)
    upseeRollNo = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.candidate.registrationNo

# Branch prefrance model
class Branch(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE, related_name="cbranch")
    first = models.CharField(max_length=64, choices=branch_choices)
    second = models.CharField(max_length=64, choices=branch_choices, blank=True, null=True)
    third = models.CharField(max_length=64, choices=branch_choices, blank=True, null=True)
    fourth = models.CharField(max_length=64, choices=branch_choices, blank=True, null=True)

    def __str__(self):
        return self.candidate.registrationNo
