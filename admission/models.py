from django.db import models

cat_choices = (
    ('Gen','Gen'),
    ('OBC','OBC'),
    ('ST','ST'),
    ('SC','SC')
)

course_choices = (
    ('B. Tech.','B. Tech'),
    ('MCA','MCA')
)

apply_year = (
    ('1','1st Year'),
    ('2','2nd Year')
)

passing_year = [(str(i),str(i)) for i in range(2000,2019)]

# ImageLoad Location
def upload_location(instance, filename):
    return "CandidateImages/%s/%s" % (instance,filename)

# high school details model 
class HighSchool(models.Model):
    highSchoolPassingYear = models.CharField(max_length= 16, choices=passing_year)
    highSchoolBoard = models.CharField(max_length = 64)
    highSchoolPercentageMarks = models.CharField(max_length=3)
    highSchoolResultImage = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.board
    
# Intermediate details model 
class Intermediate(models.Model):
    intermediatePassingYear = models.CharField(max_length= 16, choices=passing_year)
    intermediateBoard = models.CharField(max_length = 64)
    intermediatePercentageMarks = models.CharField(max_length=3)
    intermediateResultImage = models.ImageField(upload_to=upload_location)

    # marks for diffrent Importent subject
    math = models.IntegerField( default = 0, null = True)
    physics = models.IntegerField(default = 0, null = True)
    chemistry = models.IntegerField(default = 0, null = True)

    def __str__(self):
        return self.board

# UG or Diploma details fields
class UgOrDiploma(models.Model):
    ugOrDiplompassingYear = models.CharField(max_length= 16, choices=passing_year)
    ugOrDiplomBoard = models.CharField(max_length = 64)
    ugOrDiplomBranch = models.CharField(max_length = 32)
    ugOrDiplomPercentageMarks = models.CharField(max_length=3)
    ugOrDiplomResultimage = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.board

# upsee details fields
class Upsee(models.Model):
    rank = models.IntegerField(null= True)
    catRank = models.IntegerField(null = True)
    upseeRollNo = models.IntegerField(null = True)

    def __str__(self):
        return str(self.rank)

# Condidate pername details
class Candidate(models.Model):
    applyYear = models.CharField(max_length= 16, choices= apply_year)
    aadharNo = models.CharField(max_length=16)
    name = models.CharField(max_length=64)
    fatherName = models.CharField(max_length = 64)
    dob = models.DateTimeField()
    category = models.CharField(max_length=4, choices = cat_choices)
    address = models.CharField(max_length=256)
    course = models.CharField(max_length=16, choices = course_choices)
    mobileNo = models.CharField(max_length=12)
    guardianIncome = models.IntegerField()

    # Academic details
    highSchoole = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    intermediate = models.ForeignKey(Intermediate, on_delete = models.CASCADE)
    ugOrDiploma = models.ForeignKey(UgOrDiploma, on_delete = models.CASCADE)
    upsee = models.ForeignKey(Upsee, on_delete = models.CASCADE)
    
    image = models.ImageField(upload_to=upload_location)
    signImage = models.ImageField(upload_to=upload_location)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
